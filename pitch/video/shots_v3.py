"""Screenshots of the live apps for video v3.  usage: python shots_v3.py"""
from pathlib import Path
from playwright.sync_api import sync_playwright
OUT = Path(__file__).resolve().parent / "img/v3"; OUT.mkdir(parents=True, exist_ok=True)
A = "https://handan-majied1--carecatalyst-demo-web.modal.run"
B = "https://handan-majied1--carepulse-vision-web.modal.run"
def settle(pg):
    try: pg.wait_for_load_state("networkidle", timeout=20000)
    except Exception as e: print("idle timeout")
    pg.wait_for_timeout(1500)
def shot(pg, name): settle(pg); pg.screenshot(path=str(OUT / name)); print("ok", name)
def click(pg, text, name, exact=False):
    try:
        pg.get_by_text(text, exact=exact).first.click(timeout=6000); shot(pg, name)
    except Exception as e: print("SKIP", name, str(e)[:150])
with sync_playwright() as p:
    br = p.chromium.launch()
    pg = br.new_context(viewport={"width":1366,"height":1024}, device_scale_factor=2).new_page()
    pg.goto(A, timeout=90000); shot(pg, "a_patients.png")
    click(pg, "Regional summary", "a_regional.png"); click(pg, "Regional support", "a_support.png")
    pg = br.new_context(viewport={"width":390,"height":844}, device_scale_factor=3, is_mobile=True, has_touch=True).new_page()
    pg.goto(B, timeout=90000); shot(pg, "b_today.png")
    print("B texts:", pg.evaluate("[...document.querySelectorAll('nav *, button, a')].map(e=>(e.innerText||e.getAttribute('aria-label')||'').trim()).filter(t=>t&&t.length<20).slice(0,60)"))
    for t, n in [("Agent","b_agent.png"),("Plan","b_plan.png"),("Health","b_health.png"),("Me","b_me.png")]:
        click(pg, t, n, exact=True)
    br.close()
