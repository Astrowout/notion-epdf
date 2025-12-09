# Notion PDF Exporter - Nuxt 3

Beautiful, modern web application for exporting Notion pages to professional PDFs with watermarks and page breaks.

Built with **Nuxt 3**, **Tailwind CSS v4**, and **Python**.

## 🎨 Features

- **Nuxt 3** - Latest full-stack Vue framework
- **Tailwind CSS v4** - Latest alpha with CSS-first config
- **Server-Side API** - Built-in API routes with Nitro
- **Beautiful UI** - Distinctive design with smooth animations
- **Easy to Use** - Simple form-based interface
- **Custom Watermarks** - Add watermarks to PDFs
- **Page Break Control** - Use "PAGE BREAK" markers
- **Responsive** - Works on all devices

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ and npm
- Python 3.8+
- Notion integration token

### Installation

1. **Install Node dependencies:**
```bash
npm install
```

2. **Install Python dependencies:**
```bash
pip install reportlab requests
```

3. **Run development server:**
```bash
npm run dev
```

The app will be available at `http://localhost:3000`

## 📦 Project Structure

```
notion-pdf-nuxt/
├── assets/
│   └── css/
│       └── main.css             # Tailwind v4 config & styles
├── components/
│   └── ExportForm.vue           # Export form component
├── pages/
│   └── index.vue                # Home page
├── server/
│   ├── api/
│   │   └── export.post.ts       # API route for PDF export
│   └── scripts/
│       └── export.py            # Python PDF generator
├── app.vue                      # Root component
├── nuxt.config.ts               # Nuxt configuration
├── tailwind.config.js           # Tailwind config
└── package.json                 # Dependencies
```

## 🎯 How It Works

### Frontend (Nuxt 3)
- Vue 3 Composition API
- Tailwind CSS v4 for styling
- File-based routing
- Auto-imported components

### Backend (Nitro Server)
- Built-in API routes at `/api/export`
- Server-side Python execution
- PDF generation with ReportLab
- Automatic cleanup

### API Flow
1. User submits form
2. Frontend sends request to `/api/export`
3. Server calls Python script
4. Python generates PDF from Notion
5. Server returns PDF to browser

## 🎨 Tailwind CSS v4

This project uses Tailwind v4 with the new CSS-first configuration:

### Configuration (assets/css/main.css)

```css
@import "tailwindcss";

@theme {
  --color-accent-primary: #00d4aa;
  --color-bg-primary: #0a0a0a;
  --font-display: 'DM Serif Display', serif;
}
```

### Usage in Components

```vue
<template>
  <div class="bg-[var(--color-bg-primary)] text-white">
    <h1 class="text-4xl font-display">Title</h1>
  </div>
</template>
```

## 🔧 Customization

### Change Colors

Edit `assets/css/main.css`:

```css
@theme {
  --color-accent-primary: #your-color;
  --color-bg-primary: #your-bg;
}
```

### Change Fonts

1. Update Google Fonts in `nuxt.config.ts`
2. Update font variables in `assets/css/main.css`

### Add New Pages

Create `.vue` files in `pages/` directory:

```
pages/
├── index.vue       → /
├── about.vue       → /about
└── docs.vue        → /docs
```

Nuxt auto-generates routes!

### Add New API Routes

Create files in `server/api/` directory:

```
server/api/
├── export.post.ts  → POST /api/export
├── validate.get.ts → GET /api/validate
└── status.get.ts   → GET /api/status
```

## 🌐 Build & Deploy

### Build for Production

```bash
npm run build
```

Generates optimized output in `.output/` directory.

### Preview Production Build

```bash
npm run preview
```

### Generate Static Site

```bash
npm run generate
```

Creates static HTML files in `.output/public/`

## 🚀 Deploy to Vercel

### Option 1: GitHub Integration

1. **Push to GitHub:**
```bash
git init
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Import to Vercel:**
   - Go to vercel.com
   - Import repository
   - Vercel auto-detects Nuxt!
   - Click Deploy

### Option 2: Vercel CLI

```bash
npm install -g vercel
vercel
```

### Environment Variables

Add in Vercel dashboard if needed:
- Settings → Environment Variables

## ⚠️ Python Backend Note

The Python script needs to be executable on the deployment platform.

### For Vercel

Add `vercel.json`:

```json
{
  "functions": {
    "api/*.ts": {
      "maxDuration": 60
    }
  }
}
```

Python may need separate deployment. Alternatives:
- Deploy Python to Railway/Render
- Use Vercel's Python support (beta)
- Convert to Node.js PDF generation

## 📚 Nuxt 3 Features Used

### Auto Imports
- No need to import `ref`, `reactive`, `computed`
- Components auto-imported
- Composables auto-imported

### File-based Routing
- `pages/index.vue` → `/`
- `pages/about.vue` → `/about`

### Server Routes
- `server/api/export.post.ts` → `/api/export`
- Built on Nitro server

### Built-in Composables
- `useHead()` - Meta tags
- `useFetch()` - Data fetching
- `useState()` - Shared state
- `useRoute()` - Current route

## 🎯 Key Differences from Vite Version

### Advantages

✅ **Built-in Server** - No separate backend needed
✅ **File-based Routing** - Pages are auto-routed
✅ **Auto Imports** - Less boilerplate
✅ **Server API** - API routes included
✅ **SEO Ready** - SSR/SSG support
✅ **Type Safety** - TypeScript by default

### Structure

| Vite | Nuxt 3 |
|------|--------|
| `src/App.vue` | `pages/index.vue` |
| `src/components/` | `components/` |
| `src/api/` | `server/api/` |
| `index.html` | `app.vue` |
| Manual routing | File-based routing |

## 🐛 Troubleshooting

### "Cannot find module" errors

```bash
npm install
```

### Port already in use

```bash
npm run dev -- --port 3001
```

### Python not found

```bash
which python3
pip install reportlab requests
```

### Tailwind not working

1. Check `nuxt.config.ts` has `@nuxtjs/tailwindcss`
2. Verify `@import "tailwindcss"` in `main.css`
3. Clear `.nuxt` cache:
```bash
rm -rf .nuxt
npm run dev
```

## 📖 Resources

### Nuxt 3
- [Nuxt 3 Documentation](https://nuxt.com/)
- [Nuxt 3 Examples](https://nuxt.com/docs/examples/hello-world)

### Tailwind CSS v4
- [Tailwind v4 Blog](https://tailwindcss.com/blog/tailwindcss-v4-alpha)
- [Tailwind Docs](https://tailwindcss.com/docs)

### Notion API
- [Notion API Docs](https://developers.notion.com/)

## 💡 Tips

1. **Use Auto Imports**
   ```vue
   <script setup>
   // No imports needed!
   const count = ref(0)
   const data = await useFetch('/api/data')
   </script>
   ```

2. **File-based Routing**
   - Create pages in `pages/` directory
   - Routes are auto-generated

3. **Server API Routes**
   - Create endpoints in `server/api/`
   - Use TypeScript for type safety

4. **Composables**
   - Create reusable logic in `composables/`
   - Auto-imported everywhere

5. **Layouts**
   - Create layouts in `layouts/`
   - Wrap pages with shared UI

## 🌟 What Makes This Special

### Modern Stack
- Nuxt 3 (latest)
- Tailwind CSS v4 (cutting edge)
- Full-stack in one project

### Developer Experience
- Auto imports
- File-based routing
- Hot module replacement
- TypeScript support

### Production Ready
- Server-side rendering
- Static generation
- API routes included
- Optimized builds

## 🎓 Learning Nuxt 3

This project demonstrates:
- Nuxt 3 project structure
- File-based routing
- API routes with Nitro
- Tailwind CSS v4 integration
- Component composition
- Form handling
- File downloads

Perfect for learning modern Vue development!

## 📄 License

MIT License - feel free to use in your projects!

---

**Built with Nuxt 3, Tailwind CSS v4, Python, and ❤️**
