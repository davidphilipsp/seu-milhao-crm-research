# Seu Milhão · CRM and market research

Product research, a living PRD and CRM UX decisions for **Seu Milhão**, a SUSEP-regulated philanthropic
sweepstakes brand in Brazil (a *título de capitalização*: pay by Pix, receive a numbered title, and the
draw follows the Federal Lottery). The documents are in Brazilian Portuguese. This README is the English entry point.

> **Public, sanitized copy.** Business numbers (prices, prizes, costs, LTV, conversion, counts), quotes from
> private chats and meetings, names of real people, vendors and partners, private board links and raw scraped
> artifacts were removed or replaced with markers such as `[valor]`, `[n]`, `[x%]` or a role.
> Two PRD sections that depended on confidential third-party information are omitted.

## What is here

| Path | What it is |
|---|---|
| [`PRD.md`](PRD.md) | Living PRD: a knowledge hub that turns every gap into a research question tied to a pending decision |
| [`crm-ux/01-DECISOES-TRAVADAS.md`](crm-ux/01-DECISOES-TRAVADAS.md) | Locked CRM product decisions |
| [`crm-ux/02-VISUAL-BRIEFING.md`](crm-ux/02-VISUAL-BRIEFING.md) | Step-by-step log of the UX artifacts (IA, flows, wireframes) and their approvals |
| [`research/`](research/) | Market research: ad libraries, short-form direct sales, regulation, players, complaints, promotion cadence |
| [`docs/research/`](docs/research/) | Follow-up research: raffle money flows, AI-generated video ads on Meta |
| [`tools/speech-metrics/`](tools/speech-metrics/) | Small scripts for presenter speech analysis (pace, pauses, pitch, emphasis) |

## Method: evidence tags

Every claim that matters carries a tag:
- **[E] documented**: primary source read directly and quotable.
- **[C] consensus**: a pattern repeated across several sources, with no single source.
- **[I] inference**: plausible, not directly observed.

Other rules: a number self-reported by a third party is never plain [E]. The PRD shrinks its backlog only by
answering questions, never by dropping them. Every open question names the decision it unblocks and the source
that raised it, with priority P0/P1/P2. Questions that are cheap to check come before expensive ones.

## CRM UX decisions (summary)

- **Build, not buy.** An in-house CRM for segmentation, orchestration, sending and assets. WhatsApp is the primary
  channel through a BSP. SMS, voice and email are support channels. Single brand. Web only, so no push or in-app inbox.
- **North-star metric:** first-time buyers per draw cycle, with a defined set of core and diagnostic metrics
  (Pix conversion and recovery, repurchase after the draw, prize-payment SLA, opt-in, WhatsApp quality, compliance
  blocks, tracking discrepancy, refunds, complaints).
- **Data model:** cycle-first navigation and entity-first data. The customer key is the CPF (Brazilian taxpayer ID);
  pre-purchase leads stay provisional. The **Order is the financial aggregate root** (one Pix = one order = one state
  machine) and the **Title is the legal child entity** (one paid order → N titles). An **append-only event store**
  feeds everything; RFM, value score and LTV are rebuilt in a nightly batch. Unpaid-Pix recovery is real-time.
- **Compliance as a rail, not a wall.** Sends to non-opt-in, minors or off-hours show an explicit warning instead
  of a hard block. The event store is the permanent audit log.
- **Economics in the interface:** a cost/margin panel next to the send button shows projected cost, break-even
  conversion and expected margin as a traffic light. It warns and does not block.
- **WhatsApp rule:** almost everything is a pre-approved template triggered by backend events. Pix recovery and
  title confirmation are *Utility*; campaigns are *Marketing* (frequency-capped). There is a dedicated
  template-status screen, and quality is tracked per number.
- **Day-1 journeys:** Pix generated but unpaid → recovery; title confirmation; draw result → winner / non-winner →
  repurchase. Acquisition comes from scheduled campaigns, not journeys.
- **Information architecture, 6 areas:** Home · Customers · Segments · Campaigns · Journeys · Templates. The draw
  console and the Pix monitor became contextual overlays opened from the Home cards and alerts.
- **Segmentation:** visual builder with a "view as SQL" toggle, a live counter, and CSV import/export through the
  compliance rail.
- **Out of scope for v1:** the scratch-card mechanic, gamification, push/inbox, dedicated LGPD screen (handled
  manually and logged as residual risk).

## Research topics

- Meta Ad Library: ad format taxonomy, script skeletons and creative persistence in the Brazilian sweepstakes niche.
  The whitespace found was **mechanism transparency** (Federal Lottery / SUSEP).
- TikTok Creative Center (Brazil): summarized in the PRD only. The report is not published because it was collected with browser automation.
- Short-form direct sales for low-ticket offers to Brazilian C/D classes: a 9-layer operating system from offer to
  iteration, angle discovery and percentile-based kill/keep/scale decisions.
- Capitalization players and business models, and SUSEP regulation of capitalization titles.
- Public consumer complaints (ReclameAqui) about the sector.
- Promotion cadence, angles and channels.
- Raffle money flows, and AI-generated video ads on Meta.

## Not included

Chat exports, meeting notes, spreadsheets/CSV, screenshots and raw JSON from research sessions, videos, audio and
transcripts, a capture brief of a third-party CRM tenant, and any scraping tool. Do not use this repository as a
source of market numbers. The markers stand for values that were removed on purpose.

> Built with Claude Code as a pair programmer.
