import { exec } from 'child_process'
import { promisify } from 'util'
import { writeFile, unlink, mkdir } from 'fs/promises'
import { join } from 'path'
import { tmpdir } from 'os'
import { existsSync, readFileSync } from 'fs'

const execAsync = promisify(exec)

export default defineEventHandler(async (event) => {
  try {
    const body = await readBody(event)
    const { token, pageId, watermark, pageSize, filename, includePageNumbers } = body

    // Validate inputs
    if (!token || !pageId) {
      throw createError({
        statusCode: 400,
        message: 'Missing required fields: token and pageId'
      })
    }

    // Create temp directory
    const tempDir = join(tmpdir(), `notion-export-${Date.now()}`)
    await mkdir(tempDir, { recursive: true })

    const outputPath = join(tempDir, `${filename || 'notion-export'}.pdf`)

    // Build Python command - try multiple Python paths
    const pythonScript = join(process.cwd(), 'server', 'scripts', 'export.py')
    
    // Possible Python locations
    const pythonPaths = [
      process.env.PYTHON_PATH,
      '/vercel/.pyenv/shims/python3',
      'python3',
      'python'
    ].filter(Boolean)
    
    let pythonCmd = 'python3' // default
    
    // Try to find working python command
    for (const cmd of pythonPaths) {
      try {
        await execAsync(`${cmd} --version`)
        pythonCmd = cmd
        break
      } catch {
        continue
      }
    }
    
    let command = `${pythonCmd} "${pythonScript}" --token "${token}" --page-id "${pageId}" --output "${outputPath}" --page-size "${pageSize || 'letter'}"`
    
    if (watermark) {
      command += ` --watermark "${watermark}"`
    }
    
    if (includePageNumbers) {
      command += ` --page-numbers`
    }

    // Execute Python script
    try {
      await execAsync(command, {
        timeout: 60000, // 60 second timeout
        maxBuffer: 50 * 1024 * 1024 // 50MB buffer
      })
    } catch (execError) {
      console.error('Python execution error:', execError)
      throw createError({
        statusCode: 500,
        message: 'PDF generation failed. Please check your Notion credentials.'
      })
    }

    // Read the generated PDF
    if (!existsSync(outputPath)) {
      throw createError({
        statusCode: 500,
        message: 'PDF file was not generated'
      })
    }

    const pdfBuffer = readFileSync(outputPath)

    // Clean up temp files
    try {
      await unlink(outputPath)
    } catch (cleanupError) {
      console.error('Cleanup error:', cleanupError)
    }

    // Set headers for PDF download
    setResponseHeaders(event, {
      'Content-Type': 'application/pdf',
      'Content-Disposition': `attachment; filename="${filename || 'notion-export'}.pdf"`,
      'Content-Length': pdfBuffer.length.toString()
    })

    return pdfBuffer
  } catch (error) {
    console.error('Export error:', error)
    
    throw createError({
      statusCode: error.statusCode || 500,
      message: error.message || 'Export failed'
    })
  }
})
