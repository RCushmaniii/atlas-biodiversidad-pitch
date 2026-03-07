# CLAUDE.md — BioJalisco Pitch Site

## Project Overview
Bilingual (ES/EN) scrollytelling single-file HTML site presenting the BioJalisco citizen-science biodiversity platform vision for western Mexico. This is a persuasion/pitch site, not the platform itself. All images are embedded as base64 data URIs for a fully self-contained deployment.

Includes a **Species Identifier** tool — an AI-powered species/breed identification feature using GPT-4o vision, deployed as a Vercel serverless function with a secret link from the pitch site footer.

## Tech Stack
- Single-file HTML/CSS/JS (no build step, no dependencies) for the pitch site
- Google Fonts (Playfair Display, Source Sans 3, Cormorant Garamond)
- Intersection Observer API for scroll-triggered reveal animations
- Web Audio API for ambient forest soundscape
- **Species Identifier**: Python (Flask local dev) + Vercel serverless function + OpenAI GPT-4o vision API
- Vercel for static hosting + serverless functions

## Project Structure
```
biojalisco-pitch/
├── index.html              ← The pitch site (single file, ~1.8MB with embedded images)
├── api/
│   └── identify.py         ← Vercel serverless function (species ID via GPT-4o)
├── species-id/
│   ├── app.py              ← Flask local dev server (species ID)
│   └── static/
│       └── index.html      ← Species Identifier frontend (tabbed results UI)
├── assets/
│   └── images/             ← Source WebP images (originals, not used at runtime)
├── docs/                   ← Project documentation, changelogs, competitive analysis
├── requirements.txt        ← Python deps for Vercel serverless (openai, httpx)
├── vercel.json             ← Vercel routing: static site + serverless API + species-id page
├── README.md
├── LICENSE
├── CLAUDE.md
└── portfolio.md
```

## Development Commands
```powershell
# Pitch site — open directly in browser (no build step)
start index.html

# Species Identifier — local Flask dev server on port 5050
python species-id/app.py

# Or serve pitch site with any static server
npx serve .

# Deploy everything to Vercel
vercel --prod
```

## Key Patterns & Conventions
- **Bilingual system**: `data-lang="es|en"` attribute on `<body>`, `.lang-es` / `.lang-en` CSS classes hide/show content
- **Scroll reveals**: Elements with `.reveal`, `.reveal-left`, `.reveal-right`, `.reveal-scale` classes are observed by IntersectionObserver
- **Images**: All embedded as base64 data URIs in inline CSS `background-image` or `<img src>` attributes
- **Audio**: Web Audio API generates procedural forest ambience (wind noise, bird chirps, drone) — no audio files
- **5-act narrative**: Hero → Problem → Vision → Evidence → Ask
- **Species Identifier**: Camera/upload → GPT-4o vision → structured JSON (confidence %, taxonomy, ecology, geography, conservation, similar species) → tabbed UI with scan history in localStorage
- **Secret footer link**: Leaf icon (20% opacity, 50% hover) in pitch site footer links to `/species-id`

## URL Parameters
- `?mode=prez` — Auto-launches presentation mode (skips overlay, starts narration + auto-scroll)
- `?lang=es` / `?lang=en` — Sets language (overrides browser auto-detection)
- Combinable: `?mode=prez&lang=es` for a fully automatic Spanish presentation

### Outreach Links
- English presentation: `https://biojalisco-pitch.vercel.app/?mode=prez&lang=en`
- Spanish presentation: `https://biojalisco-pitch.vercel.app/?mode=prez&lang=es`
- Species Identifier: `https://biojalisco-pitch.vercel.app/species-id`

## Vercel Routing
- `/` → `index.html` (pitch site)
- `/species-id` → `species-id/static/index.html` (Species Identifier UI)
- `/api/identify` → `api/identify.py` (serverless GPT-4o vision endpoint)
- `/assets/*`, `/docs/*` → static file passthrough

## Current Focus
Both the pitch site and Species Identifier are deployed and functional. Species Identifier may evolve with additional data sources or features based on feedback.

## Known Issues
- Large single-file size (~1.8MB) due to embedded base64 images — acceptable for this use case
- `background-attachment: fixed` parallax doesn't work on iOS Safari (degrades gracefully)
- Ambient audio requires user interaction to start (browser autoplay policy)

## Environment Setup
- **Pitch site**: No environment variables needed
- **Species Identifier**: Requires `OPENAI_API_KEY` environment variable
  - Local: set in `.env` file or shell environment
  - Production: set in Vercel dashboard (Settings → Environment Variables)
