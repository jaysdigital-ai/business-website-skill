---
name: demo-business-website
description: Use when building a demo or sample business website (e.g. vet clinic, dental practice, HVAC, salon) to show prospects. Produces a premium, multi-page site with real photos, a unique design per demo, animated heroes and fictional details.
license: MIT
---

# Demo business website for prospects

The goal is a site a prospect (a clinic or small business owner) sees and immediately thinks "that's what my business should look like". It must feel premium and real, not templated or AI-generated.

## 1. Confirm direction before building

- Settle the industry, the fictional business name and the general look in one short exchange.
- **Before building any hero, show 2-3 quick hero directions** (small static mockups or a one-line description each) and let the user pick. Don't build a full animated hero on a guess. Elaborate 3D landscapes and cartoon 3D animals tend to get rejected and cost several rounds.

## 1b. A unique design for every demo, never a repeat

No two demos may share a look. Every demo gets its own design system, derived from the business, and it must differ clearly from every earlier demo.

1. **Check what already exists.** Look for a design log of past demos: a `design-log.md` file in the user's project or working folder, or a design-log entry in Claude's memory if memory is available. Also check any earlier demo sites the user has shared or that are in the folder. If there is no log yet, this is the first entry.
2. **Derive a brand personality from the business**, e.g. clinical and reassuring (dental, medical), warm and family (vet, childcare), rugged and dependable (trades), refined and luxe (salon, florist, law), fresh and outdoorsy (landscaping, pools), bold and energetic (gym, electrical). Let it drive every choice below.
3. **Choose one option on each design axis** and write it down as the fingerprint:
   - Layout system: two-column split / full-bleed photo with overlaid type / bento grid / asymmetric editorial magazine / centred single-column storytelling / sticky split scroll / horizontal-scroll sections
   - Type pairing: serif display + sans; grotesk-only; condensed display + mono; rounded geometric sans; high-contrast didone; slab serif. Match the client's logo where there is one.
   - Palette approach: dark luxe; light and airy; bold colour-blocked; earthy and natural; monochrome plus one neon accent; pastel. The dominant colour should come from the industry and the logo.
   - Shape language: soft rounded; sharp square edges; arches; pills and capsules; organic blobs; thin-ruled editorial lines
   - Navigation: sticky top bar; centred logo with split menu; transparent over the hero; side rail; full-screen overlay menu
   - Hero composition: split; full-bleed image; collage; framed arch or circle photo; oversized type with a small photo; video-like slideshow
   - Image treatment: full-bleed; framed with thick borders; duotone or colour-graded; cut-out subjects; rounded masks; grid mosaics
   - Section patterns: pick a different mix each time from ticker, stats, numbered steps, timeline, accordion FAQ, tabbed content, comparison table, testimonial carousel, masonry gallery, sticky side nav, quote wall
   - Buttons and links: pill, square, underline-arrow, outlined, icon-circle
   - Motion personality: calm and fluid; snappy and precise; playful and bouncy; cinematic slow reveals
4. **Compare with the log.** The new fingerprint must differ from every logged demo on at least 6 of the 10 axes, and must not reuse the same type pairing, palette or hero composition as any of them. If it's too close, change it before building.
5. Show the user the chosen direction in one or two lines (with the hero options from section 1) before building.

Everything in sections 5 and 6 is a toolkit of examples that worked, not a template. Pick the pieces that fit this design's personality, and vary them from earlier demos.

## 2. Fictional details only

- Invent the business name, people, email and address. Never use a real business or person.
- Phone numbers: use ranges reserved for fiction, e.g. Australia (02) 5550 xxxx, US/Canada 555-0100 to 555-0199, UK 020 7946 0xxx. Elsewhere, use an obviously fictional number.
- Email: use an `.example` domain.
- Label testimonials as samples ("Replace with the business's real Google reviews") and say in the footer that details are fictional.

## 3. Structure

- Multi-page: every menu item is its own page, and **every page is fully filled** with several real sections, not just the home page. For a clinic: Home, About, Services, Our team, New clients, Advice/blog, Contact, Book online.
- Content should match what real businesses in that industry have: services with what's included and prices from, team bios, FAQs, opening hours, emergency info, plans or memberships, articles, booking flow, map and directions.
- Fonts should match the client's logo and the type pairing chosen in section 1b. Never default to the pairing used in the previous demo.
- Build from a small Python generator (shared header, footer and helpers) so all pages stay consistent, plus one stylesheet and small JS files.

## 4. Images: real photos, not illustrations

- Use **real photos**. Illustrations and stock icons read as cheap.
- If the user supplies their own photos, use them. Map each image slot to the best-fitting photo with its own crop (background-position), crop team portraits from group shots, and swap any card whose subject no photo matches (e.g. retail, café, clinic) for an icon card rather than a mismatched photo.
- If an image-generation tool is connected, generate photos with one consistent style line in every prompt (natural light, the site's palette, editorial lifestyle photography, no text, no logos). **Estimate the cost first**: list the images needed, give the total credits, and confirm before generating.
- If there are no photos yet, use clearly labelled photo placeholders and tell the user which shots are needed.
- Save every image into the site's own `img/` folder at full resolution (high-quality jpg, no downscaling), so the site works offline and on any static host.
- Reuse photos across pages where they fit, rather than leaving gaps.
- Keep photos HD: no grain or noise overlay on photos. Don't put `will-change: transform` on scaled or parallax image layers, because Chrome rasterises them at low resolution and they look blurred. Check sharpness at 2x device scale before delivering.

## 5. Hero sections: animated, on-theme, different per page

- **The animation must look like the business.** Example for a vet clinic: a heartbeat/ECG line running across the bottom, a rotating headline (care for dogs / cats / rabbits / birds), a photo slideshow with slow zoom and crossfade, and small cards (heart rate with beating heart, a check-up list that ticks itself off, next available appointment with a live dot). Example for HVAC: a thermostat dial that counts to the set temperature, a technician ETA countdown and a service checklist.
- Every page gets **its own** hero. Ideas that worked: floating tilted photo stack that follows the cursor (About), morphing photo blob with orbiting service icons (Services), two staff portrait reels scrolling in opposite directions (Team), arch photo with a rotating stamp (New clients), drifting colour blobs with a shuffling article card deck (Advice), pulsing location rings with a bouncing pin (Contact), a booking card that plays itself (Book), a draggable before/after slider (Projects), a live zone-temperature board (Commercial).
- Avoid 3D WebGL landscapes and cartoon 3D animals. Technically impressive, but they clash with a photographic premium look.
- **Never cover the hero photo, especially faces, with floating cards.** Put animated cards in a row below or beside the photo; at most one small pill in a corner. Set each slide's crop so faces stay in frame on desktop and phone.

## 6. Animation on the rest of the page

A toolkit to pick from, matched to the motion personality chosen in section 1b. Don't use the same set on every demo.

- Headlines reveal word by word.
- Images open with a clip/zoom-out reveal, then drift slightly with scroll (parallax).
- Cards slide in with a stagger; step lines draw in; timeline years pop; stats count up.
- CTA and emergency panels scale in as they scroll into view.
- A scrolling service ticker band on a few pages.
- Desktop only: subtle 3D tilt with shine on cards, magnetic primary buttons.
- A thin reading-progress bar.
- Respect prefers-reduced-motion: show a calm, static version.
- Add a safety fallback so content never stays hidden if the animation script fails.

## 6b. Ambient 3D layer, themed to the business

Every demo gets an ambient 3D particle layer behind the content of each hero, each CTA panel and the footer. **The theme is picked from the business, never fixed to one effect.**

A ready-made engine ships with this skill: copy `assets/ambient.js` into the site, load it at the end of `<body>`, and set `<html data-ambient="...">` from the industry. If the attribute is left off, the script picks a theme from keywords in the page title and meta description. It attaches itself to elements with the classes `hero`, `cta-panel` and `footer`, and uses the dark palette on sections that also have `dark`, `deep`, `cta-panel` or `footer`.

| Theme | Industries | Particles and motion |
|---|---|---|
| hvac | air con, ducted, refrigeration | frost crystals, cool-air streaks, low mist, drifting sideways |
| heating | heaters, fireplaces, hot water | warm embers rising and fading |
| vet | vets, pet care, grooming | paw prints and small hearts floating up |
| dental | dentists, orthodontists | twinkling sparkles and bubbles |
| plumbing | plumbers, drains, pools | water droplets and bubbles rising |
| electrical | electricians, EV charging | amber sparks, fast streaks, small bolts |
| garden | landscaping, arborists, nurseries | tumbling leaves and a few petals |
| cleaning | cleaners, pressure washing | bubbles and sparkles |
| solar | solar, batteries, energy | warm light motes, rays, soft rings |
| cafe | cafés, bakeries, restaurants | steam wisps and warm dust |
| beauty | salons, spas, florists, weddings | petals and sparkles |
| legal | law, accounting, consulting | calm motes and a few outlined squares |
| generic | anything else | soft bokeh motes |

Required CSS so the layer sits behind content:

```css
canvas.frost{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:0}
.hero,.cta-panel,.footer{position:relative;overflow:hidden}
.hero>.container,.footer>.container,.cta-panel>:not(canvas){position:relative;z-index:1}
```

To add a new theme, add an entry to `THEMES` (particle mix, flow direction, flip speed, mist amount, dark and light rgb colours) and a keyword rule to `KEYWORDS`. New sprite shapes go in `S`. Before publishing, render the chosen theme on one dark and one light section and check that it stays subtle behind the text.

## 7. Test before delivering

- Render every page in a headless browser at desktop and phone widths and look at the screenshots.
- Scroll through each page and check that every revealed element ends up visible. This once caught a CSS specificity bug that hid all team photos and article images.
- Check for console errors and for horizontal overflow on phones.

## 8. Deliver

- Deliver the site as a folder (pages, `assets/`, `img/`) and a zip, ready for Cloudflare Pages, Netlify or any static host. If the environment can publish hosted pages, publish it there too and give the link.
- Reply briefly: what changed, anything the user should check on a real device, and one natural next step.
- **Log the design.** Add the demo's fingerprint (business, date, and the choice on each section 1b axis) to the design log: `design-log.md` in the user's project folder, and Claude's memory too if available. Update the entry if the design changes in later rounds.
