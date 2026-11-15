import asyncio, pathlib, sys
from playwright.async_api import async_playwright
P = pathlib.Path(__file__).resolve().parents[2]
CSS = """@page{size:1920px 1080px;margin:0}
html,body{height:auto!important;overflow:visible!important;background:#fff!important}
#stage{position:static!important;transform:none!important;width:1920px!important;height:auto!important}
.slide{position:relative!important;inset:auto!important;width:1920px;height:1080px;opacity:1!important;page-break-after:always;break-after:page;transition:none!important}
#count,.notes{display:none!important} *{animation:none!important}
#movingDot{left:100%!important;transition:none!important} #hollowDot{left:0%!important}"""
JS = """()=>[...document.querySelectorAll('.slide')].map((s,i)=>{const r=s.getBoundingClientRect();let bad=[];
s.querySelectorAll('h1,h2,p,b,span,div,img').forEach(e=>{if(e.closest('.air')||e.classList.contains('photo'))return;
const q=e.getBoundingClientRect();if(q.width&&(q.right>r.right+1||q.bottom>r.bottom+1||q.left<r.left-1))bad.push(e.className||e.tagName)});
return bad.length?(i+1)+':'+bad.join(','):null}).filter(Boolean)"""
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width":1920,"height":1080})
        await pg.goto((P/"deck.html").as_uri()); await pg.wait_for_load_state("networkidle")
        await pg.add_style_tag(content=CSS); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(500)
        await pg.pdf(path=str(P/"CareCatalyst-deck-v3.pdf"), width="1920px", height="1080px", print_background=True)
        out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
        n = await pg.locator(".slide").count()
        for i in range(min(n, int(sys.argv[2]) if len(sys.argv)>2 else 8)):
            await pg.locator(".slide").nth(i).screenshot(path=str(out/f"s{i+1}.png"))
        print("overflow:", await pg.evaluate(JS))
        print("pages", n); await b.close()
asyncio.run(main())
