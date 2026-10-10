"""Build the den's self-contained SVG artwork. Run with Python 3; no dependencies."""

from pathlib import Path
from string import Template
from xml.sax.saxutils import escape


ASSETS = Path(__file__).resolve().parents[1] / "assets"
THEMES = {
    "dark": dict(bg="#101B23", panel="#15252E", ink="#F1EEE5", muted="#A8BCC1",
                 line="#30434B", accent="#7DE2CB", warm="#F6B77D", grid="#253740"),
    "light": dict(bg="#F6F3EB", panel="#FFFCF5", ink="#17343B", muted="#506970",
                  line="#C7D5CF", accent="#126956", warm="#9B4924", grid="#E0E5DA"),
}

BANNER = Template('''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="480" viewBox="0 0 1000 480" role="img" aria-labelledby="title desc">
  <title id="title">Mayeen's Curiosity Den</title>
  <desc id="desc">Curiosity lives here. Mayeen Abedin Sajid, Senior Software QA Engineer in Dhaka. An orbiting constellation of questions, code, and evidence surrounds a glowing idea. A tiny robot keeps watch. Come for the code. Stay for the questions.</desc>
  <defs>
    <pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="$grid"/></pattern>
    <radialGradient id="halo"><stop stop-color="$accent" stop-opacity=".13"/><stop offset="1" stop-color="$accent" stop-opacity="0"/></radialGradient>
  </defs>
  <style>
    text { font-family: 'Segoe UI', Helvetica, Arial, sans-serif; }
    .mono { font-family: Consolas, 'Liberation Mono', monospace; }
    .orbit { transform-origin: 763px 220px; animation: orbit 38s linear infinite; }
    .reverse { animation-direction: reverse; animation-duration: 50s; }
    .breathe { animation: breathe 5s ease-in-out infinite; }
    .spark { animation: sparkle 6s ease-in-out infinite; }
    .spark-late { animation-delay: -3s; }
    .cursor { animation: blink 1.4s steps(1) infinite; }
    .robot { animation: bob 5s ease-in-out infinite; }
    .eyes { transform-origin: 852px 358px; animation: eyes 7s infinite; }
    .signal { stroke-dasharray: 5 11; animation: signal 6s linear infinite; }
    @keyframes orbit { to { transform: rotate(360deg); } }
    @keyframes breathe { 0%,100% { opacity:.45; } 50% { opacity:1; } }
    @keyframes sparkle { 0%,100% { opacity:.35; } 50% { opacity:1; } }
    @keyframes blink { 0%,65% { opacity:1; } 66%,100% { opacity:0; } }
    @keyframes bob { 0%,100% { transform:translateY(0); } 50% { transform:translateY(-5px); } }
    @keyframes eyes { 0%,43%,47%,100% { transform:scaleY(1); } 45% { transform:scaleY(.12); } }
    @keyframes signal { to { stroke-dashoffset:-64; } }
    @media (prefers-reduced-motion: reduce) { * { animation:none !important; } }
  </style>

  <rect x="1" y="1" width="998" height="478" rx="24" fill="$bg" stroke="$line"/>
  <rect x="1" y="1" width="998" height="478" rx="24" fill="url(#grid)"/>
  <path d="M40 76H960 M40 419H960" stroke="$line"/>
  <circle cx="48" cy="43" r="5" fill="$accent" class="breathe"/>
  <text x="64" y="48" class="mono" font-size="13" letter-spacing="2" fill="$ink">MAYEEN / THE CURIOSITY DEN</text>
  <text x="955" y="48" text-anchor="end" class="mono" font-size="12" letter-spacing="1" fill="$muted">EST. IN DHAKA · OPEN TO IDEAS</text>

  <text x="48" y="124" class="mono" font-size="13" letter-spacing="2" fill="$accent">HELLO, FELLOW EXPLORER.</text>
  <text x="44" y="207" font-size="76" font-weight="750" letter-spacing="-3" fill="$ink">Curiosity</text>
  <text x="44" y="289" font-size="76" font-weight="750" letter-spacing="-3" fill="$ink">lives here<tspan fill="$warm">.</tspan></text>
  <path d="M49 309 Q172 300 292 309" stroke="$warm" stroke-width="3" fill="none" stroke-linecap="round"/>
  <text x="48" y="353" font-size="23" font-weight="600" fill="$ink">Mayeen Abedin Sajid</text>
  <text x="48" y="383" font-size="16" fill="$muted">Senior Software QA Engineer · Builder · Bug detective</text>

  <!-- The idea observatory: decorative motion, never a live status indicator. -->
  <circle cx="763" cy="220" r="183" fill="url(#halo)" class="breathe"/>
  <g fill="none" stroke="$line">
    <circle cx="763" cy="220" r="132"/>
    <circle cx="763" cy="220" r="97" stroke-dasharray="3 8"/>
    <path d="M599 220H927 M763 65V374" stroke-dasharray="2 8"/>
    <ellipse cx="763" cy="220" rx="161" ry="63" transform="rotate(-32 763 220)"/>
  </g>
  <g class="orbit"><circle cx="763" cy="88" r="6" fill="$accent"/><circle cx="763" cy="352" r="4" fill="$warm"/></g>
  <g class="orbit reverse"><circle cx="860" cy="220" r="4" fill="$warm"/></g>
  <g class="spark" fill="$warm"><path d="M909 119v16m-8-8h16" stroke="$warm" stroke-width="2"/><circle cx="595" cy="167" r="3"/></g>
  <g class="spark spark-late" stroke="$accent" stroke-width="2"><path d="M638 317v12m-6-6h12 M911 284v12m-6-6h12"/></g>

  <circle cx="763" cy="220" r="60" fill="$panel" stroke="$accent" stroke-opacity=".5"/>
  <circle cx="763" cy="220" r="51" fill="none" stroke="$line"/>
  <g fill="none" stroke="$accent" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
    <path d="M746 223c-16-16-4-40 17-40s33 24 17 40c-5 5-7 9-7 15h-20c0-6-2-10-7-15Z"/>
    <path d="M754 245h18m-14 7h10m-5-15v-24m-7-6 7 7 7-7"/>
    <path d="M763 171v-7m-35 20-5-5m-5 30h-7m87-25 5-5m5 30h7" class="breathe"/>
  </g>

  <g class="mono" font-size="12" letter-spacing="1">
    <rect x="588" y="100" width="117" height="32" rx="16" fill="$panel" stroke="$line"/>
    <text x="646" y="121" text-anchor="middle" fill="$accent" class="mono">WHAT IF?</text>
    <rect x="847" y="188" width="113" height="32" rx="16" fill="$panel" stroke="$line"/>
    <text x="903" y="209" text-anchor="middle" fill="$ink" class="mono">LET'S BUILD</text>
    <rect x="604" y="277" width="112" height="32" rx="16" fill="$panel" stroke="$line"/>
    <text x="660" y="298" text-anchor="middle" fill="$ink" class="mono">PROVE IT.</text>
  </g>

  <path d="M754 334v41h63" fill="none" stroke="$accent" stroke-opacity=".5" class="signal"/>
  <g class="robot">
    <path d="M852 328v10" stroke="$muted" stroke-width="2"/>
    <circle cx="852" cy="326" r="4" fill="$warm" class="breathe"/>
    <rect x="822" y="338" width="60" height="41" rx="13" fill="$panel" stroke="$muted" stroke-width="1.5"/>
    <g class="eyes" fill="$accent"><rect x="834" y="352" width="8" height="9" rx="4"/><rect x="862" y="352" width="8" height="9" rx="4"/></g>
    <path d="M847 368q5 4 10 0" fill="none" stroke="$muted" stroke-width="1.5" stroke-linecap="round"/>
    <path d="M833 386h38m-32-6v6m26-6v6" stroke="$muted" stroke-width="2" stroke-linecap="round"/>
    <path d="M885 356l8-7 3-9" stroke="$warm" stroke-width="3" fill="none" stroke-linecap="round"/>
  </g>
  <text x="48" y="452" class="mono" font-size="13" fill="$muted">&gt; come for the code. stay for the questions.</text>
  <rect x="426" y="440" width="8" height="15" rx="1" fill="$accent" class="cursor"/>
  <text x="953" y="452" text-anchor="end" class="mono" font-size="12" fill="$muted">SCROLL TO EXPLORE ↓</text>
</svg>
''')

NOTES = Template('''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="152" viewBox="0 0 1000 152" role="img" aria-labelledby="title desc">
  <title id="title">Notes from the desk</title>
  <desc id="desc">Three rotating desk notes: A passing test answers a question. Curiosity asks a better one. Make room for the strange idea. Then build a way to test it. Leave the code clearer, the product kinder, and the next person a clue.</desc>
  <style>
    text { font-family: 'Segoe UI', Helvetica, Arial, sans-serif; }
    .mono { font-family: Consolas, 'Liberation Mono', monospace; }
    .note { animation-duration:24s; animation-timing-function:linear; animation-iteration-count:infinite; }
    .one { animation-name:first; }
    .two { opacity:0; animation-name:second; }
    .three { opacity:0; animation-name:third; }
    @keyframes first { 0%,29%,100% { opacity:1; } 33%,95% { opacity:0; } }
    @keyframes second { 0%,29%,66%,100% { opacity:0; } 33%,62% { opacity:1; } }
    @keyframes third { 0%,62%,100% { opacity:0; } 66%,95% { opacity:1; } }
    @media (prefers-reduced-motion: reduce) { .note { animation:none; } .one { opacity:1; } .two,.three { opacity:0; } }
  </style>
  <rect x="1" y="1" width="998" height="150" rx="16" fill="$bg" stroke="$line"/>
  <path d="M29 28v96" stroke="$warm" stroke-width="3" stroke-linecap="round"/>
  <text x="52" y="36" class="mono" font-size="12" letter-spacing="2" fill="$muted">NOTES FROM THE DESK / A LITTLE FUEL FOR YOUR NEXT IDEA</text>
  <g class="note one">
    <text x="52" y="80" font-size="27" font-weight="600" fill="$ink">A passing test answers a question.</text>
    <text x="52" y="116" font-size="27" fill="$accent">Curiosity asks a better one.</text>
    <text x="949" y="118" text-anchor="end" class="mono" font-size="13" fill="$muted">01 / 03</text>
  </g>
  <g class="note two">
    <text x="52" y="80" font-size="27" font-weight="600" fill="$ink">Make room for the strange idea.</text>
    <text x="52" y="116" font-size="27" fill="$accent">Then build a way to test it.</text>
    <text x="949" y="118" text-anchor="end" class="mono" font-size="13" fill="$muted">02 / 03</text>
  </g>
  <g class="note three">
    <text x="52" y="80" font-size="27" font-weight="600" fill="$ink">Leave the code clearer, the product kinder,</text>
    <text x="52" y="116" font-size="27" fill="$accent">and the next person a clue.</text>
    <text x="949" y="118" text-anchor="end" class="mono" font-size="13" fill="$muted">03 / 03</text>
  </g>
</svg>
''')


CARD = Template('''<svg xmlns="http://www.w3.org/2000/svg" width="720" height="112" viewBox="0 0 720 112" role="img" aria-labelledby="title desc">
  <title id="title">$title</title>
  <desc id="desc">$subtitle. Open this card to read a short note.</desc>
  <style>
    text { font-family:'Segoe UI',Helvetica,Arial,sans-serif; }
    .float { animation:float 4s ease-in-out infinite; }
    .trace { stroke-dasharray:4 8; animation:trace 8s linear infinite; }
    .pulse { animation:pulse 4s ease-in-out infinite; }
    .turn { transform-origin:56px 56px; animation:turn 24s linear infinite; }
    @keyframes float { 0%,100% { transform:translateY(2px); } 50% { transform:translateY(-3px); } }
    @keyframes trace { to { stroke-dashoffset:-96; } }
    @keyframes pulse { 0%,100% { opacity:.35; } 50% { opacity:.9; } }
    @keyframes turn { to { transform:rotate(360deg); } }
    @media(max-width:400px) {
      .card-title { font-size:40px; transform:translateY(16px); }
      .card-subtitle { display:none; }
    }
    @media(prefers-reduced-motion:reduce) { * { animation:none !important; } }
  </style>
  <rect x="1" y="1" width="718" height="110" rx="18" fill="$bg" stroke="$line"/>
  <rect x="1" y="1" width="718" height="110" rx="18" fill="$card_accent" fill-opacity=".055"/>
  <path d="M19 30v52" stroke="$card_accent" stroke-width="3" stroke-linecap="round"/>
  <circle cx="64" cy="56" r="31" fill="$card_accent" fill-opacity=".10"/>
  <g transform="translate(8 0)" fill="none" stroke="$card_accent" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">$icon</g>
  <text class="card-title" x="116" y="48" font-size="28" font-weight="650" fill="$ink">$title</text>
  <text class="card-subtitle" x="116" y="79" font-size="18" fill="$muted">$subtitle</text>
  <path d="M570 56h45" stroke="$card_accent" stroke-opacity=".5" class="trace"/>
  <circle cx="658" cy="56" r="22" fill="$panel" stroke="$card_accent" stroke-opacity=".5"/>
  <path d="M650 56h16m-8-8v16" stroke="$card_accent" stroke-width="2" stroke-linecap="round"/>
</svg>
''')

CARDS = {
    "museum": dict(title="Bug Museum", subtitle="Small bugs. Plot twists. Case closed?", color="violet",
                   icon='<g class="float"><rect x="44" y="42" width="24" height="30" rx="12"/><path d="M49 42v-6m14 6v-6M44 49l-8-5m8 13h-9m9 8-8 5m32-21 8-5m-8 13h9m-9 8 8 5M56 44v25"/><circle cx="51" cy="50" r="1"/><circle cx="61" cy="50" r="1"/></g>'),
    "playwright": dict(title="The test kitchen", subtitle="Fresh tests. Zero mystery ingredients.", color="accent",
                       icon='<g class="float"><rect x="34" y="36" width="44" height="37" rx="6"/><path d="M34 45h44m-36-5h1m5 0h1m5 0h1M46 58l7 7 13-14"/></g><path d="M36 81h40" class="trace"/>'),
    "grocery": dict(title="GroceryMate", subtitle="Split the bill. Keep the friendship.", color="warm",
                    icon='<g class="float"><path d="M35 46h42l-5 27H40Zm10 0 6-12m16 12-6-12m-13 22V54m8 12V54m8 12V54"/><path d="M40 78h32"/></g>'),
    "toolkit": dict(title="The gadget drawer", subtitle="A few tools. A lot of what-ifs.", color="blue",
                    icon='<g class="turn"><ellipse cx="56" cy="56" rx="26" ry="11"/><ellipse cx="56" cy="56" rx="26" ry="11" transform="rotate(60 56 56)"/><ellipse cx="56" cy="56" rx="26" ry="11" transform="rotate(120 56 56)"/></g><circle cx="56" cy="56" r="4" fill="$card_accent"/>'),
    "now": dict(title="On my mind", subtitle="Ideas currently stealing my attention.", color="violet",
                icon='<g class="float"><path d="M44 57a17 17 0 1 1 24 0l-4 6H48Zm5 12h14m-11 6h8"/><path d="M56 28v-5M34 39l-4-3m48 3 4-3" class="pulse"/></g>'),
    "play": dict(title="One tiny mystery", subtitle="One cookie. Two orders. Something's off.", color="warm",
                 icon='<g class="float"><circle cx="52" cy="50" r="17"/><path d="m65 63 15 15M47 46a5 5 0 0 1 10 0c0 4-5 3-5 7m0 5v1"/></g><circle cx="34" cy="75" r="2" class="pulse"/>'),
}

CARD_COLORS = {
    "dark": dict(violet="#C4ADFF", blue="#8CC9F5"),
    "light": dict(violet="#7150A6", blue="#24618C"),
}

COOKIE_CASE = Template('''<svg xmlns="http://www.w3.org/2000/svg" width="560" height="168" viewBox="0 0 560 168" role="img" aria-labelledby="title desc">
  <title id="title">The case of the impossible cookie</title>
  <desc id="desc">An illustrated puzzle, not live data. Mina and Rafi each order the last cookie. Both orders are confirmed. How did one cookie sell twice?</desc>
  <style>
    text { font-family:'Segoe UI',Helvetica,Arial,sans-serif; }
    .left { animation:left 3s ease-in-out infinite; }
    .right { animation:right 3s ease-in-out infinite; }
    .cookie { transform-origin:280px 61px; animation:wobble 5s ease-in-out infinite; }
    @keyframes left { 0%,15% { transform:translateX(0); opacity:0; } 25% { opacity:1; } 75% { opacity:1; } 90%,100% { transform:translateX(52px); opacity:0; } }
    @keyframes right { 0%,15% { transform:translateX(0); opacity:0; } 25% { opacity:1; } 75% { opacity:1; } 90%,100% { transform:translateX(-52px); opacity:0; } }
    @keyframes wobble { 0%,100% { transform:rotate(-8deg); } 50% { transform:rotate(8deg); } }
    @media(prefers-reduced-motion:reduce) { * { animation:none !important; } }
  </style>
  <rect x="1" y="1" width="558" height="166" rx="16" fill="$bg" stroke="$line"/>
  <rect x="18" y="29" width="152" height="106" rx="12" fill="$panel" stroke="$line"/>
  <rect x="390" y="29" width="152" height="106" rx="12" fill="$panel" stroke="$line"/>
  <g text-anchor="middle">
    <text x="94" y="59" font-size="22" font-weight="650" fill="$ink">Mina</text>
    <text x="466" y="59" font-size="22" font-weight="650" fill="$ink">Rafi</text>
    <text x="94" y="84" font-size="15" fill="$muted">ORDER #001</text>
    <text x="466" y="84" font-size="15" fill="$muted">ORDER #002</text>
    <text x="94" y="114" font-size="17" font-weight="600" fill="$accent">✓ Confirmed</text>
    <text x="466" y="114" font-size="17" font-weight="600" fill="$accent">✓ Confirmed</text>
  </g>
  <path d="M179 63h51m-7-5 7 5-7 5m158-5h-51m7-5-7 5 7 5" fill="none" stroke="$muted" stroke-width="1.5"/>
  <circle class="left" cx="177" cy="63" r="3" fill="$accent"/>
  <circle class="right" cx="383" cy="63" r="3" fill="$accent"/>
  <g class="cookie">
    <circle cx="280" cy="61" r="27" fill="$warm" fill-opacity=".22" stroke="$warm" stroke-width="2"/>
    <g fill="$warm"><circle cx="270" cy="50" r="3"/><circle cx="290" cy="54" r="4"/><circle cx="281" cy="69" r="3"/><circle cx="265" cy="66" r="2"/><circle cx="293" cy="74" r="2"/></g>
  </g>
  <text x="280" y="110" text-anchor="middle" font-size="20" font-weight="650" fill="$warm">1 cookie</text>
  <text x="280" y="140" text-anchor="middle" font-size="14" fill="$muted">2 promises. Hmm.</text>
</svg>
''')


def main():
    ASSETS.mkdir(exist_ok=True)
    for theme, colors in THEMES.items():
        for name, template in (("banner", BANNER), ("desk-notes", NOTES), ("cookie-case", COOKIE_CASE)):
            path = ASSETS / f"{name}-{theme}.svg"
            path.write_text(template.substitute(colors), encoding="utf-8", newline="\n")
            print(f"Generated {path.name}")
        for name, data in CARDS.items():
            accent = {**colors, **CARD_COLORS[theme]}[data["color"]]
            values = dict(colors, title=escape(data["title"]), subtitle=escape(data["subtitle"]),
                          card_accent=accent, icon=data["icon"].replace("$card_accent", accent))
            path = ASSETS / f"card-{name}-{theme}.svg"
            path.write_text(CARD.substitute(values), encoding="utf-8", newline="\n")
            print(f"Generated {path.name}")


if __name__ == "__main__":
    main()
