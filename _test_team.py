"""Diagnose team carousel issues on mobile"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 375, "height": 812})
    page.goto("http://localhost:8080")
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(1000)

    btn = page.locator("text=Browse Freely")
    if btn.is_visible():
        btn.click()
        page.wait_for_timeout(800)

    # Scroll section to exact viewport top
    page.evaluate("document.getElementById('team').scrollIntoView({block:'start',behavior:'instant'})")
    page.wait_for_timeout(300)
    page.evaluate("window.scrollBy(0, document.getElementById('team').getBoundingClientRect().top)")
    page.wait_for_timeout(300)

    info = page.evaluate("""() => {
        var section = document.getElementById('team');
        var sectionR = section.getBoundingClientRect();
        var grid = section.querySelector('.roles-grid');
        var gridR = grid.getBoundingClientRect();
        var dots = section.querySelector('.team-dots');
        var dotsR = dots ? dots.getBoundingClientRect() : null;
        var cards = grid.querySelectorAll('.role-card');
        var cardRects = [];
        cards.forEach(function(c) {
            var r = c.getBoundingClientRect();
            cardRects.push({ top: r.top, bottom: r.bottom, height: r.height, left: r.left, width: r.width });
        });
        return {
            viewport: window.innerHeight,
            sectionTop: sectionR.top,
            sectionHeight: sectionR.height,
            gridTop: gridR.top,
            gridBottom: gridR.bottom,
            gridHeight: gridR.height,
            gridScrollWidth: grid.scrollWidth,
            gridClientWidth: grid.clientWidth,
            dotsTop: dotsR ? dotsR.top : null,
            dotsBottom: dotsR ? dotsR.bottom : null,
            dotsVisible: dotsR ? (dotsR.bottom <= window.innerHeight) : false,
            cards: cardRects
        };
    }""")

    vp = info['viewport']
    st = info['sectionTop']
    print("=== Team Section Layout ===")
    print(f"  Viewport: {vp}px")
    print(f"  Section: top={st:.1f}, height={info['sectionHeight']:.0f}")
    print(f"  Grid: offset={info['gridTop']-st:.0f}, height={info['gridHeight']:.0f}")
    print(f"  Grid scroll: scrollW={info['gridScrollWidth']:.0f}, clientW={info['gridClientWidth']:.0f}")
    dt = info['dotsTop'] - st if info['dotsTop'] else None
    db = info['dotsBottom'] - st if info['dotsBottom'] else None
    print(f"  Dots: offset={dt:.0f}-{db:.0f} (viewport pos={info['dotsTop']:.0f}-{info['dotsBottom']:.0f}), visible={info['dotsVisible']}")
    for i, c in enumerate(info['cards']):
        print(f"  Card {i}: offset={c['top']-st:.0f}, height={c['height']:.0f}, left={c['left']:.0f}, width={c['width']:.0f}")

    fits = info['dotsBottom'] and info['dotsBottom'] <= vp
    print(f"\n  {'OK: Everything fits in viewport' if fits else 'PROBLEM: Dots below viewport fold (' + str(round(info['dotsBottom'] - vp)) + 'px over)'}")

    page.screenshot(path="/tmp/team_debug.png", full_page=False)

    browser.close()
