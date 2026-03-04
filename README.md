# BioJalisco

**Documenting and protecting the biodiversity of western Mexico — one observation at a time.**

A bilingual (ES/EN) scrollytelling website presenting the vision for BioJalisco — a citizen-science biodiversity monitoring platform for western Mexico's forests, mountains, and wetlands.

## What This Is

A narrative persuasion experience built as a single-page cinematic scroll, designed to communicate the BioJalisco vision to stakeholders, partners, and collaborators. Features scroll-triggered animations, ambient forest audio, animated counters, and a 5-act story arc.

## Tech

- Single-file HTML/CSS/JS (no build step)
- Google Fonts (Playfair Display, Source Sans 3, Cormorant Garamond)
- Intersection Observer API for scroll reveals
- Web Audio API for ambient soundscape
- Deployed on Vercel

## Live Site

[biojalisco.vercel.app](https://biojalisco.vercel.app) *(update after deploy)*

## Adding Photos

Replace placeholder backgrounds in `index.html` — search for `<!-- REPLACE -->` comments. Recommended image sizes:

| Slot | Recommended Size | Notes |
|------|-----------------|-------|
| Hero background | 1920x1080+ | Landscape, dramatic lighting |
| Vision parallax | 1920x1080+ | Jalisco landscape, works with fixed attachment |
| Species cards | 800x1067 (3:4) | Portrait orientation, one per species |
| Closing section | 1920x1080+ | Emotional, warm tone |

## Team

- **Veronica Rosas-Espinoza** — Science Director
- **Robert Cushman** — Technology & Product Director

## Contact

Robert Cushman / [CushLabs.ai](https://cushlabs.ai) / info@cushlabs.ai
