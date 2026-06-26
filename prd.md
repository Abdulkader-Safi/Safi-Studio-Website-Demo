# Safi Studio landing page, PRD

> The contract for what we build. Strategy and reasoning live in strategy.md.
> Status: draft, awaiting Safi's sign-off. No design work starts until this is approved.

## Problem

Safi has the parts of a dev-tools business (a live open-source component system, editor plugins, senior Laravel skill) but no single brand that sells them. He bought safi-studio.com to fix that. The site needs to convert Laravel agencies into buyers of his tools and his tooling services, while pulling solo developers in through free open-source work.

The trap to avoid: a "stuff I made" portfolio that lists unrelated tools and sells nothing. The site must read as a real product-and-services business with one clear buyer.

## Who it's for

- Primary: small-to-mid Laravel-focused web/app agencies, and the senior devs who pick their tools.
- Secondary: individual Laravel developers who adopt the free tools and feed the funnel.
- Messaging leads at agencies.

## Success criteria (concrete, testable)

1. A first-time agency visitor can state, within five seconds, that this is a Laravel dev-tools studio selling both products and services.
2. The page shows at least one real product (LaralCN-UI) with a real screenshot, not an icon row.
3. Services are named and scoped clearly enough that a buyer self-selects an offer and hits one primary CTA (book / enquire).
4. Free tools are visible and reachable so a solo dev can enter without talking to anyone.
5. The design passes the design-rules.md self-check (own brand, no AI-slop tells: no purple gradient, not Inter-only, no glow/lights, real content not lorem, contrast passes AA).
6. Desktop and mobile both designed, consistent type and spacing scale across both.

## Scope

### In (v1)
- Full positioning and offer strategy (done in strategy.md, confirmed at sign-off).
- A defined service catalogue: named, productized offers with scope and pricing logic.
- One landing page, designed in Pencil: desktop (1440px) and mobile (390px).
- Sections (draft, finalised at sign-off): nav with the Safi Studio mark, hero (clear positioning + primary CTA), proof strip (real products / logos / download or star counts if real), products section (LaralCN-UI lead + free tools), services section (named offers, "from" pricing or enquiry), a why-me / credibility block (senior Laravel, open-source proof, dual-market), a single enquiry CTA band, footer.
- Real copy throughout, written to writing-rules.md. No lorem, no placeholder offers.

### Out (v1)
- No code build. This is strategy + design only, same pattern as the other Pencil projects.
- No live pricing engine, checkout, or auth.
- No blog, docs site, or multi-page site. One landing page.
- No new product gets built here. We feature what exists; roadmap items are labelled as such or left off.
- Not the dark-terminal social theme. This brand is decided fresh at design time.

## Constraints

- Design in Pencil (.pen), Safi's tool for this. Design only, no HTML/Tailwind output unless he asks later.
- Must follow design-rules.md (anti-AI-slop) and writing-rules.md (copy).
- Brand is a solo indie-dev brand, distinct from dsrpt and abdulkadersafi.com.
- Only feature real, shippable tools. No promising products that don't exist.
- Solo operator: services scope must be deliverable by one senior engineer, so productized and bounded, not open-ended.

## Plan

1. Sign-off on strategy.md + this PRD, and answers to the open questions below. (gate)
2. Finalise the service catalogue (names, scope, pricing logic) into services.md.
3. Decide the brand direction for the page: palette, type pairing, one repeated layout primitive (per design-rules.md). Show Safi the direction before full build.
4. Build the Pencil landing page, desktop first, then mobile, with real copy.
5. Review against both rule files, check a run of screens together for consistency, fix the named tells.
6. Update Projects/index.md, about-me.md headline list, and memory.md.

## Open questions (must resolve before build)

1. Is "Safi Studio" the final brand name, or do you want a less personal product name?
2. Real "from" prices on the site, or "contact for quote"? (My lean: show "from" prices.)
3. Is there a real paid product (LaralCN-UI Pro / a tier) today, or is that roadmap?
4. Are you taking services work through Safi Studio now, or is v1 product-led with services "coming"?
5. Target globally, or lead with Australia + GCC like dsrpt?
6. Which specific plugins/packages are real and shippable today, so we feature real names?

## Decisions locked (from the kickoff)

- Sells both products and services; services are the revenue engine.
- Agency-led messaging, solo devs as secondary funnel.
- Safi Studio is a solo indie-dev brand, separate from dsrpt and the portfolio.
- v1 = full strategy + landing page design (Pencil), no code.
