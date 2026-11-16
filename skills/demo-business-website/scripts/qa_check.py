#!/usr/bin/env python3
"""QA check for a static demo website.

Renders every .html page in a site folder at desktop (1440px) and phone (390px)
widths in headless Chromium, scrolls through it, and reports problems a visitor
would notice. Saves screenshots for a visual review.

Usage:
  python3 qa_check.py SITE_DIR [--out QA_DIR] [--chrome /path/to/chrome] [--json]

Requires Playwright:  pip install playwright && python -m playwright install chromium
Exit code: 0 = no blockers found, 1 = blockers found, 2 = setup error.
"""
import argparse, asyncio, json, os, re, sys
from pathlib import Path
from urllib.parse import urlparse, unquote

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Playwright is not installed. Run: pip install playwright && python -m playwright install chromium")
    sys.exit(2)

WIDTHS = {"desktop": (1440, 900), "phone": (390, 844)}

CHECK_JS = r"""
() => {
  const out = {hidden: [], noAlt: [], lowRes: [], h1: 0, title: document.title || '',
               desc: (document.querySelector('meta[name=description]')||{}).content || '',
               lang: document.documentElement.lang || '', jsonld: [], overflow: false, links: []};
  out.overflow = document.documentElement.scrollWidth > window.innerWidth + 1;
  out.h1 = document.querySelectorAll('h1').length;
  // Elements with real content that are still invisible after a full scroll
  // Heroes, carousels and anything marked data-qa-ignore have intentional hidden states (rotating words, inactive slides).
  const skip = el => el.closest('[aria-hidden="true"],nav,.mnav,[hidden],dialog,template,noscript,script,style,.hero,[data-hero],[data-qa-ignore],[aria-roledescription=carousel]');
  document.querySelectorAll('main *').forEach(el => {
    if (skip(el)) return;
    const hasContent = (el.children.length === 0 && el.textContent.trim().length > 2) || el.tagName === 'IMG' || el.getAttribute('role') === 'img';
    if (!hasContent) return;
    let node = el, invisible = false;
    while (node && node !== document.body) {
      const cs = getComputedStyle(node);
      if (parseFloat(cs.opacity) < 0.05) { invisible = true; break; }
      node = node.parentElement;
    }
    const r = el.getBoundingClientRect();
    if (invisible && r.width > 0 && r.height > 0) {
      out.hidden.push((el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/).join('.') : el.tagName.toLowerCase()) + ' :: ' + (el.textContent || el.getAttribute('aria-label') || '').trim().slice(0, 50));
    }
  });
  document.querySelectorAll('img').forEach(img => {
    if (!img.hasAttribute('alt')) out.noAlt.push(img.getAttribute('src'));
    const r = img.getBoundingClientRect();
    if (img.naturalWidth && r.width && img.naturalWidth < r.width * 1.5) out.lowRes.push(img.getAttribute('src') + ' (' + img.naturalWidth + 'px shown at ' + Math.round(r.width) + 'px)');
  });
  document.querySelectorAll('[role=img]').forEach(el => { if (!el.getAttribute('aria-label')) out.noAlt.push('role=img ' + (el.className || '')); });
  // background images: check resolution against displayed size
  document.querySelectorAll('main *').forEach(el => {
    const bg = getComputedStyle(el).backgroundImage;
    const m = bg && bg.match(/url\(["']?([^"')]+)["']?\)/);
    if (m && !m[1].startsWith('data:')) out.links.push({kind: 'bg', url: m[1], w: el.getBoundingClientRect().width});
  });
  document.querySelectorAll('script[type="application/ld+json"]').forEach(s => {
    try { JSON.parse(s.textContent); out.jsonld.push('ok'); } catch (e) { out.jsonld.push('INVALID: ' + e.message); }
  });
  document.querySelectorAll('a[href]').forEach(a => out.links.push({kind: 'a', url: a.getAttribute('href')}));
  document.querySelectorAll('img[src],link[rel=stylesheet][href],script[src]').forEach(e => out.links.push({kind: 'asset', url: e.getAttribute('src') || e.getAttribute('href')}));
  return out;
}
"""

def local_target(site, page, url):
    if not url or url.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return None
    p = urlparse(url)
    if p.scheme == "file":
        return Path(unquote(p.path))
    if p.scheme in ("http", "https") or url.startswith("//"):
        return None
    path = unquote(p.path)
    if not path:
        return None
    base = page.parent
    return (site / path.lstrip("/")) if path.startswith("/") else (base / path)

async def run(site, out, chrome):
    pages = sorted(site.rglob("*.html"))
    if not pages:
        print(f"No .html files found in {site}")
        return 2
    out.mkdir(parents=True, exist_ok=True)
    report = {"pages": {}, "blockers": 0, "majors": 0}
    async with async_playwright() as p:
        kw = {"args": ["--no-sandbox"]}
        if chrome:
            kw["executable_path"] = chrome
        browser = await p.chromium.launch(**kw)
        for page_path in pages:
            rel = str(page_path.relative_to(site))
            report["pages"][rel] = {}
            for wname, (w, h) in WIDTHS.items():
                ctx = await browser.new_context(viewport={"width": w, "height": h})
                pg = await ctx.new_page()
                errors = []
                pg.on("pageerror", lambda e, errors=errors: errors.append("pageerror: " + str(e)))
                pg.on("console", lambda m, errors=errors: errors.append("console: " + m.text) if m.type == "error" and "fonts.g" not in m.text else None)
                await pg.goto(page_path.resolve().as_uri())
                await pg.wait_for_timeout(1200)
                height = await pg.evaluate("document.body.scrollHeight")
                y = 0
                while y < height:
                    y += int(h * 0.6)
                    await pg.evaluate(f"window.scrollTo(0,{y})")
                    await pg.wait_for_timeout(140)
                await pg.wait_for_timeout(1600)
                data = await pg.evaluate(CHECK_JS)
                await pg.evaluate("window.scrollTo(0,0)")
                await pg.wait_for_timeout(400)
                shot = out / f"{rel.replace('/', '_')}-{wname}.png"
                await pg.screenshot(path=str(shot), full_page=True)
                broken = []
                for link in data.pop("links"):
                    t = local_target(site, page_path, link["url"])
                    if t is not None and not t.exists():
                        broken.append(f'{link["kind"]}: {link["url"]}')
                issues = []
                if data["hidden"]:
                    issues.append(("blocker", f'{len(data["hidden"])} element(s) still hidden after scrolling, e.g. ' + "; ".join(data["hidden"][:4])))
                if data["overflow"]:
                    issues.append(("major", "horizontal overflow (page scrolls sideways)"))
                if errors:
                    issues.append(("major", "script errors: " + "; ".join(errors[:3])))
                if broken:
                    issues.append(("blocker", "broken links or missing files: " + "; ".join(sorted(set(broken))[:6])))
                if wname == "desktop":
                    if data["noAlt"]:
                        issues.append(("major", "images without alt text: " + "; ".join(map(str, data["noAlt"][:4]))))
                    if data["lowRes"]:
                        issues.append(("major", "low-resolution images: " + "; ".join(data["lowRes"][:4])))
                    if data["h1"] != 1:
                        issues.append(("major", f'{data["h1"]} H1 headings (expected exactly 1)'))
                    if not data["title"]:
                        issues.append(("major", "missing <title>"))
                    if not data["desc"]:
                        issues.append(("minor", "missing meta description"))
                    if not data["lang"]:
                        issues.append(("minor", "missing lang attribute on <html>"))
                    bad = [j for j in data["jsonld"] if j != "ok"]
                    if bad:
                        issues.append(("major", "invalid JSON-LD: " + "; ".join(bad)))
                report["pages"][rel][wname] = {"issues": issues, "screenshot": str(shot)}
                report["blockers"] += sum(1 for s, _ in issues if s == "blocker")
                report["majors"] += sum(1 for s, _ in issues if s == "major")
                await ctx.close()
        await browser.close()
    return report

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("site")
    ap.add_argument("--out", default=None, help="folder for screenshots (default: SITE/../qa)")
    ap.add_argument("--chrome", default=None, help="path to a Chrome/Chromium binary to use")
    ap.add_argument("--json", action="store_true", help="print the full report as JSON")
    a = ap.parse_args()
    site = Path(a.site).resolve()
    out = Path(a.out).resolve() if a.out else site.parent / "qa"
    report = asyncio.run(run(site, out, a.chrome))
    if isinstance(report, int):
        sys.exit(report)
    if a.json:
        print(json.dumps(report, indent=2))
    else:
        for page, widths in report["pages"].items():
            for wname, r in widths.items():
                status = "OK " if not r["issues"] else "!! "
                print(f"{status}{page} [{wname}]")
                for sev, msg in r["issues"]:
                    print(f"     - {sev.upper()}: {msg}")
        print(f"\nBlockers: {report['blockers']}  Majors: {report['majors']}  Screenshots: {out}")
        print("VERDICT:", "PASS" if report["blockers"] == 0 and report["majors"] == 0 else "FAIL")
    sys.exit(1 if report["blockers"] else 0)

if __name__ == "__main__":
    main()
