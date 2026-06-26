# Safi Studio brand guidelines

> The rules the website and the logo follow. One source of truth for colour, type, the mark, and voice.
> If you build anything new for Safi Studio, match this. The philosophy behind the mark is in `logo-philosophy.md`.

## The idea in one line

Safi Studio looks like the command line made warm. Terminal precision (brackets, mono, sharp corners) on a paper-and-ink ground, with a single clay accent used sparingly. The mark says the whole pitch: `[ S ]`, copy-and-own, you hold the S.

---

## Logo

The mark is a constructed S framed by two brackets, held in a hairline square with sharp 2px corners. The brackets are the one point of heat, in clay. Never redraw the S from a font: it's built from straight strokes on purpose.

### Logo variants and when to use each

| Variant | File | Use it for | Background |
|---|---|---|---|
| Primary mark | `mark-primary.svg` / `mark-primary@1024.png` | Default. Nav, favicon, anywhere on light | Paper `#F4F1EA` |
| Dark mark | `mark-dark.svg` / `mark-dark@1024.png` | On the ink footer, dark sections, dark social | Ink `#1A1815` |
| Mono ink | `mark-mono-ink.svg` | One-colour print, stamps, watermarks, faxable docs | Light, transparent |
| Mono reversed | `mark-mono-paper.svg` | One-colour on dark, embossing, single-ink reversed | Dark |
| Horizontal lockup | `lockup-horizontal.svg` / `@2x.png` | Headers, email signature, slide title, partner decks | Light |
| Favicon | `favicon@512.png` / `mark-primary.svg` | Browser tab, app icon, social avatar | Any |
| Full brand sheet | `safi-studio-logo-sheet.png` | Reference only, the spec sheet. Not for embedding | Paper |

### Logo rules

| Rule | Detail |
|---|---|
| Minimum size | Mark works down to 32px (favicon). Don't go smaller. |
| Clear space | Keep padding around the mark equal to the height of one bracket arm. Nothing crowds it. |
| Accent | The brackets are clay. The S is ink (or paper on dark). Never recolour the S to clay. |
| Corners | Always 2px sharp. Never round the square into a soft app-icon radius. |
| Don't | Don't add gradients, glows, or shadows to the mark. Don't stretch it. Don't put it on a busy photo. Don't swap the fonts in the wordmark. |
| Wordmark | "Safi Studio" in the display font. Tagline `DEV TOOLS // BUILDS` in mono, all-caps, letter-spaced. |

---

## Colour

The palette is warm and deliberate, not the cold blue of a default tech brand. Clay is the only accent and it's used once per view, on the thing that matters.

### Core tokens

| Token    | Hex       | Role                        | Notes                                                   |
| -------- | --------- | --------------------------- | ------------------------------------------------------- |
| Paper    | `#F4F1EA` | Page background             | The warm bone ground. Default canvas.                   |
| Panel    | `#EDE8DD` | Raised surface              | Slightly darker paper for bands and cards.              |
| Ink      | `#1A1815` | Primary text, dark sections | Near-black, warm. Body and headings on light.           |
| Muted    | `#5A554C` | Secondary text              | Captions, labels, supporting copy.                      |
| Line     | `#D9D2C4` | Hairline borders            | Dividers, card outlines.                                |
| Clay     | `#E5533D` | Accent, CTAs                | The one warm signal. Buttons, brackets, links-on-hover. |
| Clay ink | `#C23E2A` | Accent hover/active         | Darker clay for hover states and small accent text.     |
| Moss     | `#3F6F4E` | Success / "free / live"     | Rare. Tags like "Live · free · MIT", form success.      |

### Contrast (WCAG)

| Pairing | Ratio | Passes |
|---|---|---|
| Ink on Paper | ~13:1 | AA + AAA |
| Muted on Paper | ~5.3:1 | AA |
| Paper on Ink | ~13:1 | AA + AAA |
| Clay on Paper | ~3.6:1 | AA for large/UI only, not body text |

Rule: clay is for buttons, accents, and large text, never for paragraph body copy. Body text is ink or muted.

---

## Type

Two typefaces do all the work, plus a mono for the terminal motif. No third font.

| Role | Font (web) | Canvas/asset equivalent | Used for |
|---|---|---|---|
| Display | Space Grotesk | Bricolage Grotesque | Headlines, the wordmark, section titles |
| Body | Inter | Inter | Paragraphs, UI labels, buttons |
| Mono | JetBrains Mono / system mono | JetBrains Mono | Code, terminal windows, eyebrow tags, the logo tagline |

### Type rules

| Rule | Detail |
|---|---|
| Headings | Display font, tight tracking (`-1` to `-2`), sentence case. Never title case. |
| Body | Inter, 16 to 18px, line-height ~1.7. |
| Eyebrows / tags | Mono, all-caps, letter-spaced. Used sparingly, calm spacing, never crammed against the heading. |
| Weight | Bold for display, regular/medium for body. Don't bold every other phrase. |
| Mono | Reserve for code, terminal mockups, and small labels. It carries the "developer" signal so it shouldn't be everywhere. |

---

## Layout and motion

| Element | Rule |
|---|---|
| Corner radius | 2px everywhere (`rounded-sharp`). One radius, committed. |
| The primitive | The signature block: hairline border, an index number (`01`, `02`), sharp corners, lifts on hover with a hard 6px offset shadow. Reuse this instead of inventing new card styles. |
| Borders | 1px hairline in Line `#D9D2C4`. Flat, no soft drop-shadows by default. |
| Container | Max width ~1152px (`max-w-6xl`), generous side padding. |
| Hover | Real response: lift + hard shadow on blocks, an animated clay underline on links. Easing, never a snap. |
| Spacing | Group related things tight, leave generous air between sections. Not one uniform gap everywhere. |
| Alignment | Left-aligned by default. Centre only when it's earned (the closing CTA). |

---

## Voice

Follows Safi's writing rules. Plain, direct, specific. Sounds like a senior engineer, not a marketing page.

| Do | Don't |
|---|---|
| "The dev tools your agency keeps meaning to build." | "Empowering teams with seamless, robust solutions." |
| Short sentences. Real numbers and concrete examples. | Three-item lists by reflex, puffed-up significance. |
| Say what something is, plainly. | Em-dashes, curly quotes, AI vocabulary. |
| One clear action per page. | Hedging, vague "experts say" claims. |

Tagline: **DEV TOOLS // BUILDS**. Positioning line: products prove it, services pay for it.

---

## Asset index

Everything lives in `Safi-Studio/brand/`.

| Asset | Format | Purpose |
|---|---|---|
| `mark-primary.svg` | SVG | Primary mark, also the favicon source |
| `mark-dark.svg` | SVG | Mark on dark |
| `mark-mono-ink.svg` | SVG | One-colour ink |
| `mark-mono-paper.svg` | SVG | One-colour reversed |
| `lockup-horizontal.svg` | SVG | Mark + wordmark + tagline |
| `favicon@512.png` | PNG | Favicon / avatar raster |
| `*@1024.png` | PNG | High-res raster of each mark |
| `safi-studio-logo-sheet.png` | PNG | The full reference sheet |
| `logo-philosophy.md` | MD | The thinking behind the mark |
| `build_logo.py` | PY | The generator. Edit + re-run to change the mark |

To change the mark (colours, proportions), edit `build_logo.py` and re-run it. It regenerates every SVG, PNG, and the sheet from one source.
