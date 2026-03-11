# HRHelp.nl — Services Pages Knowledge Base

> Comprehensive reference for the inner service pages (`src/pages/solutions/[slug].astro`).
> Last updated: 2026-02-28

---

## Architecture

### Single Dynamic Route
All 4 services are rendered by **one file**: `src/pages/solutions/[slug].astro`.
- Uses `getStaticPaths()` returning 4 slugs: `hr-settlers`, `hr-teams`, `hr-reset`, `hr-sos`
- All service content lives in a `serviceData` object at the top of the file (lines 31–340)
- No external CMS or content collection yet — everything is hard-coded inline

### Page Sections (in order)
| # | Section | CSS Class Prefix | Description |
|---|---------|-----------------|-------------|
| 1 | **Hero** | `.sv-hero` | Premium split layout — text left, photo + floating cards right |
| 2 | **Story** | `.sv-story` | Insight quote card + split (text + photo with overlay card) |
| 3 | **What's Included** | `.sv-included` | 6-card grid of services/features with inline SVG icons |
| 4 | **Challenge vs. Approach** | `.sv-versus` | Two-column comparison (Friction vs. Solution) |
| 5 | **How It Works** | `.sv-vtimeline` | Animated vertical timeline with 4 steps + illustrations |
| 6 | **Pricing** | `.sv-pricing` | 3-tier pricing cards |
| 7 | **Ideal For** | `.sv-ideal` | Grid of target customer segments |
| 8 | **Testimonial** | `.sv-testimonial` | Pull quote with attribution |
| 9 | **FAQ** | `.sv-faq` | Accordion-style Q&A |
| 10 | **CTA** | `.sv-cta` | Final call-to-action with photo |
| 11 | **Related Services** | `.sv-related` | Links to other services |

### Data Shape (per service)
Each service in `serviceData` has these keys:
```
name, tagline, hero, heroImage, heroPhoto, illustration
heroCards: { tl: {icon, label, value}, br: {icon, label, value} }
premiseHeading, premiseBody: string[]
included: { icon, title, desc }[]
friction: { title, description, items[], image }
settlement: { title, description, items[], image }
process: { step, title, desc, week, image }[]
testimonial: { quote, name, role, company }
pricingTiers: { name, desc, price, unit }[]
ideal: string[]
faqs: { q, a }[]
relatedServices: string[]
sections: { included, versus, process, pricing, ideal, faq } — eyebrow/heading/desc per section
photos: { story, strip, cta }
```

---

## Services Overview

| Slug | Name | Tagline | Timeline Label |
|------|------|---------|---------------|
| `hr-settlers` | HR Settlers | Enter the Dutch market with confidence | Week-based (1 → Ongoing) |
| `hr-teams` | HR Teams | Your outsourced HR department | Day/Week-based (Day 1 → Ongoing) |
| `hr-reset` | HR Reset | Modernize your HR foundations | Week-based (1–2 → 9–12) |
| `hr-sos` | HR S.O.S. | Emergency HR intervention | Day-based (Day 1 → 1–8 weeks) |

---

## Design System & Styling

### Color Palette (CSS Variables)
- `--navy`: Dark blue — headings, primary text
- `--orange`: `#F47920` — accents, CTAs, badges, timeline markers
- `--cream`: Light warm background for cards
- `--white`: Section backgrounds
- `--gray-500`, `--gray-600`: Body text

### Key Design Decisions

#### Hero Section
- **Background**: Warm cream gradient (`#fdf8f3` → `#f6f2ed` → white) — NOT plain white
- **Purpose**: Creates visual separation from the Story section below
- **Bottom border**: `1px solid rgba(0,0,0,0.05)` for subtle containment
- **Mesh gradient**: Animated radial gradients with a 20s drift animation for depth
- **Floating cards**: Two glassmorphic cards (top-left, bottom-right) with service-specific stats
- **Status pill**: "Expert Advisor Online" with a pulsing green dot

#### Story Section
- **Layout**: Quote card + text on left column, photo on right (NOT quote full-width above the split)
- **Insight card**: Compact (`padding: 1.75rem 2rem`), inside the left column, orange accent bar on left
- **Lead paragraph**: First body paragraph has bolder weight (500) and navy color
- **CTA link**: "Speak with an expert →" orange link with sliding chevron on hover
- **Photo frame**: Decorative offset border (`rgba(244,121,32,0.2)`) behind the image
- **Overlay card**: Glassmorphic "Trusted by 50+ Companies" floating bottom-left of photo

#### Timeline Section (How It Works)
- **Style**: Vertical timeline with numbered circle markers (01–04)
- **Animations**: Scroll-triggered staggered reveals, animated progress line, hover lift
- **Interactive**: Click-to-select steps with highlight state
- **Thumbnails**: Flat vector illustrations in **oval frames** (`border-radius: 50%`)
  - 80×80px, subtle orange border ring, cream background
  - Positioned right-aligned inside each step card
  - Hidden on mobile (`display: none` below 768px)
  - Hover: `scale(1.08)` with orange-tinted shadow

### Responsive Breakpoints
- `@media (max-width: 768px)`:
  - Hero: Stacks vertically, floating cards repositioned
  - Story: Single column, image above text (`order: -1`)
  - Timeline: Single column, markers shrink to 38px, thumbnails hidden
  - All grids collapse to `1fr`

---

## Images & Assets

### Image Locations
All images are in `public/images/`:

| Purpose | Path Pattern | Format | Source |
|---------|-------------|--------|--------|
| Hero photos | `/images/hero/hero-{slug}.png` | PNG | AI-generated |
| Story section | `/images/sections/story-{slug}.png` | PNG | AI-generated |
| Strip section | `/images/sections/strip-{slug}.png` | PNG | AI-generated |
| CTA section | `/images/sections/cta-{slug}.png` | PNG | AI-generated |
| Timeline illustrations | `/images/sections/illus-{slug}-{01-04}.png` | PNG | AI-generated |

### Timeline Illustrations (16 total)
Flat vector style, navy blue + orange palette, white background, ~400KB each.

**HR Settlers:**
1. `illus-settlers-01.png` — Consultant analyzing documents with magnifying glass
2. `illus-settlers-02.png` — Building strategic framework with blocks and gears
3. `illus-settlers-03.png` — Implementation at laptop with checklist
4. `illus-settlers-04.png` — Handover — two people exchanging folder

**HR Teams:**
1. `illus-teams-01.png` — Discovery call with speech bubbles
2. `illus-teams-02.png` — Talent matching with puzzle pieces
3. `illus-teams-03.png` — Compliance audit with clipboard and shield
4. `illus-teams-04.png` — Ongoing partnership handshake with calendar

**HR Reset:**
1. `illus-reset-01.png` — Comprehensive audit with magnifying glass and files
2. `illus-reset-02.png` — Risk report presentation with warning triangle
3. `illus-reset-03.png` — Modernization sprint — running with wrench and documents
4. `illus-reset-04.png` — Training session at whiteboard with graduation cap

**HR S.O.S.:**
1. `illus-sos-01.png` — Emergency call with ringing phone and alert
2. `illus-sos-02.png` — Situation assessment with magnifying glass and scales
3. `illus-sos-03.png` — Action plan flowchart on whiteboard
4. `illus-sos-04.png` — Successful resolution celebration with trophy

### Friction/Settlement Section Images
Still using Unsplash URLs (external). These could be replaced with local AI images in the future.

---

## Icon System
The `iconSvg` map at the top of the file provides inline SVG icons for the "What's Included" cards. Available icons:
`domain`, `savings`, `description`, `flight_takeoff`, `policy`, `support_agent`, `person`, `trending_up`, `gavel`, `groups`

Material Symbols Outlined font is loaded globally for hero floating cards.

---

## Animations & Interactivity

### Scroll-Triggered Animations
- `data-animate="fade-up"` / `"fade-left"` / `"fade-right"` attributes
- Observed by `IntersectionObserver` (threshold: 0.15)
- `data-delay` attribute for staggered entries (in ms)
- Elements start with `opacity: 0; transform: translateY(30px)` and animate in

### Timeline-Specific Animations
- **Progress line**: SVG-based, animates `strokeDashoffset` on scroll
- **Step reveals**: Each step fades/slides in with staggered delay
- **Active step**: Click sets `.sv-vtimeline-step.active` — scales up marker, changes colors
- **Hover**: Each step lifts with `translateY(-4px)` and brightens border

### Hero Floating Cards
- `data-float` / `data-float-reverse` attributes trigger a subtle float animation
- `@keyframes float-gentle`: 6s ease-in-out loop, ±8px Y translation

---

## Deployment

### Stack
- **Framework**: Astro v5.17.x (static output)
- **Hosting**: Cloudflare Pages
- **Project name**: `hrhelp-website`

### Deploy Command
```bash
cd hr/hrhelp-website
npx astro build
npx wrangler pages deploy dist --project-name=hrhelp-website
```

### Build Stats
- 18 pages total (homepage, about, contact, resources, 4 solutions, 8 industries, solutions index, industries index)
- Build time: ~1.2s
- Zero build errors in current state

---

## Common Pitfalls & Learnings

### Image Integration
1. **Don't use full-width images in timeline steps** — the user found them too heavy. Use small thumbnails (80–90px) positioned to the right of text.
2. **Always copy generated images to `public/`** — Astro serves from `public/`, not from artifact directories. Verify files exist with `ls` before browser testing.
3. **Illustrations > Photos for timeline** — flat vector illustrations in the brand color palette feel lighter and more professional than photographs at small sizes.
4. **Oval borders for illustrations** — `border-radius: 50%` with a subtle `2.5px solid rgba(244,121,32,0.15)` border creates a polished look.

### Layout & Visual Hierarchy
5. **Hero needs visual separation** — if hero and story both use `background: white`, they merge visually. Use a cream gradient and/or bottom border to create "containment".
6. **Insight quote belongs IN the left column** — not as a full-width element above the split. This keeps both text blocks adjacent to the image and avoids the section looking too tall.
7. **Keep the insight card compact** — `padding: 1.75rem 2rem` and `clamp(1.15rem, 2.2vw, 1.5rem)` font size. Not a big hero-sized quote.

### Development Process
8. **Always restart the dev server after copying new static files** — Astro's dev server may not detect new files in `public/` without a restart.
9. **Browser verification is essential** — CSS changes that look correct in code can render unexpectedly. Always take screenshots.
10. **Build before deploy** — `npx astro build` catches template errors that the dev server may not surface.

### CSS Organization
11. All service page styles are scoped within `[slug].astro` (no external CSS file) — this keeps the ~1000 lines of section-specific CSS co-located with their templates.
12. Media queries are consolidated at the bottom of the `<style>` block, not scattered.
13. CSS variable usage is consistent — always reference `--navy`, `--orange`, etc. rather than hex values.

---

## File Quick Reference

| File | Purpose | Lines |
|------|---------|-------|
| `src/pages/solutions/[slug].astro` | All service pages (data + template + styles) | ~1884 |
| `src/pages/solutions/index.astro` | Solutions listing page | — |
| `src/components/Layout.astro` | Global layout wrapper | — |
| `src/components/Header.astro` | Site navigation | — |
| `public/images/sections/` | Section-specific images and illustrations | 16 illus + 12 section photos |
| `public/images/hero/` | Hero section photos | 4 files |

---

## Future Considerations
- **WordPress CMS Integration**: The `serviceData` object is ready to be replaced with CMS-fetched data. The data shape is well-defined.
- **Image Optimization**: Illustrations are ~400KB PNGs. Converting to WebP and resizing to actual display dimensions (80×80 for thumbnails) would improve load times.
- **Friction/Settlement Unsplash images**: Should be replaced with local AI-generated images for consistency and to avoid external dependencies.
- **Photo strip section**: Was removed from all service pages. The CSS and related photos (`strip-*.png`) still exist but are unused.
