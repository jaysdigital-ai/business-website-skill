# Demo Business Website — a Claude plugin

A studio team of seven AI agents that builds premium, multi-page demo websites for small businesses: the kind of site you can show a prospect so they think "that's what my business should look like".

Made for web designers and agencies who pitch websites to local businesses (clinics, trades, salons, cafés and more).

## The team

| Agent | Role |
|---|---|
| **UI/UX Designer** | Turns the business into a unique design system, sitemap and hero concepts, and checks the design log so it never repeats an earlier demo |
| **Copywriter** | Writes every page in the brand's voice, with realistic but fictional details and no AI-sounding filler |
| **SEO Specialist** | Plans titles, meta descriptions, headings, local-business schema, alt text, sitemap.xml and robots.txt, then audits the built site |
| **Graphic Artist** | Designs the logo, icons and social image, and prepares every photo at full resolution with the right crop |
| **Web Developer** | Builds the fast, accessible, responsive multi-page site from the briefs |
| **Animator** | Creates a different animated hero for every page, the scroll motion and the industry-themed 3D layer |
| **Website Tester** | Independently renders every page on desktop and phone, runs the QA script and sends issues back until the site passes |

Each agent hands off a written brief to the next, and **no site is delivered until the tester passes it**. That hand-off and QA loop is what makes the results consistent. In environments without agents, Claude runs the same steps itself, using each agent's file as the checklist.

## What it does

- **Multi-page sites, fully filled.** Every menu item is its own page with real sections: services and prices, team, FAQs, opening hours, booking flow, contact and more.
- **A unique design every time.** It derives a brand personality from the business, picks a look across 10 design choices (layout, fonts, colours, shapes, navigation, hero, image style, sections, buttons, motion) and checks a design log so no two demos look the same.
- **Real photos, kept sharp.** Uses your photos (or generated ones, if you have an image tool connected), cropped to fit each spot and published at full resolution.
- **Animated heroes that fit the business.** A different hero on every page, with animated cards that never cover faces in the photos.
- **Ambient 3D effect matched to the industry.** Frost for air conditioning, paw prints for vets, sparkles for dental, water drops for plumbing, leaves for landscaping and 8 more themes. A ready-made engine (`ambient.js`) is included.
- **Safe demo details.** Fictional business names, people, emails and reserved fictional phone numbers, with testimonials labelled as samples.
- **Local SEO built in.** Page titles, meta descriptions, LocalBusiness schema, FAQ schema, alt text, sitemap.xml and robots.txt.
- **Tested before delivery.** A bundled QA script (`qa_check.py`) renders every page at desktop and phone sizes and reports hidden content, overflow, script errors, broken links, missing alt text, low-resolution images and SEO problems, with screenshots.

## Install

### Claude Code

```
/plugin install demo-business-website --marketplace jaysdigital-ai/business-website-skill
```

On older versions of Claude Code, add the marketplace first:

```
/plugin marketplace add jaysdigital-ai/business-website-skill
/plugin install demo-business-website@digital-agila
```

### Claude apps (claude.ai and the desktop app)

1. Download **[`demo-business-website.plugin`](https://github.com/jaysdigital-ai/business-website-skill/raw/main/dist/demo-business-website.plugin)** (it's in the `dist` folder of this repo).
2. Upload it in Claude's plugin settings, or drop it into a chat and accept it from the preview card. (Plugin uploads must be available on your plan or enabled by your organisation.)

### Just the skill

If your Claude only supports skills, zip the `skills/demo-business-website` folder (so the zip contains `demo-business-website/SKILL.md`) and upload it under **Settings → Capabilities → Skills**.

## Use it

Just ask, for example:

> Build a demo website for a dental clinic in Melbourne.

> Make a sample site for a landscaping business. Use these photos.

Claude will confirm the business, the look and the hero direction with you, then build the site, test it and hand you the files (and a link, where your Claude environment can publish pages).

## What's inside

```
.claude-plugin/
├── plugin.json            # plugin manifest
└── marketplace.json       # lets Claude Code install it from this repo
agents/
├── ui-ux-designer.md
├── copywriter.md
├── seo-specialist.md
├── graphic-artist.md
├── web-developer.md
├── animator.md
└── website-tester.md
skills/
└── demo-business-website/
    ├── SKILL.md           # the workflow and shared rules
    ├── assets/
    │   └── ambient.js     # themed 3D particle layer (no dependencies)
    └── scripts/
        └── qa_check.py    # automated QA (needs Playwright)
```

The QA script needs Playwright: `pip install playwright && python -m playwright install chromium`.

## Notes

- The ambient effect turns itself off for visitors who prefer reduced motion and pauses when off screen.
- All business details in generated demos are fictional. Replace them, and the sample testimonials, before using a design for a real client.

## License

MIT, see [LICENSE](LICENSE). Made by [The Digital Agila](https://thedigitalagila.com).
