#!/usr/bin/env python3
"""Safi Studio logo — constructed bracket-framed S mark. Outputs SVGs + a brand sheet PNG."""
import cairosvg, os

OUT = os.path.dirname(os.path.abspath(__file__))

PAPER = "#F4F1EA"
PANEL = "#EDE8DD"
INK   = "#1A1815"
CLAY  = "#E5533D"
MUTED = "#5A554C"
LINE  = "#D9D2C4"

# ----- the mark, drawn in a 100x100 viewBox, parameterised by colors -----
def mark(ink, accent, frame, bg=None, square=True):
    """A constructed S framed by two brackets, inside a hairline square.
    ink   = stroke colour of the S
    accent= bracket colour (the one point of heat)
    frame = hairline square colour
    bg    = optional fill behind the square
    """
    sw = 9          # S stroke weight
    bg_rect = f'<rect x="2" y="2" width="96" height="96" rx="2" fill="{bg}"/>' if bg else ''
    sq = f'<rect x="2" y="2" width="96" height="96" rx="2" fill="none" stroke="{frame}" stroke-width="2.4"/>' if square else ''
    # Constructed S: three horizontal bars + two connecting verticals, cut corners (no curves)
    # geometry tuned within ~30..70 x, 26..74 y
    s = f'''
      <g fill="{ink}">
        <!-- top bar -->
        <rect x="34" y="28" width="32" height="9"/>
        <!-- upper-left vertical -->
        <rect x="34" y="33" width="9" height="20"/>
        <!-- middle bar -->
        <rect x="34" y="46" width="32" height="9"/>
        <!-- lower-right vertical -->
        <rect x="57" y="49" width="9" height="20"/>
        <!-- bottom bar -->
        <rect x="34" y="63" width="32" height="9"/>
      </g>'''
    # Brackets framing the S (the accent, the prompt)
    bl = f'''
      <g fill="{accent}">
        <rect x="21" y="27" width="6.5" height="46"/>
        <rect x="21" y="27" width="12" height="6.5"/>
        <rect x="21" y="66.5" width="12" height="6.5"/>
      </g>'''
    br = f'''
      <g fill="{accent}">
        <rect x="72.5" y="27" width="6.5" height="46"/>
        <rect x="67" y="27" width="12" height="6.5"/>
        <rect x="67" y="66.5" width="12" height="6.5"/>
      </g>'''
    return f'<g>{bg_rect}{sq}{s}{bl}{br}</g>'

def mark_svg(ink, accent, frame, bg=None, square=True, size=240):
    inner = mark(ink, accent, frame, bg, square)
    if not square:
        # frameless: crop the viewBox tight to the mark's bounds (x21..79, y27..73) with a small even margin
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="18 24 64 52" width="{size}" height="{int(size*52/64)}">{inner}</svg>'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="{size}" height="{size}">{inner}</svg>'''

# ---- standalone mark SVGs (no square frame, bracket+S only) ----
variants = {
    "mark-primary.svg":   mark_svg(INK, CLAY, INK, bg=None, square=False),    # ink S, clay brackets, transparent
    "mark-dark.svg":      mark_svg(PAPER, CLAY, PAPER, bg=None, square=False), # paper S, clay brackets, transparent (for dark)
    "mark-mono-ink.svg":  mark_svg(INK, INK, INK, bg=None, square=False),     # single colour ink
    "mark-mono-paper.svg":mark_svg(PAPER, PAPER, PAPER, bg=None, square=False),# single colour paper
}
for name, svg in variants.items():
    open(os.path.join(OUT, name), "w").write(svg)
    cairosvg.svg2png(bytestring=svg.encode(), write_to=os.path.join(OUT, name.replace(".svg","@1024.png")),
                     output_width=1024, output_height=1024)

print("standalone marks written:", list(variants))

# ---- fonts ----
FONTS = "/sessions/serene-great-franklin/mnt/.claude/skills/canvas-design/canvas-fonts"
font_face = f'''
  @font-face {{ font-family:'Disp'; src:url('file://{FONTS}/BricolageGrotesque-Bold.ttf'); }}
  @font-face {{ font-family:'DispR'; src:url('file://{FONTS}/BricolageGrotesque-Regular.ttf'); }}
  @font-face {{ font-family:'Mono'; src:url('file://{FONTS}/JetBrainsMono-Regular.ttf'); }}
  @font-face {{ font-family:'MonoB'; src:url('file://{FONTS}/JetBrainsMono-Bold.ttf'); }}
'''

def lockup_horizontal(markfn_inner, text_ink, accent, tag_color):
    """mark + wordmark on one baseline, in a 760x200 frame."""
    return f'''
      <g transform="translate(30,40)"><g transform="scale(1.2)">{markfn_inner}</g></g>
      <text x="190" y="103" font-family="Disp" font-size="62" letter-spacing="-1.5" fill="{text_ink}">Safi Studio</text>
      <text x="193" y="138" font-family="Mono" font-size="19" letter-spacing="3" fill="{tag_color}">DEV TOOLS // BUILDS</text>
    '''

# ===== BRAND SHEET (1600 x 2000) =====
W, H = 1600, 2000
# frameless marks for the sheet (centred + enlarged group)
def frameless(ink, accent):
    return f'<g transform="translate(50,50) scale(1.42) translate(-50,-50)">{mark(ink, accent, ink, bg=None, square=False)}</g>'
m_primary = frameless(INK, CLAY)
m_dark    = frameless(PAPER, CLAY)
m_ink_only= frameless(INK, INK)

def place_mark(inner, x, y, scale):
    return f'<g transform="translate({x},{y}) scale({scale})">{inner}</g>'

sheet = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs><style>{font_face}</style></defs>
<rect width="{W}" height="{H}" fill="{PAPER}"/>

<!-- header -->
<text x="90" y="130" font-family="Mono" font-size="22" letter-spacing="6" fill="{MUTED}">SAFI STUDIO</text>
<text x="90" y="200" font-family="Disp" font-size="78" letter-spacing="-2" fill="{INK}">Brand mark</text>
<line x1="90" y1="250" x2="{W-90}" y2="250" stroke="{LINE}" stroke-width="2"/>
<text x="90" y="290" font-family="Mono" font-size="18" letter-spacing="2" fill="{MUTED}">[ S ]  —  copy-and-own. you hold the S.</text>

<!-- hero primary mark -->
{place_mark(m_primary, 90, 360, 4.0)}
<rect x="490" y="360" width="{W-90-490}" height="400" fill="{PANEL}"/>
{place_mark(m_primary, 540, 380, 3.6)}
<text x="900" y="500" font-family="Disp" font-size="46" letter-spacing="-1" fill="{INK}">The mark</text>
<text x="900" y="545" font-family="DispR" font-size="22" fill="{MUTED}">A constructed S, framed by two brackets,</text>
<text x="900" y="577" font-family="DispR" font-size="22" fill="{MUTED}">held in a hairline square. Sharp 2px corners.</text>
<text x="900" y="609" font-family="DispR" font-size="22" fill="{MUTED}">One accent of clay, used once.</text>
<text x="900" y="690" font-family="Mono" font-size="16" letter-spacing="1" fill="{CLAY}">#E5533D  ·  clay accent</text>
<text x="900" y="720" font-family="Mono" font-size="16" letter-spacing="1" fill="{INK}">#1A1815  ·  ink</text>

<!-- horizontal lockups: light + dark -->
<line x1="90" y1="820" x2="{W-90}" y2="820" stroke="{LINE}" stroke-width="2"/>
<text x="90" y="870" font-family="Mono" font-size="18" letter-spacing="3" fill="{MUTED}">LOCKUP</text>

<g transform="translate(90,900)">{lockup_horizontal(m_primary, INK, CLAY, MUTED)}</g>

<rect x="90" y="1120" width="{W-180}" height="210" fill="{INK}"/>
<g transform="translate(90,1130)">{lockup_horizontal(m_dark, PAPER, CLAY, '#A8A296')}</g>

<!-- favicon / scale row -->
<line x1="90" y1="1400" x2="{W-90}" y2="1400" stroke="{LINE}" stroke-width="2"/>
<text x="90" y="1450" font-family="Mono" font-size="18" letter-spacing="3" fill="{MUTED}">HOLDS AT ANY SIZE</text>
{place_mark(m_primary, 90, 1490, 2.2)}
{place_mark(m_primary, 360, 1490, 1.4)}
{place_mark(m_primary, 560, 1490, 0.85)}
{place_mark(m_primary, 700, 1490, 0.5)}
<rect x="90" y="1490" width="220" height="220" fill="none" stroke="{LINE}" stroke-width="1.5"/>
<text x="800" y="1560" font-family="DispR" font-size="22" fill="{MUTED}">216px · 88px · 64px · 32px — the strokes</text>
<text x="800" y="1592" font-family="DispR" font-size="22" fill="{MUTED}">keep their weight down to the favicon.</text>

<!-- single colour / reversed -->
<line x1="90" y1="1760" x2="{W-90}" y2="1760" stroke="{LINE}" stroke-width="2"/>
<text x="90" y="1810" font-family="Mono" font-size="18" letter-spacing="3" fill="{MUTED}">ONE COLOUR</text>
<rect x="90" y="1840" width="200" height="120" fill="none"/>
{place_mark(m_ink_only, 110, 1850, 1.0)}
<rect x="360" y="1840" width="200" height="120" fill="{INK}"/>
{place_mark(mark(PAPER, PAPER, PAPER, bg=None), 380, 1850, 1.0)}
<rect x="630" y="1840" width="200" height="120" fill="{CLAY}"/>
{place_mark(mark(PAPER, PAPER, PAPER, bg=None), 650, 1850, 1.0)}

<text x="{W-90}" y="1950" text-anchor="end" font-family="Mono" font-size="15" letter-spacing="2" fill="{MUTED}">safi-studio.com</text>
</svg>'''

open(os.path.join(OUT, "brand-sheet.svg"), "w").write(sheet)
cairosvg.svg2png(bytestring=sheet.encode(), write_to=os.path.join(OUT, "safi-studio-logo-sheet.png"),
                 output_width=1600, output_height=2000)

# ---- a clean horizontal lockup as its own asset (transparent) ----
lock = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 200" width="780" height="200">
<defs><style>{font_face}</style></defs>
<g transform="translate(10,30)">{lockup_horizontal(mark(INK, CLAY, INK, bg=PAPER), INK, CLAY, MUTED)}</g>
</svg>'''
open(os.path.join(OUT, "lockup-horizontal.svg"), "w").write(lock)
cairosvg.svg2png(bytestring=lock.encode(), write_to=os.path.join(OUT, "lockup-horizontal@2x.png"),
                 output_width=1560, output_height=400)

# favicon: tight square crop (mark spans x21..79 w58, y27..73 h46; centre in a 64x64 square box -> x18..82, y23..73 wait)
# centre the 58x46 mark in a 64-square: x from (21-3)=18..82 gives 64 wide; y centred: 50 +/-32 = 18..82
fav = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="18 18 64 64" width="512" height="512">{mark(INK, CLAY, INK, bg=None, square=False)}</svg>'''
open(os.path.join(OUT, "favicon.svg"), "w").write(fav)
cairosvg.svg2png(bytestring=fav.encode(), write_to=os.path.join(OUT, "favicon@512.png"), output_width=512, output_height=512)

print("sheet + lockup + favicon written")
