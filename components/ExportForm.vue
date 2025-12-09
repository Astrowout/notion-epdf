<template>
  <div class="bg-[var(--color-bg-secondary)] border border-[var(--color-border-subtle)] rounded-3xl p-8 md:p-12 shadow-[var(--shadow-md)]">
    <!-- Header -->
    <div class="text-center mb-12 pb-8 border-b border-[var(--color-border-subtle)]">
      <h2 class="font-display text-3xl mb-2">Export Configuration</h2>
      <p class="text-[var(--color-text-tertiary)] text-sm">Configure your PDF export settings</p>
    </div>

    <!-- Form -->
    <form @submit.prevent="handleSubmit" class="flex flex-col gap-8">
      <!-- Notion Token -->
      <div class="flex flex-col gap-2">
        <label for="token" class="flex items-center gap-2 font-medium text-sm">
          Notion Integration Token
          <span class="text-[var(--color-accent-primary)] text-sm">*</span>
        </label>
        <div class="relative">
          <input
            id="token"
            v-model="formData.token"
            :type="showToken ? 'text' : 'password'"
            placeholder="secret_..."
            class="w-full px-4 py-3.5 pr-12 bg-[var(--color-bg-elevated)] border border-[var(--color-border-subtle)] rounded-xl text-[var(--color-text-primary)] transition-all duration-300 hover:border-[var(--color-border-medium)] focus:border-[var(--color-accent-primary)] focus:shadow-[0_0_0_3px_rgba(0,212,170,0.1)]"
            required
          />
          <button
            type="button"
            @click="showToken = !showToken"
            class="absolute right-3 top-1/2 -translate-y-1/2 p-1 text-[var(--color-text-tertiary)] hover:text-[var(--color-text-primary)] hover:bg-white/5 rounded-lg transition-all"
            aria-label="Toggle token visibility"
          >
            <svg v-if="!showToken" width="20" height="20" viewBox="0 0 20 20" fill="none">
              <path d="M10 4C4.5 4 2 10 2 10s2.5 6 8 6 8-6 8-6-2.5-6-8-6z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              <circle cx="10" cy="10" r="2" stroke="currentColor" stroke-width="1.5"/>
            </svg>
            <svg v-else width="20" height="20" viewBox="0 0 20 20" fill="none">
              <path d="M3 3l14 14M10 7a3 3 0 013 3m-6 0a3 3 0 003 3m5-3s-2.5-6-8-6m-6 6s2.5 6 8 6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg>
          </button>
        </div>
        <p class="text-xs text-[var(--color-text-tertiary)]">
          Get your token at <a href="https://www.notion.so/my-integrations" target="_blank" rel="noopener" class="text-[var(--color-accent-primary)] underline">notion.so/my-integrations</a>
        </p>
      </div>

      <!-- Page ID -->
      <div class="flex flex-col gap-2">
        <label for="pageId" class="flex items-center gap-2 font-medium text-sm">
          Notion Page ID
          <span class="text-[var(--color-accent-primary)] text-sm">*</span>
        </label>
        <input
          id="pageId"
          v-model="formData.pageId"
          type="text"
          placeholder="abc123def456..."
          class="w-full px-4 py-3.5 bg-[var(--color-bg-elevated)] border border-[var(--color-border-subtle)] rounded-xl text-[var(--color-text-primary)] transition-all duration-300 hover:border-[var(--color-border-medium)] focus:border-[var(--color-accent-primary)] focus:shadow-[0_0_0_3px_rgba(0,212,170,0.1)]"
          required
        />
        <p class="text-xs text-[var(--color-text-tertiary)]">
          Found in your page URL: notion.so/Page-Name-<span class="font-mono text-[var(--color-text-secondary)]">PAGE_ID</span>
        </p>
      </div>

      <!-- Watermark -->
      <div class="flex flex-col gap-2">
        <label for="watermark" class="flex items-center gap-2 font-medium text-sm">
          Watermark Text
          <span class="text-[var(--color-text-tertiary)] text-xs font-normal">Optional</span>
        </label>
        <input
          id="watermark"
          v-model="formData.watermark"
          type="text"
          placeholder="DRAFT, CONFIDENTIAL, etc."
          maxlength="50"
          class="w-full px-4 py-3.5 bg-[var(--color-bg-elevated)] border border-[var(--color-border-subtle)] rounded-xl text-[var(--color-text-primary)] transition-all duration-300 hover:border-[var(--color-border-medium)] focus:border-[var(--color-accent-primary)] focus:shadow-[0_0_0_3px_rgba(0,212,170,0.1)]"
        />
        <p class="text-xs text-[var(--color-text-tertiary)]">
          Add custom text that appears on every page
        </p>
      </div>

      <!-- Page Size -->
      <div class="flex flex-col gap-2">
        <label class="font-medium text-sm">Page Size</label>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <label class="relative flex items-start gap-3 p-4 bg-[var(--color-bg-elevated)] border border-[var(--color-border-subtle)] rounded-xl cursor-pointer transition-all hover:border-[var(--color-border-medium)] has-[:checked]:border-[var(--color-accent-primary)] has-[:checked]:bg-[var(--color-accent-primary)]/5">
            <input
              type="radio"
              v-model="formData.pageSize"
              value="letter"
              name="pageSize"
              class="mt-0.5 w-5 h-5 accent-[var(--color-accent-primary)] cursor-pointer"
            />
            <div class="flex-1">
              <div class="font-medium text-sm">Letter</div>
              <div class="text-xs text-[var(--color-text-tertiary)]">8.5" × 11" (US)</div>
            </div>
          </label>
          <label class="relative flex items-start gap-3 p-4 bg-[var(--color-bg-elevated)] border border-[var(--color-border-subtle)] rounded-xl cursor-pointer transition-all hover:border-[var(--color-border-medium)] has-[:checked]:border-[var(--color-accent-primary)] has-[:checked]:bg-[var(--color-accent-primary)]/5">
            <input
              type="radio"
              v-model="formData.pageSize"
              value="a4"
              name="pageSize"
              class="mt-0.5 w-5 h-5 accent-[var(--color-accent-primary)] cursor-pointer"
            />
            <div class="flex-1">
              <div class="font-medium text-sm">A4</div>
              <div class="text-xs text-[var(--color-text-tertiary)]">210mm × 297mm (International)</div>
            </div>
          </label>
        </div>
      </div>

      <!-- Advanced Options Toggle -->
      <div class="pt-8 border-t border-[var(--color-border-subtle)]">
        <button
          type="button"
          @click="showAdvanced = !showAdvanced"
          class="flex items-center justify-between w-full py-2 text-[var(--color-text-primary)] font-medium hover:text-[var(--color-accent-primary)] transition-colors"
        >
          <span>Advanced Options</span>
          <svg
            width="16"
            height="16"
            viewBox="0 0 16 16"
            fill="none"
            class="transition-transform duration-300"
            :class="{ 'rotate-180': showAdvanced }"
          >
            <path d="M4 6L8 10L12 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>

        <Transition
          enter-active-class="transition-all duration-300 ease-out"
          enter-from-class="opacity-0 max-h-0"
          enter-to-class="opacity-100 max-h-[500px]"
          leave-active-class="transition-all duration-300 ease-in"
          leave-from-class="opacity-100 max-h-[500px]"
          leave-to-class="opacity-0 max-h-0"
        >
          <div v-if="showAdvanced" class="flex flex-col gap-8 mt-8 overflow-hidden">
            <!-- Output Filename -->
            <div class="flex flex-col gap-2">
              <label for="filename" class="font-medium text-sm">Output Filename</label>
              <div class="relative">
                <input
                  id="filename"
                  v-model="formData.filename"
                  type="text"
                  placeholder="my-document"
                  class="w-full px-4 py-3.5 pr-16 bg-[var(--color-bg-elevated)] border border-[var(--color-border-subtle)] rounded-xl text-[var(--color-text-primary)] transition-all duration-300 hover:border-[var(--color-border-medium)] focus:border-[var(--color-accent-primary)] focus:shadow-[0_0_0_3px_rgba(0,212,170,0.1)]"
                />
                <span class="absolute right-4 top-1/2 -translate-y-1/2 text-[var(--color-text-tertiary)] pointer-events-none">.pdf</span>
              </div>
            </div>

            <!-- Include Page Numbers -->
            <label class="flex items-start gap-3 p-4 bg-[var(--color-bg-elevated)] border border-[var(--color-border-subtle)] rounded-xl cursor-pointer transition-all hover:border-[var(--color-border-medium)]">
              <input
                type="checkbox"
                v-model="formData.includePageNumbers"
                class="mt-0.5 w-5 h-5 accent-[var(--color-accent-primary)] cursor-pointer"
              />
              <div class="flex-1">
                <div class="font-medium text-sm">Include Page Numbers</div>
                <div class="text-xs text-[var(--color-text-tertiary)]">Add page numbers to footer</div>
              </div>
            </label>
          </div>
        </Transition>
      </div>

      <!-- Submit Button -->
      <button
        type="submit"
        class="w-full px-8 py-4 bg-gradient-to-r from-[var(--color-accent-primary)] to-[var(--color-accent-secondary)] text-[var(--color-bg-primary)] font-semibold text-base rounded-xl shadow-[var(--shadow-accent)] transition-all duration-300 hover:-translate-y-0.5 hover:shadow-[0_12px_40px_rgba(0,212,170,0.4)] active:translate-y-0 disabled:opacity-70 disabled:cursor-not-allowed disabled:hover:translate-y-0"
        :disabled="isExporting"
      >
        <span v-if="!isExporting" class="flex items-center justify-center gap-2">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
            <path d="M10 4V12M10 12L7 9M10 12L13 9M3 16H17" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <span>Export to PDF</span>
        </span>
        <span v-else class="flex items-center justify-center gap-2">
          <div class="w-5 h-5 border-2 border-[var(--color-bg-primary)]/30 border-t-[var(--color-bg-primary)] rounded-full animate-spin"></div>
          <span>Exporting...</span>
        </span>
      </button>

      <!-- Error Message -->
      <Transition
        enter-active-class="transition-all duration-300 ease-out"
        enter-from-class="opacity-0 -translate-y-2"
        leave-active-class="transition-all duration-300 ease-in"
        leave-to-class="opacity-0 translate-y-2"
      >
        <div v-if="error" class="flex items-center gap-3 p-4 bg-[var(--color-error)]/10 border border-[var(--color-error)]/30 rounded-xl text-[var(--color-error)]">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
            <path d="M10 6V10M10 14H10.01M19 10C19 14.9706 14.9706 19 10 19C5.02944 19 1 14.9706 1 10C1 5.02944 5.02944 1 10 1C14.9706 1 19 5.02944 19 10Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <span class="text-sm">{{ error }}</span>
        </div>
      </Transition>
    </form>
  </div>
</template>

<script setup>
const emit = defineEmits(['export-start', 'export-complete', 'export-error'])

const showToken = ref(false)
const showAdvanced = ref(false)
const isExporting = ref(false)
const error = ref('')

const formData = reactive({
  token: '',
  pageId: '',
  watermark: '',
  pageSize: 'letter',
  filename: '',
  includePageNumbers: true
})

const handleSubmit = async () => {
  error.value = ''
  isExporting.value = true
  emit('export-start')

  try {
    const response = await $fetch('/api/export', {
      method: 'POST',
      body: {
        token: formData.token,
        pageId: formData.pageId,
        watermark: formData.watermark || null,
        pageSize: formData.pageSize,
        filename: formData.filename || 'notion-export',
        includePageNumbers: formData.includePageNumbers
      },
      responseType: 'blob'
    })

    // Create download
    const filename = `${formData.filename || 'notion-export'}.pdf`
    const url = URL.createObjectURL(response)
    const link = document.createElement('a')
    link.href = url
    link.download = filename
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
    URL.revokeObjectURL(url)

    emit('export-complete', filename)
  } catch (err) {
    const errorMessage = err.data?.error || err.message || 'Export failed'
    error.value = errorMessage
    emit('export-error', errorMessage)
  } finally {
    isExporting.value = false
  }
}
</script>
