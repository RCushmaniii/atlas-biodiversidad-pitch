# BioJalisco — Biodiversity Atlas Pitch Site

![HTML5](https://img.shields.io/badge/HTML5-Single_File-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Custom_Properties-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JS-Vanilla-F7DF1E?logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-Serverless-3776AB?logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/GPT--4o-Vision-412991?logo=openai&logoColor=white)
![Vercel](https://img.shields.io/badge/Deployed-Vercel-000?logo=vercel&logoColor=white)
![Bilingual](https://img.shields.io/badge/Bilingual-ES%20%7C%20EN-c8a45c)

> Cinematic scrollytelling site pitching BioJalisco — a citizen-science biodiversity platform for western Mexico — plus an AI-powered Species Identifier tool.

## Overview

BioJalisco is a proposed citizen-science biodiversity monitoring platform for western Mexico's forests, mountains, and wetlands. This repo contains two things:

1. **The Pitch Site** — A narrative scrollytelling experience designed to communicate the BioJalisco vision to stakeholders, academic partners, and potential collaborators. Built as a single self-contained HTML file with scroll-triggered animations, parallax photography, procedural ambient forest audio, and full bilingual (ES/EN) support. Every image is embedded as a base64 data URI, making the site fully portable.

2. **The Species Identifier** — An AI-powered species and breed identification tool using OpenAI's GPT-4o vision API. Upload or photograph any organism (wildlife, insects, plants, domestic animals) and get structured results: confidence percentage, full taxonomy, ecology, geographic range, conservation status, and similar species. Deployed as a Vercel serverless function.

The site presents the work of Dra. Verónica Rosas-Espinoza (Science Director) and Robert Cushman (Technology & Product Director) — combining deep ecological expertise with modern technology to build something neither could create alone.

## The Challenge

Conservation researchers in Jalisco face a fundamental asymmetry: deep scientific expertise covering only ~5% of the state's 80,000+ km² territory. Traditional ecology methods — small teams, limited funding, years per survey — can't keep pace with biodiversity loss. The BioJalisco vision proposes closing that gap through citizen science and technology, but the idea needed a compelling presentation to win over partners.

The pitch site had to work for two audiences simultaneously: Spanish-speaking Mexican academics and English-speaking international partners. It needed to persuade, not just inform — moving people from awareness to action through narrative rather than bullet points.

## The Solution

A scrollytelling experience structured as a 5-act narrative:

1. **The Hook** — A provocative question over a dramatic Jalisco landscape with floating firefly particles
2. **The Problem** — Animated counters and a comparison grid making the data crisis tangible
3. **The Vision** — BioJalisco introduced as the answer, with parallax photography and a 4-step "how it works"
4. **The Evidence** — Roadmap timeline, iNaturalist precedent data, book trilogy, and team credentials
5. **The Ask** — Emotional close with a direct call to action

All content exists in both languages in the DOM. A `data-lang` attribute on the body element toggles visibility via CSS — instant switching, zero reload.

## Technical Highlights

- **Self-contained single file:** All 9 images embedded as base64 data URIs. 16.8MB PNG originals optimized to 1.3MB WebP (92% reduction), resulting in a 1.8MB HTML file that works offline
- **Procedural audio:** Web Audio API generates a three-layer forest soundscape in real-time — filtered noise for wind, frequency-modulated oscillators for bird chirps, sine drone for atmospheric depth. No audio files.
- **Scroll choreography:** Intersection Observer API drives multiple reveal classes (translateY, translateX, scale) with staggered CSS transition delays — cinematic feel without animation libraries
- **CSS-only parallax:** `background-attachment: fixed` creates depth on the vision section without JavaScript scroll listeners
- **Bilingual architecture:** `.lang-es` / `.lang-en` CSS class system with `data-lang` body attribute enables instant language toggle across all content
- **AI Species Identification:** GPT-4o vision API returns structured JSON with confidence percentage, full taxonomy (Kingdom to Species), ecology (habitat, diet, size, lifespan), geographic range, IUCN conservation status, and similar species. Supports wildlife, insects, plants, and domestic animals (breed identification). Results displayed in a tabbed UI with scan history persisted in localStorage.

## Live Demo

**Pitch Site:** [biojalisco-pitch.vercel.app](https://biojalisco-pitch.vercel.app)
**Species Identifier:** [biojalisco-pitch.vercel.app/species-id](https://biojalisco-pitch.vercel.app/species-id)

### Direct Presentation Links

Share these for a hands-free, auto-narrated experience:

- **English:** [biojalisco-pitch.vercel.app/?mode=prez&lang=en](https://biojalisco-pitch.vercel.app/?mode=prez&lang=en)
- **Spanish:** [biojalisco-pitch.vercel.app/?mode=prez&lang=es](https://biojalisco-pitch.vercel.app/?mode=prez&lang=es)

### URL Parameters

| Parameter | Values | Effect |
|-----------|--------|--------|
| `mode` | `prez` | Skips overlay, auto-launches narrated presentation |
| `lang` | `es`, `en` | Sets language (overrides browser detection) |

### Try These Interactions

- Toggle the **ES/EN** language switch (top right) — all content swaps instantly
- Click the **audio button** (top left) — procedural forest ambience fades in
- Scroll slowly through each act — watch the counters animate and elements reveal on scroll
- Find the **secret leaf icon** in the footer — it links to the Species Identifier
- Upload a photo in the Species Identifier — explore the tabbed results (Taxonomy, Ecology, Range, Conservation)

## Project Structure

```
biojalisco-pitch/
├── index.html              # The pitch site (single file, ~1.8MB with embedded images)
├── api/
│   └── identify.py         # Vercel serverless function (species ID via GPT-4o)
├── species-id/
│   ├── app.py              # Flask local dev server (species ID)
│   └── static/
│       └── index.html      # Species Identifier frontend (tabbed results UI)
├── assets/
│   └── images/             # Source WebP images (originals)
├── docs/                   # Project documentation, changelogs, competitive analysis
├── requirements.txt        # Python deps for Vercel serverless (openai, httpx)
├── vercel.json             # Vercel routing: static site + serverless API + species-id
├── CLAUDE.md               # AI assistant project context
├── portfolio.md            # CushLabs portfolio entry
├── LICENSE
└── README.md
```

## Getting Started

### Prerequisites

- Any modern web browser
- Optional: Node.js >= 18 (only if you want a local dev server)
- Optional: Python 3.9+ (only for local Species Identifier development)

### Installation

```powershell
git clone https://github.com/RCushmaniii/biojalisco-pitch.git
cd biojalisco-pitch
```

**Pitch site** — Open `index.html` directly in a browser, or serve it:

```powershell
npx serve .
```

**Species Identifier** — Run the Flask dev server:

```powershell
# Set your OpenAI API key
set OPENAI_API_KEY=sk-...

# Run the local server (port 5050)
python species-id/app.py
```

### Deployment

```powershell
# Deploy to Vercel (CLI)
vercel --prod

# Or connect the GitHub repo in the Vercel dashboard — auto-deploys on push
```

The pitch site requires no environment variables. The Species Identifier requires `OPENAI_API_KEY` set in the Vercel dashboard (Settings > Environment Variables).

## Results

| Metric | Value |
|--------|-------|
| Pitch site file size | ~1.8MB (self-contained) |
| Image optimization | 92% reduction (16.8MB → 1.3MB) |
| External dependencies | 0 for pitch site (fonts loaded async) |
| Build step | None |
| Languages supported | 2 (Spanish, English) |
| Species ID confidence | 0-100% with visual gauge |
| Species ID data | Taxonomy, ecology, geography, conservation, similar species |
| Time to deploy | Instant (static + serverless) |

The site serves as both a stakeholder pitch and a demonstration of what focused web development can achieve. The Species Identifier showcases AI integration as a preview of BioJalisco's citizen-science capabilities.

## Team

- **Verónica Rosas-Espinoza** — Science Director, CUCBA/Universidad de Guadalajara
- **Robert Cushman** — Technology & Product Director, CushLabs AI Services

## Contact

**Robert Cushman**
Business Solution Architect & Full-Stack Developer
Guadalajara, Mexico

info@cushlabs.ai
[GitHub](https://github.com/RCushmaniii) | [LinkedIn](https://linkedin.com/in/robertcushman) | [Portfolio](https://cushlabs.ai)

## License

Proprietary — CushLabs AI Services. See LICENSE file for details.

---

*Last Updated: 2026-03-06*
