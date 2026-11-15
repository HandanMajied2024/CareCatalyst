# Builds presentation/deck.html (v3, 2-minute flow) from deck-v2-backup.html + pitch/video/facts.json
import json, re, html, pathlib
P = pathlib.Path(__file__).resolve().parents[2]
V = P.parents[1] / "pitch" / "video"
old = (P / "deck-v2-backup.html").read_text(encoding="utf-8")
head, rest = old.split('<div id="stage">', 1)
secs = re.findall(r'<section class="slide.*?</section>', rest, flags=re.S)
tail = rest[rest.index('</div>\n<div id="count">'):]
facts = {}
try: facts = json.loads((V / "facts.json").read_text(encoding="utf-8"))
except Exception: pass
rev = {}
try: rev = json.loads((V / "script_review.json").read_text(encoding="utf-8"))
except Exception: pass
e = html.escape
R = [r.get("label", "") for r in facts.get("reasons", [])][:3]
if len(R) < 3: R = ["Fear", "Distance", "Transport"]
rsrc = facts.get("reasons_source") or "Partner talk: Equitable Cancer Care"
age = facts.get("age_claim") or {}; dig = facts.get("digital_claim") or {}

def ic(d, extra=""): return f'<svg class="ic" viewBox="0 0 24 24" {extra}>{d}</svg>'
I = dict(
 fear='<circle cx="12" cy="12" r="10"/><path d="M16 16s-1.5-2-4-2-4 2-4 2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/>',
 cost='<path d="M4 10h12"/><path d="M4 14h9"/><path d="M19 6a7.7 7.7 0 0 0-5.2-2A7.9 7.9 0 0 0 6 12c0 4.4 3.5 8 7.8 8 2 0 3.8-.8 5.2-2"/>',
 book='<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
 pin='<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
 car='<path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/><path d="M9 17h6"/>',
 help='<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
 card='<rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/>',
 repeat='<path d="m17 2 4 4-4 4"/><path d="M3 11v-1a4 4 0 0 1 4-4h14"/><path d="m7 22-4-4 4-4"/><path d="M21 13v1a4 4 0 0 1-4 4H3"/>',
 bars='<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>',
 cal='<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
 mail='<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
 user='<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
 phone='<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
 check='<polyline points="20 6 9 17 4 12"/>',
 build='<path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/><path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"/><path d="M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"/><path d="M10 6h4M10 10h4M10 14h4M10 18h4"/>',
 spark='<path d="M12 3l1.9 5.8L20 10l-6.1 1.2L12 17l-1.9-5.8L4 10l6.1-1.2z"/>',
 smart='<rect x="5" y="2" width="14" height="20" rx="2"/><line x1="12" y1="18" x2="12.01" y2="18"/>',
)
def ricon(label):
    l = label.lower()
    for k, v in (("fear","fear"),("anx","fear"),("cost","cost"),("money","cost"),("financ","cost"),("litera","book"),("knowledge","book"),("distance","pin"),("transport","car"),("travel","car")):
        if k in l: return I[v]
    return I["help"]
BC = f'<span class="badge b-county">{ic(I["build"])}For counties · Today</span>'
BY = f'<span class="badge b-you">{ic(I["user"])}For you · Tomorrow</span>'
def air(i, shapes):
    ps = "".join(f'<path filter="url(#v{i})" fill="{c}" opacity="{o}" d="{d}"/>' for c, o, d in shapes)
    return f'<svg class="air" viewBox="0 0 800 600" aria-hidden="true"><defs><filter id="v{i}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="80"/></filter></defs>{ps}</svg>'

N = dict(
 p1n1=f"We know why patients miss their cancer care appointments. Research shared by companies like AstraZeneca shows it: {R[0].lower()}, {R[1].lower()}, {R[2].lower()}.",
 p1n2="But we don't know who.",
 p1n3=facts.get("narration_age") or "We do know who is most at risk: older people. And many of them struggle with smartphones.",
 p1n4="Meet CareCatalyst, for the welfare counties. They already hold the appointment data. Now they see who is stuck, and why. And they can act: for example, with a simple phone call to Eero.",
 p1n5="Counties pay once. Updates, once. No subscription. We fund the work by sharing anonymised, aggregated patterns with companies like AstraZeneca, so research can adapt.",
 p1n6="But we go one step further. The center of gravity is shifting. Just as everyone has a phone today, soon everyone will have a personal agent.",
 p2e1="…and the usual dog food for Jenny, please.", p2e2="Ah… my back.",
 p2a1="Eero, your back has been hurting for weeks, and you saw the orthopaedist last week. You are eligible for a cancer check-up. Shall I book it?",
 p2e3="Getting there is hard for me. I can't walk far. And honestly… I'm a bit scared.",
 p2a2="Don't worry. Finland already has help for people like you. Some care can come to you, and for the clinic, Kela pays the taxi. How about tomorrow at eight, before bingo with your friends?",
 p2e4="That sounds good.", p2a3="Don't worry, Eero. We've got this, together.",
 p2n1="The center of gravity is moving: towards a future where everyone gets equal care, with the help of technology.",
)
# reviewer wording changes: accepts {id: "text"} / {id:{text|new|replacement}} / {"lines"|"changes":[{id,...}]}
applied = []
def _apply(k, v):
    if isinstance(v, dict):
        if v.get("blocking") is False: return
        v = v.get("new") or v.get("replacement") or v.get("new_text") or v.get("text")
    if isinstance(v, str) and v.strip() and k in N and N[k] != v.strip():
        N[k] = v.strip(); applied.append(k)
if isinstance(rev, dict):
    items = rev.get("lines") or rev.get("changes") or rev
    if isinstance(items, list):
        for it in items:
            if isinstance(it, dict): _apply(it.get("id"), it)
    elif isinstance(items, dict):
        for k, v in items.items(): _apply(k, v)
elif isinstance(rev, list):
    for it in rev:
        if isinstance(it, dict): _apply(it.get("id"), it)
for k in N: N[k] = N[k].replace("{R1}", R[0].lower()).replace("{R2}", R[1].lower()).replace("{R3}", R[2].lower())
json.dump(N, open(P / "assets/v3/narration_v3.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
n = lambda k: e(N[k])

def claim(c, fallback):
    num, txt, src = (c.get("number") or "").strip(), (c.get("text") or "").strip(), (c.get("source") or "").strip()
    yr = str(c.get("year") or "").strip()
    if src and yr and yr not in src: src += " " + yr
    return num, (txt or fallback), src
anum, atxt, asrc = claim(age, "Cancer risk rises with age")
dnum, dtxt, dsrc = claim(dig, "Many struggle with smartphones")
import re as _re
def short(num, txt, kind):
    """big figure (short) + caption + detail for the source line"""
    if len(num) <= 8: return num, txt, ""
    if kind == "age":
        m = _re.search(r"about (\d+)", txt) or _re.search(r"(\d+)", num)
        return ("≈" + m.group(1) if m else ""), txt, num
    m = _re.match(r"\s*(\d+ in \d+)\s+(.*)", txt)
    if m: return m.group(1), m.group(2), num
    m = _re.search(r"(\d+\s?%)", num)
    return (m.group(1) if m else ""), txt, num
anum, atxt, adet = short(anum, atxt, "age")
dnum, dtxt, ddet = short(dnum, dtxt, "dig")
cap = lambda t: t[:1].upper() + t[1:]
src3 = " · ".join((cap(d) + ": " if d else "") + s for d, s in ((adet, asrc), (ddet, dsrc)) if s)
bars = "".join(f'<rect x="{20+i*74}" y="{300-h}" width="54" height="{h}" rx="12" fill="{"#e5262b" if i>=5 else "#d4d4d4"}"/>' for i, h in enumerate([18,26,40,70,120,190,260,290]))

S = []
S.append(f'''<!-- v3 · 1 why -->
<section class="slide" data-t="0:00">
  {air(1, [("#e5262b", ".14", "M600 40C700 50 790 140 770 240 750 340 660 360 600 310 540 260 500 180 520 120 535 75 560 36 600 40Z")])}
  <h1>We know why.</h1>
  <p class="sub">Why patients delay or miss cancer care.</p>
  <div class="v3why">
    <div class="v3talk"><img src="assets/v3/az_reasons_slide.png" alt="Partner talk: Equitable Cancer Care"></div>
    <div class="v3tiles">
      {"".join(f'<div class="v3tile">{ic(ricon(r))}<b>{e(r)}</b></div>' for r in R)}
    </div>
  </div>
  <p class="src">Source: {e(rsrc)}</p>
  <aside class="notes">0:00–0:12 · {n("p1n1")}</aside>
</section>''')
ppl = "".join(f'<svg class="ic" viewBox="0 0 24 24">{I["user"]}</svg>' for _ in range(9))
S.append(f'''<!-- v3 · 2 who -->
<section class="slide" data-t="0:12">
  {air(2, [("#e5262b", ".16", "M300 380C380 320 520 340 560 430 600 520 500 600 390 590 280 580 220 450 300 380Z")])}
  <div class="center" style="align-items:center">
    <div class="v3who">Who?</div>
    <div class="v3ppl">{ppl}</div>
  </div>
  <aside class="notes">0:12–0:15 · {n("p1n2")} (Pause.)</aside>
</section>''')
S.append(f'''<!-- v3 · 3 age + smartphones -->
<section class="slide" data-t="0:15">
  <h2>Most at risk: older people.</h2>
  <div class="v3two">
    <div class="v3box">
      <svg viewBox="0 0 620 320" class="v3chart" aria-label="Cancer risk rises with age"><line x1="0" y1="302" x2="620" y2="302" stroke="#e6e6e6" stroke-width="4"/>{bars}</svg>
      <div class="v3cap">{f'<b style="color:var(--red)">{e(anum)}</b>' if anum else ''}<span>{e(atxt)}</span></div>
    </div>
    <div class="v3box">
      <div class="v3phoneq">{ic(I["smart"])}<i>?</i></div>
      <div class="v3cap">{f'<b>{e(dnum)}</b>' if dnum else ''}<span>{e(dtxt)}</span></div>
    </div>
  </div>
  {f'<p class="src">{e(src3)}</p>' if src3 else ''}
  <aside class="notes">0:15–0:24 · {n("p1n3")}</aside>
</section>''')
S.append(f'''<!-- v3 · 4 CareCatalyst for the welfare counties -->
<section class="slide" data-t="0:24">
  {air(4, [("#1f5eff", ".18", "M40 420C100 360 220 380 250 460 280 540 180 600 110 590 40 580 -10 480 40 420Z"), ("#14a44d", ".14", "M200 520C260 480 350 500 360 560 370 620 280 650 230 630 180 610 160 550 200 520Z")])}
  {BC}
  <div style="position:absolute;left:140px;top:250px;width:640px">
    <h2>See who is stuck. Ask why.</h2>
    <p class="sub">CareCatalyst for wellbeing services counties.</p>
    <div class="v3call">{ic(I["phone"])}Calling Eero…</div>
  </div>
  <div class="v3tablet" style="left:850px;top:200px;width:930px"><img src="screens/LIVE-A-01-patients.png" alt="App A: patient list with risk and reasons"></div>
  <p class="src">Live demo · synthetic patients</p>
  <aside class="notes">0:24–0:39 · {n("p1n4")}</aside>
</section>''')
S.append(f'''<!-- v3 · 5 business model -->
<section class="slide" data-t="0:39" id="model3">
  {BC}
  <h2 style="margin-top:90px">Pay once. No subscription.</h2>
  <div class="v3steps">
    <div class="v3step"><div class="c" style="background:var(--green-soft);color:var(--green)">{ic(I["card"])}</div><b>Pay once</b></div>
    <div class="v3step"><div class="c">{ic(I["repeat"] + '<line x1="3" y1="3" x2="21" y2="21" stroke="#e5262b" stroke-width="2.4"/>')}</div><b>Updates: pay once</b></div>
    <div class="v3step"><div class="c" style="background:var(--blue-soft);color:var(--blue)">{ic(I["bars"])}</div><b>Anonymised patterns for research partners</b></div>
  </div>
  <aside class="notes">0:39–0:52 · {n("p1n5")}</aside>
</section>''')
S.append(f'''<!-- v3 · 6 the center of gravity shifts -->
<section class="slide" data-t="0:52" id="bridge">
  {air(6, [("#1f5eff", ".18", "M90 260C150 200 260 220 280 300 300 380 220 430 150 420 80 410 40 320 90 260Z"), ("#ffc400", ".28", "M560 250C630 200 740 230 750 320 760 410 680 450 610 430 540 410 500 300 560 250Z")])}
  <div style="position:absolute;left:140px;top:210px;width:1180px">
    <h1>The center of gravity is shifting.</h1>
    <p class="sub">Soon everyone has a personal agent.</p>
    <div class="cog" style="margin-top:90px"><span>Institution</span><div class="track"><i class="d" id="movingDot" style="left:0%"></i><i class="h" id="hollowDot" style="left:100%"></i></div><span>Person</span></div>
  </div>
  <div class="v3phone" style="left:1440px;top:150px;width:340px;height:737px"><img src="screens/B-04-booking-0800-before-bingo.png" alt="App B: the personal agent"></div>
  <aside class="notes">0:52–1:04 · {n("p1n6")}</aside>
</section>''')
S.append(f'''<!-- v3 · 7 Eero's story (Part 2, warm) -->
<section class="slide warm" data-t="1:04">
  <div class="photo" style="background-image:url(assets/eero/eero-kitchen-backpain.jpg)"></div>
  {BY}
  <div style="position:absolute;left:140px;top:220px;width:860px">
    <h2>Eero, 78, Espoo.<br>And Jenny.</h2>
    <div class="bubble"><small>{ic(I["spark"], 'width="30" height="30"')}His agent</small>“Tomorrow at eight, before bingo?”</div>
    <div class="v3chips">
      <span>{ic(I["check"])}Kela taxi</span><span>{ic(I["check"])}Home visit</span><span>{ic(I["check"])}Video visit</span>
    </div>
  </div>
  <aside class="notes">1:04–1:50 · Tell it as a story, or let the video play. Eero: “{n("p2e1")}” (something drops) “{n("p2e2")}” · Agent: “{n("p2a1")}” · Eero: “{n("p2e3")}” · Agent: “{n("p2a2")}” · Eero: “{n("p2e4")}” · Agent: “{n("p2a3")}” If asked: the agent never diagnoses, it only books the check-up.</aside>
</section>''')
S.append(f'''<!-- v3 · 8 closing: tablet + phone + three bubbles + one QR -->
<section class="slide" data-t="1:50">
  {air(8, [("#1f5eff", ".16", "M40 420C100 360 220 380 250 460 280 540 180 600 110 590 40 580 -10 480 40 420Z"), ("#ffc400", ".18", "M640 60C720 50 790 130 770 210 750 290 670 300 620 260 570 220 560 150 580 110 592 84 612 64 640 60Z")])}
  <div style="position:absolute;left:140px;top:80px;width:700px">
    <div class="wordmark"><svg width="150" height="40" viewBox="0 0 150 40"><rect x="18" y="18" width="114" height="4" rx="2" fill="#e6e6e6"/><circle cx="20" cy="20" r="13" fill="#fff" stroke="#0a0a0a" stroke-width="3"/><circle cx="130" cy="20" r="15" fill="#1f5eff"/></svg>CareCatalyst</div>
    <p class="sub" style="color:var(--fg);font-weight:700;font-size:48px;letter-spacing:-.02em;line-height:1.15">Equal care for everyone,<br>with the help of technology.</p>
  </div>
  <div class="v3tablet" style="left:140px;top:470px;width:820px"><img src="screens/LIVE-A-01-patients.png" alt="App A for counties"></div>
  <svg style="position:absolute;left:0;top:0;width:1920px;height:1080px;z-index:1" viewBox="0 0 1920 1080" aria-hidden="true" fill="none" stroke="#0a0a0a" stroke-width="3" stroke-dasharray="4 12" stroke-linecap="round">
    <path d="M1010 236 C1010 300 1130 300 1150 360"/><path d="M1200 236 L1200 360"/><path d="M1430 236 C1430 300 1250 300 1240 360"/></svg>
  <div class="v3bub" style="left:900px;top:120px;width:220px">{ic(I["cal"])}{ic(I["mail"])}</div>
  <div class="v3bub" style="left:1140px;top:120px;width:120px;color:var(--blue)">{ic(I["card"])}</div>
  <div class="v3bub txt" style="left:1280px;top:120px;width:300px">Bingo at 11 · Jenny</div>
  <div class="v3phone" style="left:1040px;top:360px;width:300px;height:650px"><img src="screens/B-04-booking-0800-before-bingo.png" alt="App B, the personal agent"></div>
  <div class="qr" style="position:absolute;left:1480px;top:470px"><div class="box"><img src="assets/qr-landing.svg" alt="QR code to the CareCatalyst landing page"></div><div class="lab" style="background:var(--blue-soft);color:var(--blue)">Try it</div></div>
  <aside class="notes">1:50–2:00 · {n("p2n1")} Leave this slide up during Q&amp;A: the QR opens the landing page (For counties = app A, For you = app B).</aside>
</section>''')

# appendix from v2: Q&A limits, Goal 3, business case, model, proposals, how it works, live demo, a2a, CarePulse, why/how many/who, cold open, no call, center today
order = [14, 3, 8, 9, 7, 5, 6, 12, 11, 2, 0, 1, 4]
app = []
for k in order:
    s = re.sub(r'data-t="[^"]*"', 'data-t="Q&amp;A"' if k == 14 else 'data-t="Appendix"', secs[k], count=1)
    s = s.replace("centre", "center").replace("welfare county", "wellbeing services county")
    app.append(f"<!-- appendix (from v2 slide {k+1}) -->\n" + s)

css = '''
/* --- v3 (2-minute flow) --- */
.src{font-size:26px}
.v3why{display:flex;gap:56px;align-items:center;margin-top:64px}
.v3talk{flex:none;width:520px;border-radius:24px;overflow:hidden;border:1px solid var(--line);box-shadow:0 24px 60px rgba(0,0,0,.14);transform:rotate(-3deg)}
.v3talk img{display:block;width:100%}
.v3tiles{flex:1;display:flex;gap:28px}
.v3tile{flex:1;min-height:400px;border-radius:36px;background:var(--red-soft);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:36px;padding:30px;text-align:center}
.v3tile svg{width:130px;height:130px;color:var(--red);stroke-width:1.75}
.v3tile b{font-size:52px;font-weight:800;letter-spacing:-.02em;line-height:1.1}
.v3who{font-size:380px;font-weight:800;letter-spacing:-.05em;line-height:1;color:var(--red)}
.v3ppl{display:flex;gap:36px;margin-top:50px;color:#c9c9c9}
.v3ppl svg{width:120px;height:120px}
.v3two{display:flex;gap:40px;margin-top:60px}
.v3box{flex:1;height:570px;border-radius:36px;background:var(--surface);padding:50px 56px;display:flex;flex-direction:column;justify-content:space-between;align-items:flex-start}
.v3chart{width:620px;height:320px}
.v3cap{display:flex;align-items:baseline;gap:28px;flex-wrap:wrap;width:100%}
.v3cap b{font-size:120px;font-weight:800;letter-spacing:-.03em;line-height:1;white-space:nowrap;font-variant-numeric:tabular-nums}
.v3cap span{font-size:36px;font-weight:600;line-height:1.25;flex:1;min-width:300px}
.v3phoneq{position:relative;width:220px;height:320px}
.v3phoneq svg{width:320px;height:320px;margin-left:-50px;stroke-width:1.2}
.v3phoneq i{position:absolute;left:0;right:0;top:66px;text-align:center;font-style:normal;font-size:130px;font-weight:800;color:var(--red)}
.v3tablet{position:absolute!important;border:18px solid #0a0a0a;border-radius:44px;overflow:hidden;background:#fff;box-shadow:0 40px 90px rgba(0,0,0,.22)}
.v3tablet img{display:block;width:100%}
.v3phone{position:absolute!important;border:12px solid #0a0a0a;border-radius:52px;overflow:hidden;background:#fff;box-shadow:0 40px 90px rgba(0,0,0,.22)}
.v3phone img{display:block;width:100%;height:100%;object-fit:cover;object-position:top}
.v3call{display:inline-flex;align-items:center;gap:22px;margin-top:56px;padding:26px 44px;border-radius:999px;background:var(--blue);color:#fff;font-size:44px;font-weight:700;box-shadow:0 20px 50px rgba(31,94,255,.35)}
.v3call svg{width:46px;height:46px}
.v3steps{display:flex;gap:40px;margin-top:90px}
.v3step{flex:1;border-radius:36px;background:var(--surface);padding:60px 44px;min-height:520px;display:flex;flex-direction:column;align-items:center;gap:50px;text-align:center}
.v3step .c{width:220px;height:220px;border-radius:60px;background:#fff;display:grid;place-items:center}
.v3step .c svg{width:110px;height:110px;stroke-width:1.75}
.v3step b{font-size:46px;font-weight:800;letter-spacing:-.02em;line-height:1.15}
.v3chips{display:flex;gap:18px;margin-top:36px;flex-wrap:wrap}
.v3chips span{display:inline-flex;align-items:center;gap:12px;padding:16px 28px;border-radius:999px;background:var(--green-soft);color:#0b6b31;font-size:32px;font-weight:700}
.v3chips svg{width:32px;height:32px;stroke-width:3}
.v3bub{position:absolute!important;z-index:2!important;height:116px;border-radius:40px;background:#fff;border:1px solid var(--line);box-shadow:0 16px 40px rgba(0,0,0,.10);display:flex;align-items:center;justify-content:center;gap:26px}
.v3bub svg{width:56px;height:56px}
.v3bub.txt{font-size:30px;font-weight:700}
.v3phone,.v3tablet{z-index:2!important}
'''
out = head.replace("</style>", css + "</style>").replace("<title>CareCatalyst Pitch</title>", "<title>CareCatalyst Pitch · 2 min</title>")
out += '<div id="stage">\n\n' + "\n\n".join(S) + "\n\n" + "\n\n".join(app) + "\n\n" + tail
(P / "deck.html").write_text(out, encoding="utf-8")
print("slides", len(S), "+ appendix", len(app), "| reasons", R, "| age", repr(anum), "| digital", repr(dnum), "| review applied", applied, "| review file", bool(rev))
