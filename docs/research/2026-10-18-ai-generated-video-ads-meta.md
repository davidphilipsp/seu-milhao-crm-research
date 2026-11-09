# AI-generated video ads at scale on Meta — research memo

> Versão pública sanitizada: números de negócio, nomes de pessoas, citações de fontes privadas e parceiros foram substituídos por marcadores ([valor], [n], [x%], papéis).

**Date:** 2026-10-18
**Question:** Which AI-generated ads (preferably video) are scaling hardest on Meta right now, and what can we learn from them?
**Method:** ~30 web searches + source fetches across trade press (Fortune, Marketing Brew, Digiday, Ad Age, NPR, Reuters coverage), platform announcements (Meta earnings, NewFronts, Advertising Week), ad-intelligence research (Motion Creative Benchmarks 2026, Taboola/academic study, IAB AI Ad Gap), vendor material (Arcads, Creatify, HeyGen, Shuttlerock), and Brazilian press (Tecnoblog, E-Commerce Brasil, Agência Lupa).

> **Important caveat up front:** no public dataset ranks Meta ads by spend *and* flags them as AI-generated. Meta's Ad Library exposes spend ranges only for political/social-issue ads in most countries, and the "AI info" label is not a filterable field. Everything below is therefore triangulated from investigations, platform disclosures, research reports and vendor claims. Vendor numbers are flagged as such.

---

## 1. Executive summary

1. **The single biggest documented case of AI video ads at scale on Meta is Temu's "partnership ads" network in Europe.** Research by the Czech non-profit Online Risk Labs (reported by Fortune, 31 Aug 2026) found Temu ran 9M+ ads from 31 official pages in the UK + EU between Jan 2025 and Apr 2026, [x%] of them creator partnership ads, with estimated spend up to **US$ [valor]**. 73 of the top 100 "creators" are likely fake accounts; the top account (a creator-style page, name omitted) appeared in ~109,541 campaigns (~225/day) with 1B+ views and publishes what Fortune calls "AI slop" product videos. This is the clearest evidence that cheap AI-generated short video, pushed through creator-style placements, is being scaled at nine-figure budgets.
2. **The second biggest category is fraud.** Reuters (Nov 2025, internal Meta documents) reported Meta projected [x%] of 2024 revenue (~US$ [valor]) from scam/banned-goods ads and ~15B "higher-risk" scam ad impressions per day. A large share of these are deepfake video ads of celebrities and doctors. Brazil is a hotspot: in Feb 2026 Meta sued two Brazilian groups for deepfake ads of five Brazilian celebrities (a TV doctor, a physician-influencer, a singer, a TV presenter and an influencer); one defendant also sold a R$ [valor] course teaching the method. **This matters directly for Seu Milhão:** prize draws, "easy money" and financial products are the exact verticals these deepfake ads imitate, and Meta's enforcement is tightening in precisely our category.
3. **Among legitimate advertisers, the dominant scaled format is "AI UGC"**: a photoreal AI actor (Arcads, Creatify, HeyGen, Meta's own avatar tool) delivering a 15–45s selfie-style talking-head ad, 9:16, hook in the first 3 seconds, subtitles burned in, used primarily as a *testing layer* (10–15 hooks per concept), with winners sometimes reshot with real creators. Arcads alone reports 6,000+ clients and 100,000 assets/month; Meta reports 9M small businesses using at least one of its gen-AI creative tools (Q2 2026, up from 8M in Q1 and 4M in late 2025).
4. **Performance evidence is mixed and mostly vendor-sourced.** The best independent data (Taboola + Columbia/Harvard/TUM/CMU, Jan 2026, 500M+ impressions) shows AI ads at [x%] CTR vs [x%] human in raw data, but *parity* after controls. AI ads "that don't look AI" performed best; a large, clear human face was the key trust signal. Real creators still win on conversion/trust for high-consideration purchases; AI wins on cost (US$ [valor] per usable video vs US$ [valor] for a creator) and test velocity.
5. **The scaling mechanics are about volume, not the AI itself.** Motion's 2026 Creative Benchmarks (US$ [valor] Meta spend, 578k creatives) found only [x%] of creatives become winners and [x%] of spend goes to that [x%]. AI's real contribution is that it makes producing 50–300 variants per concept economically trivial.
6. **Regulatory headwind is real and dated.** Meta now expects disclosure of photoreal synthetic people in ads (auto-labels for its own tools / C2PA, manual toggle otherwise); Instagram began throttling reach of undisclosed AI-persona profiles on 31 Aug 2026; Brazilian consumer law (CDC) forbids presenting an avatar as a real customer testimonial; TSE rules require labelling manipulated content in 2026 election material.

---

## 2. The scaled players, by category

### 2.1 Mass-volume "AI slop" product video (marketplaces)

| Item | Detail | Source |
|---|---|---|
| Advertiser | Temu (UK + 27 EU countries) | Fortune / Online Risk Labs |
| Period | Jan 2025 – Apr 2026 (16 months) | same |
| Volume | 9M+ ads from 31 official pages; 134B cumulative reach | same |
| Format | Creator "partnership ads" = [x%] of ads, [x%] of reach (industry norm ≈[x%]) | same |
| Spend | up to US$ [valor] (estimated from impressions × avg cost per reach) | same |
| Creators | 100 accounts = [x%] of partnership ads (1.4M+ ads Jan–Apr 2026); 73/100 likely fake; 28 based in Russia, 19 in China; only 8 verified | same |
| Top account | creator-style page (name and handle omitted, [n] IG followers): ~109,541 campaigns, 1B+ views, obvious AI-generated product demo videos (e.g., shower-scrubber skit) | same |
| Status | ORL filed a DSA risk-assessment request; Meta and Temu declined comment; one outlet reports the network went quiet within days (single source) | Fortune, IBTimes, Gadget Review |

**Why it scales:** partnership ads borrow the creator's handle and social proof, bypass the "ad look", and the creative is nearly free to produce, so Temu can run hundreds of variants per day per account and let Andromeda/Advantage+ pick winners.

### 2.2 Deepfake / synthetic-spokesperson scam ads (the largest *dollar* category)

| Fact | Detail | Source |
|---|---|---|
| Scale | Meta internally projected [x%] of 2024 revenue (~US$ [valor]) from scam + banned-goods ads; ~15B "higher-risk" scam ad impressions/day (Dec 2024 doc); ~US$ [valor]/yr from the highest-risk bucket | Reuters (6 Nov 2025), via Social Media Today, MediaNama, PPC Land |
| Enforcement model | Advertisers banned only at [x%] fraud confidence; below that Meta charges *higher* rates as a deterrent | same |
| Meta's response | Disputes the [x%] as "rough and overly inclusive"; SEC reportedly examining Meta over financial-scam ads (Oct 2026) | same; IBTimes |
| Formats | Deepfake video of celebrities/doctors (a US talk-show host, a US billionaire investor, Australian TV doctors, an Israeli pathologist's class action) selling supplements, diabetes "cures", investment schemes | TODAY, ABC Australia, BMJ, Calcalist |
| **Brazil** | Feb 2026: Meta sued 2 companies + 4 individuals in Brazil. Deepfakes of five Brazilian celebrities (one identified by URB News). One defendant allegedly sold a R$ [valor] course on making fake celebrity ads. Agência Lupa had already debunked several deepfake ads of the same TV doctor and documents Meta ignoring victim reports. | Tecnoblog, URB News, Diário do Comércio, Agência Lupa |

**Relevance to Seu Milhão:** the highest-volume *illegitimate* AI video ads on Meta in Brazil sit in health, investment and prize/"money" promises. Any legitimate prize-draw advertiser using AI avatars will be pattern-matched against this cluster by Meta's classifiers and by users. Expect higher rejection rates and lower baseline trust; disclosure and a real, identifiable human face are mitigations, not optional.

### 2.3 "AI UGC" avatar ads (legitimate DTC, apps, infoproducts)

**Supply side (who makes them):**

| Tool | Scale / positioning | Cost | Source |
|---|---|---|---|
| Arcads | 6,000+ clients, 100,000 assets/month, >[x%] US users, 35+ languages, US$ [valor] seed (Dec 2025), ~US$ [valor] ARR | ~US$ [valor]/generation list; ~US$ [valor] per *usable* video after 3–4 failed takes; Trustpilot ≈2.8 | arcads.ai, GetLatka, Apogee, shhots |
| Creatify | Volume play: batch 5–10 variants per product URL, 300+ actors | ~US$ [valor]/video; free tier, paid from US$ [valor]/mo | Cometly, Rework |
| HeyGen | Cheapest talking-head (~US$ [valor] per 30s on US$ [valor] plan), 175+ languages, output looks more "corporate" than feed-native | — | shhots, HeyGen |
| Icon (founder-led) | Pivoted mid-2025 to "Human Admaker": sells 6 real human UGC ads for US$ [valor] alongside software; claims co-built with Ridge, Jones Road, Immi, Backbone, MUD\WTR (unverified) | — | Sacra, yespress, Icon YouTube |
| Meta native | Image-to-video (up to 20 product photos → multi-scene video), AI dubbing with lip-sync, AI voiceover, AI music, UGC-style avatar videos (testing), Muse Image (Jul 2026) rolling into Advantage+; Muse Video preview only; generative video ads announced at Advertising Week NY (6 Oct 2026) | included | Meta Q1/Q2 2026 earnings, MediaPost NewFronts, Common Thread, Digital Applied |

**Demand side (documented cases, mostly vendor-reported):**

| Brand | What they did | Reported result | Independence |
|---|---|---|---|
| Hilton + Shuttlerock + Meta | Static hotel photos → AI image-to-video for Travel Catalog Ads; 46 London hotels → 700+ EMEA properties | +[x%] bookings, +[x%] ROAS (one secondary source cites +[x%] reach) | Supplier case study |
| Cuisinart (Amazon Ads) | AI Video Generator vs traditional video, month-long A/B | AI version won | AdExchanger report |
| Deejo (knives) | Dozens of AI UGC ads for Meta + TikTok via VIDEOAI.ME | [n]x ROAS, −[x%] production time | Vendor only, no baseline |
| Zerorez | Creatify, 20–30 creatives/month | −[x%] cost per lead | Vendor only |
| Orbitkey / SelfMade | Atria workflow | −[x%] CPA / +[x%] ROAS | Vendor only |
| Supplement brand (unnamed) | AI UGC hook test | [x%] CTR vs [x%] control | Vendor only |
| Beauty brand (unnamed) | "glass skin in 7 days" hook + product close-up in first 2s, 3 of 12 variants | [x%] CTR vs [x%] avg for other 9 | Vendor only (TikTok) |
| Kalshi (2025) | Veo 3 NBA Finals spot, ~US$ [valor] in gen cost, 300–400 generations → 15 clips | 18M impressions in 48h; the template for "chaotic AI brand video" | NPR, BI |
| Popeyes "Wrap Battle" | Veo 3 + Suno, 3-day turnaround, TikTok/IG/X | reach only | listicles |

**Agency reality check (Marketing Brew, Apr 2026):** Deutsch, Hawke Media, The Charles Group and We Scale Startups all say clients are *hesitant* about gen-AI for customer-facing creative (legal/brand risk), that Meta's native creative AI "consistently sees worse results" than third-party stacks, and that several distinct concepts beat many micro-variants of one idea. Digiday reports brands drawing the line at AI-generated *people* talking to camera while accepting AI product imagery and templating.

### 2.4 Brazil specifics

- **No public Brazilian brand case with Meta Ads metrics for AI video was found.** Closest: Magalu's AI virtual presenter (Dia dos Namorados video, [n] views, organic), Mercado Livre + Samsung fully gen-AI campaign (Sep 2025, no results), and political video (a gubernatorial campaign: produced in hours instead of days).
- The visible AI video volume in Brazilian feeds is concentrated in (a) deepfake health/finance scams (see 2.2) and (b) infoproduct funnels using avatars with PT-BR TTS (tools cited: Konv, FluxoKit, HeyGen).
- Brazilian practitioner guidance converges on: 5-block structure (hook → pain → demo → proof → offer), 9:16 selfie framing, PT-BR lip-sync/prosody QA before publishing, and never presenting an avatar as a "cliente" giving a testimonial (CDC art. 37 misleading advertising risk).
- Meta disclosure label enforcement in Brazil is reported since March 2026 as a top rejection cause (E-Commerce Brasil, Orbit) — secondary sources, treat as directional.

---

## 3. What the data says about performance

| Source | Finding | Weight |
|---|---|---|
| Taboola + Columbia/Harvard/TUM/CMU (Jan 2026), hundreds of thousands of live ads, 500M+ impressions, 3M clicks, "sibling ads" quasi-experiment | AI [x%] CTR vs human [x%] raw; **parity after controls**. Ads that *don't look AI* had the highest engagement; large clear human face = key trust cue; AI ads included such cues more often | Strongest independent evidence, but Taboola-commissioned and native-ads, not Meta |
| Motion Creative Benchmarks 2026 (US$ [valor] Meta spend, 578,750 creatives, 6,015 accounts, Sep 2025–Jan 2026) | [x%] of creatives are winners (≥10x account median spend); [x%] of spend goes to winners ([x%] micro → [x%] enterprise); highest hit rates for the *simplest* formats (text-only [x%], product+text [x%], UGC [x%]); brands launching more creative get ~2x the winners at equal budget | Strong, Meta-specific, but measures spend not ROAS |
| IAB × Sonata "AI Ad Gap" 2026 | Executives think [x%] of consumers are positive about AI-made ads; consumers say [x%] (37-pt gap); trust falls as the "AI look" rises | Survey, independent |
| Klaviyo survey | [x%] say low-quality/generic AI brand content lowers trust | Survey |
| Meta (own claims) | Image-to-video beta: +[x%] CTR, +[x%] CVR; Advantage+ creative +[x%] ROAS; partnership ads −[x%] CPA, +[x%] CTR, +[x%] brand metrics | Platform-reported |
| Vendor comparisons (Superscale, Pose, inBeat, dansugc, hoox) | Contradictory: AI UGC CTR anywhere from [x%] to [x%] of real UGC; ROAS claims range from AI ahead of human (test-volume effect) to human well ahead of AI in 90-day cohorts | Weak, self-interested |

**Consensus that survives the noise:**
- AI video is cheaper and faster, and that alone produces more winners because of volume.
- Real humans still convert better for trust-heavy purchases and in retargeting.
- The penalty is for *looking* AI, not for *being* AI.
- Hook quality explains more variance than AI vs human.

---

## 4. The formats that are actually scaling (pattern library)

1. **AI UGC talking head** — photoreal avatar, phone-selfie framing, 9:16, 15–45s, hook ≤3s, burned-in captions, product close-up by second 2–5, direct offer close. Used in 10–15 hook variants per concept.
2. **Creator-handle "partnership" product skit** — Temu model: 10–20s AI product demo with exaggerated problem/solution, delivered from a creator account rather than the brand page.
3. **Catalog/image-to-video** — Meta native or Shuttlerock: static product/hotel/property photos animated into multi-scene video; lowest risk, no synthetic humans, measurable lift (Hilton +[x%] bookings).
4. **"Chaotic" AI brand spot** — Kalshi/Popeyes/Liquid Death lineage: surreal Veo/Kling scenes, earned media first, then paid amplification. High reach, polarising, little DR evidence.
5. **AI dubbing/localisation of a winning human ad** — Meta's AI dubbing with lip-sync; keeps a real creator but multiplies markets. Lowest trust cost of all AI uses.
6. **Deepfake authority spokesperson** — doctor/celebrity/billionaire endorsing supplements, crypto, prize schemes. Largest illegitimate volume; being litigated in Brazil and elsewhere. Do not imitate; do expect to be confused with it.

---

## 5. Rules of the road (as of Oct 2026)

| Jurisdiction / platform | Rule | Source quality |
|---|---|---|
| Meta ads | AI label auto-applied when Meta's own gen tools significantly modify an asset or when C2PA credentials are present; advertisers expected to toggle disclosure for photoreal synthetic people made elsewhere; synthetic person presented as a real customer, altered real person, or unsupported claim → rejection. "Undisclosed AI content" reportedly [x%] of rejections early 2026 (unverified) | Secondary; confirm in Meta Transparency Center |
| Instagram organic | From 31 Aug 2026 "AI-generated profile" label; unlabeled AI-persona accounts lose recommendation reach (Reels/Explore). Does not cover ads explicitly | TechCrunch, exchange4media |
| Brazil CDC | Avatar may present product/benefits; may not pose as a customer giving a fabricated testimonial | Brazilian practitioner guides; law is settled |
| Brazil TSE 2026 | Manipulated content in election material must be labelled | Jornal de Brasília |
| Meta litigation | Feb 2026 lawsuits against Brazilian deepfake ad operators | Tecnoblog |

---

## 6. Implications for Seu Milhão (prize-draw / capitalização vertical)

1. **Our category is where the scam cluster lives.** Prize, "ganhe dinheiro", Pix-prize and celebrity-endorsement deepfakes are the exact creative Meta is being sued and investigated over. A legitimate advertiser here should expect stricter review and should over-invest in trust signals: real brand identity, SUSEP/regulatory references, real faces, consistent page history.
2. **Use AI where it is invisible and compliant:** catalog/image-to-video of prize assets, AI dubbing/voiceover of real-creator ads, text and static variants (Motion's highest hit-rate formats), background/music generation. These carry near-zero trust penalty.
3. **If using AI avatars, use them as the testing layer only:** 10–15 hook variants per concept, PT-BR lip-sync QA, explicit AI disclosure toggle, never as "cliente que ganhou". Reshoot winning hooks with a real presenter or a real winner for scale.
4. **Hooks to test (inferred from winners):** concrete number in first line ("R$ X por semana"), product/prize close-up by second 2, on-screen caption that states the mechanism (how the draw works) because trust, not desire, is the bottleneck in this vertical.
5. **Volume math:** at [x%] winner rate, a serious test cadence is 20–50 new creatives per cycle; AI tooling (Creatify at ~US$ [valor]/video, Meta native at zero marginal cost) makes that affordable where human UGC (US$ [valor]/asset) does not.
6. **Measurement:** judge AI creative on CPA/ROAS in retargeting and on repeat purchase, not on CTR, since that is where the vendor data most consistently shows AI underperforming humans.

---

## 7. Open gaps / what would make this research better

- A direct Meta Ad Library pull of Brazilian prize/capitalização advertisers (filter: active ads, video, PT-BR), manually tagging AI-generated creatives and ad longevity as a proxy for spend. The Ad Library hides spend outside political ads, but days-active × number of variants is a workable scale proxy.
- Access to Foreplay/Motion/Atria libraries to filter by "AI UGC" tag and sort by days running.
- Meta's official Transparency Center text on ad AI-disclosure thresholds (secondary sources conflict).
- Primary Online Risk Labs report (Fortune summarised it; the methodology for the US$ [valor] estimate is in the original).

---

## Sources

**Investigations and trade press**
- Fortune — Temu / Online Risk Labs: https://fortune.com/2026/08/31/temu-962-million-meta-partnership-ads-fake-creators/
- IBTimes — Temu follow-up: https://www.ibtimes.co.uk/temu-meta-ad-spend-fake-accounts-1817082
- Reuters scam-ads coverage: https://www.socialmediatoday.com/news/report-claims-meta-earning-billions-scam-ads/804915/ · https://www.medianama.com/2025/11/223-meta-billions-dollars-scam-ads-internal-documents/ · https://ppc.land/meta-charged-suspected-fraudsters-premium-rates-while-earning-billions-from-scam-ads/
- Marketing Brew — How Meta's AI push is changing ad creation: https://www.marketingbrew.com/stories/2026/04/07/meta-ai-ad-creation
- Digiday — brands' AI rules for customer-facing content: https://digiday.com/marketing/the-new-ai-playbook-the-rules-brands-are-setting-around-customer-facing-content/
- NPR — Kalshi Veo 3 ad: https://www.npr.org/2025/06/23/nx-s1-5432712/ai-video-ad-kalshi-advertising-nba-finals
- Ad Age — Liquid Death AI Olympics ad: https://adage.com/technology/ai/aa-liquid-death-winter-olympics-ad-sparks-backlash
- eWeek — Coca-Cola AI holiday ad backlash: https://www.eweek.com/fr/news/coca-cola-ai-holiday-ad-backlash/
- MediaPost — Meta NewFronts 2026: https://www.mediapost.com/publications/article/413917/meta-previews-ai-powered-ad-displays-creator-offe.html
- MediaPost — Meta Q2 2026: https://www.mediapost.com/publications/article/416925/meta-boosts-advertising-in-q2.html
- PPC Land — Meta Q2 2026 (9M SMBs on AI creative tools): https://ppc.land/meta-profit-drops-8-to-15-8bn-as-legal-charges-hit-ad-gains/
- TechCrunch — Instagram AI-generated profile reach limits: https://techcrunch.com/?p=3158959
- Bloomberg — Meta image-to-video ads: https://www.bloomberg.com/news/articles/2025-06-17/meta-testing-new-auto-generated-video-ads-as-part-of-ai-push

**Research**
- Motion Creative Benchmarks 2026: https://motionapp.com/library/research/creative-benchmarks-2026/ · spend concentration: https://motionapp.com/library/research/creative-benchmarks-2026/spend-concentration · winners are rare: https://motionapp.com/library/research/creative-benchmarks-2026/winners-are-rare
- Taboola / Columbia / Harvard / TUM / CMU study: https://www.taboola.com/press-releases/genai-ads-study-2026/ · https://www.bandt.com.au/ai-ads-that-dont-look-like-ai-match-human-creative-global-taboola-report-finds/
- IAB × Sonata "AI Ad Gap": https://iab.com/insights/the-ai-gap-widens/
- Shuttlerock / Hilton case: https://yespress.io/shuttlerock

**Brazil**
- Tecnoblog — Meta sues deepfake operators: https://tecnoblog.net/noticias/meta-processa-golpistas-por-uso-de-videos-falsos-de-celebridades/
- URB News — Meta lawsuit over celebrity deepfakes (27 fev 2026), link omitted because the URL names the person
- Agência Lupa — Meta profits from scam ads: https://agencialupa.substack.com/p/13728736_lente-122
- E-Commerce Brasil — Meta integra IA, vídeo e creators: https://www.ecommercebrasil.com.br/noticias/meta-integra-ia-video-e-creators-em-nova-fase-dos-anuncios
- Orbit — Advantage+ Creative 2026 disclosure: https://www.orbitmarketing.com.br/blog/meta-advantage-creative-2026
- Guia IA — Anúncio UGC com IA: https://guiaia.io/anuncio-ugc-com-ia-estrutura-para-vender
- Jornal de Brasília — IA nas campanhas 2026: https://jornaldebrasilia.com.br/noticias/politica-e-poder/inteligencia-artificial-provoca-terremoto-em-campanhas-eleitorais-de-2026/

**Vendors (treat as claims)**
- Arcads seed announcement: https://www.arcads.ai/blog/arcads-raises-16m-seed · GetLatka: https://getlatka.com/companies/arcads.ai
- Apogee — real cost per usable Arcads video: https://www.apogee.ad/en/blog/crea-publicitaire-ia-concepts-meta-ads/
- Creatify / Zerorez: https://creatify.ai/blog/the-8-best-ai-ugc-ad-tools-in-2026
- VIDEOAI.ME / Deejo: https://videoai.me/industries/ecommerce/facebook/ugc-ads
- Icon: https://sacra.com/c/icon/
- Superscale AI vs traditional UGC: https://superscale.ai/learn/ai-vs-traditional-ugc-complete-comparison/
- Pose AI, inBeat, dansugc comparisons: https://pose.ai/blog/ai-ugc-vs-real-ugc-ads-2026 · https://inbeat.agency/blog/ai-ugc-ads-vs-real-ugc · https://dansugc.com/blog/ai-ugc-vs-real-human-ugc-converts-better-2026
- CineRads — Meta AI ad policy explainer: https://www.cinerads.com/blog/ai-ugc-facebook-ad-policy
