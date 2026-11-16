# Demo Business Website — a Claude skill

A Claude skill that builds premium, multi-page demo websites for small businesses: the kind of site you can show a prospect so they think "that's what my business should look like".

Made for web designers and agencies who pitch websites to local businesses (clinics, trades, salons, cafés and more).

## What it does

- **Multi-page sites, fully filled.** Every menu item is its own page with real sections: services and prices, team, FAQs, opening hours, booking flow, contact and more.
- **A unique design every time.** The skill derives a brand personality from the business, picks a look across 10 design choices (layout, fonts, colours, shapes, navigation, hero, image style, sections, buttons, motion) and checks a design log so no two demos look the same.
- **Real photos, kept sharp.** Uses your photos (or generated ones, if you have an image tool connected), cropped to fit each spot and published at full resolution.
- **Animated heroes that fit the business.** A different hero on every page, with animated cards that never cover faces in the photos.
- **Ambient 3D effect matched to the industry.** Frost for air conditioning, paw prints for vets, sparkles for dental, water drops for plumbing, leaves for landscaping and 8 more themes. A ready-made engine (`assets/ambient.js`) is included.
- **Safe demo details.** Fictional business names, people, emails and reserved fictional phone numbers, with testimonials labelled as samples.
- **Tested before delivery.** Every page is checked at desktop and phone sizes for hidden content, overflow and errors.

## Install

### Claude apps (claude.ai, desktop, mobile)

1. Download this repo as a ZIP (green **Code** button → **Download ZIP**).
2. Unzip it and zip **only** the `demo-business-website` folder (so the zip contains `demo-business-website/SKILL.md`).
3. In Claude, go to **Settings → Capabilities → Skills** and upload that zip. (Skills must be enabled for your account.)

### Claude Code

Copy the skill folder into your skills directory:

```bash
git clone https://github.com/jaysdigital-ai/business-website-skill.git
cp -r business-website-skill/demo-business-website ~/.claude/skills/
```

## Use it

Just ask, for example:

> Build a demo website for a dental clinic in Melbourne.

> Make a sample site for a landscaping business. Use these photos.

Claude will confirm the business, the look and the hero direction with you, then build the site, test it and hand you the files (and a link, where your Claude environment can publish pages).

## What's inside

```
demo-business-website/
├── SKILL.md            # the instructions Claude follows
└── assets/
    └── ambient.js      # themed 3D particle layer (no dependencies)
```

## Notes

- The ambient effect turns itself off for visitors who prefer reduced motion and pauses when off screen.
- All business details in generated demos are fictional. Replace them, and the sample testimonials, before using a design for a real client.

## License

MIT, see [LICENSE](LICENSE). Made by [The Digital Agila](https://thedigitalagila.com).
