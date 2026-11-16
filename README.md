# Demo Business Website — a Claude plugin

A Claude plugin that builds premium, multi-page demo websites for small businesses: the kind of site you can show a prospect so they think "that's what my business should look like".

Made for web designers and agencies who pitch websites to local businesses (clinics, trades, salons, cafés and more).

## What it does

- **Multi-page sites, fully filled.** Every menu item is its own page with real sections: services and prices, team, FAQs, opening hours, booking flow, contact and more.
- **A unique design every time.** It derives a brand personality from the business, picks a look across 10 design choices (layout, fonts, colours, shapes, navigation, hero, image style, sections, buttons, motion) and checks a design log so no two demos look the same.
- **Real photos, kept sharp.** Uses your photos (or generated ones, if you have an image tool connected), cropped to fit each spot and published at full resolution.
- **Animated heroes that fit the business.** A different hero on every page, with animated cards that never cover faces in the photos.
- **Ambient 3D effect matched to the industry.** Frost for air conditioning, paw prints for vets, sparkles for dental, water drops for plumbing, leaves for landscaping and 8 more themes. A ready-made engine (`ambient.js`) is included.
- **Safe demo details.** Fictional business names, people, emails and reserved fictional phone numbers, with testimonials labelled as samples.
- **Tested before delivery.** Every page is checked at desktop and phone sizes for hidden content, overflow and errors.

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

1. Download **`demo-business-website.plugin`** from the [latest release](https://github.com/jaysdigital-ai/business-website-skill/releases/latest).
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
skills/
└── demo-business-website/
    ├── SKILL.md           # the instructions Claude follows
    └── assets/
        └── ambient.js     # themed 3D particle layer (no dependencies)
```

## Notes

- The ambient effect turns itself off for visitors who prefer reduced motion and pauses when off screen.
- All business details in generated demos are fictional. Replace them, and the sample testimonials, before using a design for a real client.

## License

MIT, see [LICENSE](LICENSE). Made by [The Digital Agila](https://thedigitalagila.com).
