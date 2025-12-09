<template>
  <div class="min-h-screen flex flex-col">
    <!-- Hero Section -->
    <header class="relative py-16 md:py-24 text-center overflow-hidden mb-16 md:mb-24">
      <div class="max-w-4xl mx-auto px-6 relative z-10">
        <!-- Badge -->
        <div class="inline-flex items-center gap-2 px-4 py-2 bg-[var(--color-bg-elevated)] border border-[var(--color-border-subtle)] rounded-full text-[var(--color-accent-primary)] text-sm font-medium mb-8 animate-fade-in opacity-0">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none" class="text-[var(--color-accent-primary)]">
            <path d="M10 2L12.5 7.5L18 8L14 12L15 18L10 15L5 18L6 12L2 8L7.5 7.5L10 2Z" fill="currentColor"/>
          </svg>
          <span>Transform Notion into PDFs</span>
        </div>
        
        <!-- Title -->
        <h1 class="font-display text-5xl md:text-7xl leading-tight mb-6 opacity-0 animate-slide-up" style="animation-delay: 0.1s">
          Export Your <span class="text-gradient">Notion Pages</span><br/>
          to Professional PDFs
        </h1>
        
        <!-- Description -->
        <p class="text-xl text-[var(--color-text-secondary)] mx-auto mb-8 leading-relaxed opacity-0 animate-slide-up" style="animation-delay: 0.2s">
          Add watermarks, control page breaks, and maintain beautiful formatting.
          Built for teams who care about presentation.
        </p>
        
        <!-- Features Pills -->
        <div class="flex flex-wrap gap-3 justify-center opacity-0 animate-slide-up" style="animation-delay: 0.3s">
          <div v-for="feature in heroPills" :key="feature" class="flex items-center gap-2 px-4 py-2 bg-[var(--color-bg-secondary)] border border-[var(--color-border-subtle)] rounded-full text-[var(--color-text-secondary)] text-sm font-medium">
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none" class="text-[var(--color-accent-primary)]">
              <path d="M13 4L6 11L3 8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span>{{ feature }}</span>
          </div>
        </div>
      </div>
      
      <!-- Decorative Elements -->
      <div class="absolute inset-0 pointer-events-none overflow-hidden">
        <div class="absolute w-96 h-96 -top-48 -left-24 rounded-full border border-[var(--color-border-subtle)] animate-float"></div>
        <div class="absolute w-72 h-72 -bottom-36 -right-12 rounded-full border border-[var(--color-border-subtle)] animate-float" style="animation-duration: 15s; animation-direction: reverse;"></div>
        <div class="absolute top-1/5 left-1/10 w-48 h-px bg-gradient-to-r from-transparent via-[var(--color-border-subtle)] to-transparent -rotate-45 animate-pulse-subtle"></div>
        <div class="absolute bottom-1/3 right-1/6 w-48 h-px bg-gradient-to-r from-transparent via-[var(--color-border-subtle)] to-transparent rotate-45 animate-pulse-subtle" style="animation-delay: 0.5s;"></div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="flex-1 px-6 pb-16 md:pb-24">
      <!-- Export Form Container -->
      <div class="max-w-3xl mx-auto mb-16 md:mb-24 opacity-0 animate-scale-in" style="animation-delay: 0.4s">
        <ExportForm 
          @export-start="handleExportStart"
          @export-complete="handleExportComplete"
          @export-error="handleExportError"
        />
      </div>

      <!-- Status Message -->
      <Transition name="slide-up">
        <div v-if="statusMessage" 
             class="fixed bottom-8 left-1/2 -translate-x-1/2 flex items-center gap-4 px-6 py-4 bg-[var(--color-bg-elevated)] border border-[var(--color-border-medium)] rounded-xl shadow-[var(--shadow-lg)] backdrop-blur-xl z-50 max-w-[90vw]"
             :class="{
               'border-[var(--color-success)]': statusType === 'success',
               'border-[var(--color-error)]': statusType === 'error',
               'border-[var(--color-info)]': statusType === 'info'
             }">
          <div class="flex items-center justify-center w-8 h-8 rounded-full flex-shrink-0"
               :class="{
                 'bg-[var(--color-success)]/10 text-[var(--color-success)]': statusType === 'success',
                 'bg-[var(--color-error)]/10 text-[var(--color-error)]': statusType === 'error',
                 'bg-[var(--color-info)]/10 text-[var(--color-info)]': statusType === 'info'
               }">
            <svg v-if="statusType === 'success'" width="20" height="20" viewBox="0 0 20 20" fill="none">
              <path d="M16 5L7.5 13.5L4 10" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <svg v-else-if="statusType === 'error'" width="20" height="20" viewBox="0 0 20 20" fill="none">
              <path d="M10 6V10M10 14H10.01M19 10C19 14.9706 14.9706 19 10 19C5.02944 19 1 14.9706 1 10C1 5.02944 5.02944 1 10 1C14.9706 1 19 5.02944 19 10Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <svg v-else width="20" height="20" viewBox="0 0 20 20" fill="none">
              <circle cx="10" cy="10" r="8" stroke="currentColor" stroke-width="2"/>
              <circle cx="10" cy="10" r="3" fill="currentColor"/>
            </svg>
          </div>
          <span class="text-[var(--color-text-primary)]">{{ statusMessage }}</span>
        </div>
      </Transition>

      <!-- How It Works Section -->
      <section class="max-w-5xl mx-auto mb-16 md:mb-24">
        <h2 class="font-display text-4xl md:text-5xl text-center mb-12 md:mb-16">How It Works</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          <div v-for="(step, index) in steps" :key="index" class="text-center p-6">
            <div class="inline-flex items-center justify-center w-12 h-12 bg-gradient-to-br from-[var(--color-accent-primary)] to-[var(--color-accent-secondary)] rounded-full font-display text-2xl text-[var(--color-bg-primary)] mb-4">
              {{ index + 1 }}
            </div>
            <h3 class="font-display text-lg mb-2">{{ step.title }}</h3>
            <p class="text-sm text-[var(--color-text-tertiary)] leading-relaxed">{{ step.description }}</p>
          </div>
        </div>
      </section>

      <!-- Features Section -->
      <section class="max-w-6xl mx-auto">
        <h2 class="font-display text-4xl md:text-5xl text-center mb-12 md:mb-16">Powerful Features</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8">
          <div v-for="(feature, index) in features" :key="index" 
               class="p-6 md:p-8 bg-[var(--color-bg-secondary)] border border-[var(--color-border-subtle)] rounded-2xl transition-all duration-300 hover:border-[var(--color-border-medium)] hover:-translate-y-1 hover:shadow-[var(--shadow-md)]">
            <div class="w-12 h-12 flex items-center justify-center bg-[var(--color-accent-primary)]/10 rounded-xl text-[var(--color-accent-primary)] mb-4" v-html="feature.icon"></div>
            <h3 class="font-display text-lg mb-2">{{ feature.title }}</h3>
            <p class="text-sm text-[var(--color-text-tertiary)] leading-relaxed">{{ feature.description }}</p>
          </div>
        </div>
      </section>
    </main>

    <!-- Footer -->
    <footer class="mt-auto pt-16 md:pt-24 pb-8 border-t border-[var(--color-border-subtle)]">
      <div class="max-w-6xl mx-auto px-6">
        <div class="flex flex-col md:flex-row justify-between items-start gap-12 mb-8">
          <div>
            <h3 class="font-display text-xl mb-2">Notion PDF Exporter</h3>
            <p class="text-sm text-[var(--color-text-tertiary)]">Transform your Notion pages into professional PDFs</p>
          </div>
          <div class="flex gap-8">
            <a href="https://developers.notion.com/" target="_blank" rel="noopener" class="text-[var(--color-text-secondary)] text-sm hover:text-[var(--color-accent-primary)] transition-colors">Notion API</a>
            <a href="https://github.com" target="_blank" rel="noopener" class="text-[var(--color-text-secondary)] text-sm hover:text-[var(--color-accent-primary)] transition-colors">GitHub</a>
            <a href="#" @click.prevent="showDocs" class="text-[var(--color-text-secondary)] text-sm hover:text-[var(--color-accent-primary)] transition-colors">Documentation</a>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
useHead({
  htmlAttrs: {
    lang: 'en'
  }
})

const statusMessage = ref('')
const statusType = ref('info')

const heroPills = ['Vector Output', 'Custom Watermarks', 'Page Breaks']

const steps = [
  {
    title: 'Setup Integration',
    description: 'Create a Notion integration and get your API token from notion.so/my-integrations'
  },
  {
    title: 'Share Your Page',
    description: 'Share the Notion page with your integration to grant access'
  },
  {
    title: 'Enter Details',
    description: 'Paste your page ID and token, customize watermark and settings'
  },
  {
    title: 'Export PDF',
    description: 'Click export and download your beautifully formatted PDF'
  }
]

const features = [
  {
    icon: '<svg width="32" height="32" viewBox="0 0 32 32" fill="none"><path d="M16 4V28M4 16H28" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    title: 'Page Break Control',
    description: 'Add "PAGE BREAK" text in Notion to control exactly where pages split in your PDF'
  },
  {
    icon: '<svg width="32" height="32" viewBox="0 0 32 32" fill="none"><rect x="6" y="6" width="20" height="20" rx="2" stroke="currentColor" stroke-width="2"/><path d="M11 11L21 21M21 11L11 21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    title: 'Custom Watermarks',
    description: 'Add "DRAFT", "CONFIDENTIAL", or any custom watermark text to every page'
  },
  {
    icon: '<svg width="32" height="32" viewBox="0 0 32 32" fill="none"><path d="M8 12H24M8 16H24M8 20H16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    title: 'Rich Formatting',
    description: 'Preserves headings, lists, quotes, code blocks, and all Notion formatting'
  },
  {
    icon: '<svg width="32" height="32" viewBox="0 0 32 32" fill="none"><path d="M16 28C22.6274 28 28 22.6274 28 16C28 9.37258 22.6274 4 16 4C9.37258 4 4 9.37258 4 16C4 22.6274 9.37258 28 16 28Z" stroke="currentColor" stroke-width="2"/><path d="M16 8V16L20 20" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
    title: 'Fast Export',
    description: 'Generate PDFs in seconds with high-quality vector output and embedded fonts'
  },
  {
    icon: '<svg width="32" height="32" viewBox="0 0 32 32" fill="none"><rect x="4" y="8" width="24" height="16" rx="2" stroke="currentColor" stroke-width="2"/><path d="M4 12H28" stroke="currentColor" stroke-width="2"/></svg>',
    title: 'Professional Output',
    description: 'Vector-based PDFs with searchable text that scale perfectly at any resolution'
  },
  {
    icon: '<svg width="32" height="32" viewBox="0 0 32 32" fill="none"><path d="M20 4H8C6.89543 4 6 4.89543 6 6V26C6 27.1046 6.89543 28 8 28H24C25.1046 28 26 27.1046 26 26V10L20 4Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M20 4V10H26" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    title: 'Multiple Formats',
    description: 'Export to Letter or A4 page sizes to match your regional requirements'
  }
]

const handleExportStart = () => {
  statusMessage.value = 'Exporting your Notion page...'
  statusType.value = 'info'
}

const handleExportComplete = (filename) => {
  statusMessage.value = `✓ Successfully exported: ${filename}`
  statusType.value = 'success'
  setTimeout(() => {
    statusMessage.value = ''
  }, 5000)
}

const handleExportError = (error) => {
  statusMessage.value = `Export failed: ${error}`
  statusType.value = 'error'
  setTimeout(() => {
    statusMessage.value = ''
  }, 8000)
}

const showDocs = () => {
  alert('Documentation: Check the README.md file in your project!')
}
</script>

<style scoped>
.slide-up-enter-active,
.slide-up-leave-active {
  transition: all 250ms cubic-bezier(0.4, 0, 0.2, 1);
}

.slide-up-enter-from {
  opacity: 0;
  transform: translateY(20px);
}

.slide-up-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}
</style>
