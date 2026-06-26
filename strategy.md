# Safi Studio strategy

> The positioning, offers, and pricing logic for safi-studio.com.
> This is the thinking behind the build. The PRD (prd.md) is the contract for what we ship.
> Status: draft, awaiting Safi's sign-off.

## The one-line pitch

Safi Studio is where a senior Laravel engineer ships the tools agencies wish they had time to build, then builds the custom ones they don't.

## The honest problem with the brief, and the fix

The starting idea was "sell developer tools for agencies" with three things in hand: LaralCN-UI, Obsidian plugins, and VSCode plugins. Those three don't sell to one buyer. A Laravel agency that wants a component system has no use for your Obsidian plugin, and an Obsidian power-user isn't your agency client. A site that lists all three as equal products reads as a personal "stuff I made" page, not a business.

The fix is to pick one buyer and one spine, and let the rest hang off it as proof. Your strongest, most commercial asset is LaralCN-UI: a copy-and-own Blade component system, already live, already in the Laravel ecosystem where you have credibility. That is the spine. Everything else (the plugins, the packages) becomes evidence that you build real tools, not slideware.

So: **Safi Studio is a Laravel-first dev-tools studio.** Agency-led. Products prove it, services pay for it.

## Who it sells to

Primary buyer: **small-to-mid web/app agencies that live in Laravel** (and the senior devs inside them who choose the tools). They ship client sites and apps on a deadline, they reinvent the same UI and the same internal tooling on every project, and they don't have a spare engineer to build a proper component system or a custom admin tool. That is the gap you fill.

Secondary buyer: **individual Laravel developers** who adopt your open-source tools for their own workflow. They cost you nothing to serve, they become the top of the funnel, and some of them are the people inside the agencies who later hire you.

Lead the messaging at agencies. Keep the door open for solo devs through the free tools.

## The model: open core, paid edge, services for the deep work

This is the Spatie pattern, proven over a decade in exactly your ecosystem: free open-source packages downloaded a billion times act as the trust engine, then paid products (Mailcoach, Flare, courses) and web-dev services carry the revenue. You apply the same shape at your scale.

There's a sharp lesson in how NOT to price it. Tailwind Labs sold its UI kit as a one-time $299 payment, built a great funnel off free docs, and in 2026 reportedly lost about 80% of revenue when AI severed the docs-to-sales link and the one-time model left no recurring floor. The takeaway for Safi Studio: don't bet the business on one-time license sales, and don't build a funnel that an LLM can quietly replace. Recurring (support, updates, retainers) and services (which AI can't deliver end-to-end) are the durable parts.

Three layers:

**1. Free / open (the proof and the funnel).**
LaralCN-UI core, your open Obsidian and VSCode plugins, free Blade blocks. MIT, copy-and-own, no lock-in. Job: get developers using your work, rank in search, build trust. These don't make money directly. They make the rest credible.

**2. Paid products (recurring where possible).**
The pro edge on top of the free core. Examples to define properly with you: a LaralCN-UI Pro tier (premium blocks, app templates, dashboard kits, priority updates), agency licenses, ready-made starter kits. Price for a recurring or renewable floor, not a single lifetime sale. A team/agency license that renews annually beats a one-time purchase.

**3. Services (the revenue engine, agency-led).**
This is where the money is and where you're hardest to replace. Productized, named, fixed-scope offers so an agency can buy without a long sales cycle:
- **Component system build** — a custom Blade/Tailwind component library for an agency's stack, the LaralCN approach applied to their brand and their repeated needs.
- **Internal tool / admin build** — the custom dashboard, CMS, or internal tool they keep meaning to build. (Market rate for a simple internal tool runs $30k to $150k for custom software; your productized version undercuts that with a fixed scope.)
- **Plugin / package build** — a VSCode, Obsidian, or Laravel package built to spec for a team's workflow.
- **Tooling retainer** — ongoing: you maintain and extend their component system and internal tools. This is the recurring service revenue that survives AI.

Products are the storefront window. Services are the till.

## Why this is hard to copy

Three things stack into a moat: you're a named senior Laravel engineer with live open-source proof (LaralCN-UI), you sit across both the Australian and GCC markets through dsrpt, and you ship tools across the whole stack (web components, editor plugins, packages) rather than one narrow thing. The open-source work is the part competitors can't fake. It's already built and already public.

## Brand relationship (decided)

Safi Studio is **your solo indie-dev brand**. It's you, by name. dsrpt is the day job and the agency; abdulkadersafi.com is the personal portfolio and blog. Safi Studio is the place your own products and your tooling services live, under their own roof. Keep it visually and verbally distinct from both so it reads as a real product brand, not a second portfolio.

One thing to watch: the personal portfolio (abdulkadersafi.com) and Safi Studio will overlap, both are "you, selling your work." Keep the line clean: portfolio is the CV and the writing; Safi Studio is the products and the productized tooling services. Different jobs, different sites.

## What the landing page has to do

In order of priority:
1. Make an agency lead understand in five seconds: Laravel dev-tools studio, products and services.
2. Show real proof immediately (LaralCN-UI live, real plugins, real screenshots, not icon rows).
3. Name the services clearly enough that a buyer can self-select and enquire.
4. Give the free tools room so solo devs enter the funnel.
5. One clear primary action: book / enquire about a build.

Per design-rules.md, this gets its own brand and its own point of view. Not the dark-terminal social theme (that's social-only), not a generic SaaS template. Real product screenshots over icon grids. We decide the actual palette and type at design time.

## Open questions for Safi (need answers before/at PRD sign-off)

1. **Name confirm:** is "Safi Studio" final, or do you want a less personal product name (the site is safi-studio.com either way)?
2. **Pricing:** do you want real prices on the site (productized, "from $X"), or "contact for quote"? My lean: show "from" prices on services to filter buyers and signal you're a real shop.
3. **Paid product reality:** is there an actual LaralCN-UI Pro / paid tier today, or is that a roadmap item? The site shouldn't promise a product that doesn't exist yet.
4. **Services capacity:** are you taking client work through Safi Studio now (solo, alongside dsrpt), or is v1 mainly about products with services "coming"? This changes how hard the page pushes the enquiry.
5. **GCC vs global:** target globally, or lead with Australia + GCC like dsrpt?
6. **Plugins scope:** which specific plugins are real and shippable today (names), so we feature real ones, not placeholders?
