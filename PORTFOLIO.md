---
# =============================================================================
# PORTFOLIO.md — BioJalisco Pitch Site
# =============================================================================
portfolio_enabled: true
portfolio_priority: 4
portfolio_featured: true
portfolio_last_reviewed: "2026-03-06"

title: "BioJalisco — Biodiversity Atlas Pitch Site + Species Identifier"
tagline: "Cinematic scrollytelling pitch site with AI-powered species identification for western Mexico's biodiversity platform"
slug: "biojalisco-pitch"

category: "Client Work"
target_audience: "Conservation stakeholders, academic partners, and potential collaborators in Mexico"
tags:
  - "scrollytelling"
  - "biodiversity"
  - "citizen-science"
  - "bilingual"
  - "conservation"
  - "jalisco"
  - "mexico"
  - "landing-page"
  - "ai-vision"
  - "species-identification"
  - "openai"
  - "serverless"

thumbnail: "assets/images/portfolio/scrollytelling_pitch_thumb.png"
hero_images:
  - "assets/images/portfolio/scrollytelling_pitch_01.png"
  - "assets/images/portfolio/scrollytelling_pitch_02.png"
  - "assets/images/portfolio/scrollytelling_pitch_03.png"
  - "assets/images/portfolio/scrollytelling_pitch_04.png"
  - "assets/images/portfolio/scrollytelling_pitch_05.png"
  - "assets/images/portfolio/scrollytelling_pitch_06.png"
  - "assets/images/portfolio/scrollytelling_pitch_07.png"
  - "assets/images/portfolio/scrollytelling_pitch_08.png"
  - "assets/images/portfolio/scrollytelling_pitch_09.png"
  - "assets/images/portfolio/scrollytelling_pitch_10.png"
demo_video_url: "assets/video/scrollytelling-pitch.mp4"
demo_video_poster: "assets/images/portfolio/scrollytelling-pitch-poster.jpg"

live_url: "https://biojalisco-pitch.vercel.app"
demo_url: "https://biojalisco-pitch.vercel.app"
case_study_url: ""

problem_solved: |
  Conservation researchers in western Mexico face an asymmetry: deep scientific
  expertise but limited reach. Their work covers a fraction of Jalisco's 80,000+ km²
  territory. BioJalisco proposes closing that gap through citizen science and technology,
  but the vision needed a compelling presentation to win stakeholders and partners.

key_outcomes:
  - "Self-contained single-file HTML site with 9 embedded images (~1.8MB total)"
  - "Bilingual ES/EN with instant language switching"
  - "Cinematic 5-act narrative arc designed for stakeholder persuasion"
  - "Full auto-play presentation mode with segmented MP3 narration, rain-intro crossfades, and auto-scroll"
  - "Mobile-first species carousel with scroll-snap, dot indicators, and audio-synced auto-cycle"
  - "AI Species Identifier with GPT-4o vision — confidence %, full taxonomy, ecology, geography, conservation status, similar species"
  - "Tabbed results UI with scan history persisted in localStorage"
  - "Vercel serverless Python function for production API"
  - "Deployed on Vercel with zero build step"

tech_stack:
  - "HTML5"
  - "CSS3 (custom properties, grid, flexbox, scroll-snap)"
  - "Vanilla JavaScript"
  - "Python (Flask + Vercel serverless)"
  - "OpenAI GPT-4o Vision API"
  - "Intersection Observer API"
  - "Web Audio API (procedural ambient + MP3 narration)"
  - "Google Fonts"
  - "Vercel (static + serverless)"
  - "Base64 image embedding"

complexity: "Production"
---

## Overview

BioJalisco is a proposed citizen-science biodiversity monitoring platform for western Mexico. Before building the platform, the project needed a persuasion artifact — a site that communicates the vision with enough emotional and intellectual weight to win over academic partners, conservation organizations, and potential funders.

This scrollytelling site is that artifact. Built as a single self-contained HTML file, it uses a cinematic 5-act story arc (Hook → Problem → Vision → Evidence → Ask) with scroll-triggered animations, parallax photography, ambient forest audio, and bilingual content to make the case for BioJalisco.

Every image is embedded as a base64 data URI, making the site fully portable — it works offline, deploys anywhere, and has zero external dependencies beyond Google Fonts.

## The Challenge

- **The reach problem:** Verónica Rosas-Espinoza has deep expertise in Jalisco's biodiversity, but traditional ecology covers only ~5% of the territory systematically. The pitch needed to make this gap visceral, not abstract.
- **Dual audience:** The site must work for Spanish-speaking Mexican academics and English-speaking international partners — not as separate pages, but as a seamless bilingual experience.
- **Persuasion, not information:** This isn't a documentation site. It's a narrative designed to move people from awareness to action. Every section must earn its scroll.
- **Zero infrastructure:** The site needed to deploy instantly with no build step, no CMS, no backend — just drop a file on Vercel.

## The Solution

**Cinematic narrative structure:**
A 5-act story arc modeled on screenwriting principles. The hero section poses a provocative question, the problem section makes the data crisis tangible with animated counters, the vision section introduces BioJalisco as the answer, the evidence section builds credibility with a roadmap and proof points (iNaturalist precedent, book trilogy, team credentials), and the closing ask creates urgency.

**Bilingual architecture:**
A `data-lang` attribute on the body element combined with `.lang-es` / `.lang-en` CSS classes enables instant language switching with zero page reload. All content exists in both languages in the DOM — CSS toggles visibility.

**Self-contained deployment:**
All 9 images converted from PNG to WebP (88-95% size reduction), then embedded as base64 data URIs. The entire site is a single 1.8MB HTML file with no external asset dependencies.

**Procedural audio:**
The ambient forest soundscape is generated in real-time using Web Audio API — layered noise filters for wind, oscillators for bird chirps, and a low drone for depth. No audio files needed.

## Technical Highlights

- **Base64 image pipeline:** Python/Pillow batch conversion from PNG to optimized WebP, then base64 encoding — reduced total image payload from 16.8MB to 1.3MB (92% reduction)
- **Intersection Observer scroll system:** Multiple reveal classes (translate-Y, translate-X, scale) with staggered delays create a choreographed scroll experience without a single animation library
- **Web Audio API synthesis:** Three-layer procedural soundscape (filtered noise for wind, frequency-modulated oscillators for bird chirps, sine drone for depth) with fade-in/fade-out on toggle
- **CSS-only parallax:** `background-attachment: fixed` on the vision section creates depth without JavaScript scroll listeners
- **Animated counters:** Eased counter animations triggered by IntersectionObserver with cubic easing for natural deceleration
- **AI Species Identification:** GPT-4o vision API with structured JSON output — confidence percentage, full taxonomy (Kingdom→Species), ecology (habitat, diet, size, lifespan, behavior), geographic range with Jalisco/Mexico/invasive badges, IUCN conservation status, and similar species comparison. Handles wildlife, insects, plants, and domestic animals (breed identification with temperament and origin history).
- **Tabbed results UI:** Six-tab interface (Overview, Taxonomy, Ecology, Range, Conservation, Similar) with circular confidence gauge, taxonomy tree visualization, and scan history persisted in localStorage
- **Serverless architecture:** Same Python codebase runs as Flask dev server locally and as a Vercel serverless function in production

## Results

**For the Stakeholder Audience:**

- Complete narrative pitch accessible in both Spanish and English
- Credibility elements (PhD photo, book trilogy, fieldwork photography) embedded directly
- Single URL to share — no login, no app install, works on any device
- Interactive Species Identifier demonstrates real AI capability — stakeholders can try it immediately

**Technical Demonstration:**

- Proves that a high-impact persuasion site doesn't need React, a build system, or a CMS
- Shows restraint in technology choices — vanilla JS for a project that genuinely doesn't need frameworks
- AI integration via serverless functions keeps the architecture simple while delivering real utility
- Image optimization pipeline that could be reused across CushLabs projects
