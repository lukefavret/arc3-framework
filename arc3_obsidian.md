# ARC³ Case Framework — Release Template

> [!info] ARC³ Case Framework — Release Template> **Mode badge:** `Mode: Standard | Qual | Lite`
> **Selection rule:** Choose the mode by the **strongest available evidence**. If tied, use **Standard**.
> > [!info] Framework guardrails> - **A.4 → C.1 contract:** every criterion defined in **A.4** reappears as one row in **C.1** (no orphan metrics).> - **Status vocabulary:** Quant (Standard/Lite): `Pass | Partial | Fail`; Qual (Qual): `Supported | Mixed | Not Supported | Emergent`> - **Reliability targets:** κ/α ≥ **0.70** where applicable (report actual).> - **Conventions:** SI units; ISO-8601 dates; data sources as `system_log:<table>/<field>` or `instrument:<tool>@<version>`.
---
# ⭐ STAR Summary Card (Dual-Lane) — one screen
> [!abstract] One-liner> What it is, for whom, core purpose.**S — Situation** — one-line context & stakes.
**T — Target (from A.4)** — 3–5 criteria, each with an OWNER and DATA SOURCE.
**A — Approach** — methods + system + design type (between/within; randomized/counterbalanced), sample frame & recruitment, constraints, instruments/logs.
**R — Results (dual-lane)**
- Impact (industry): ROI/adoption/efficiency/risk deltas (before → after).
- Evidence (academic): observed vs target, effect sizes (d/δ/OR/RR), CI/SE, assumptions (or nonparametric), ablations/sensitivity checks.

---
# Executive Summary (150–300 words)
Interpret STAR for a general reader. No new metrics. Mention the single most decision-relevant ablation.
For academic export, retitle to **Abstract** and drop the decision sentence.

---
# A — Anchor & Aim
> [!todo] Section A: Action Plan> - [ ] Problem statement & provocation (1 paragraph)> - [ ] Cite 1–2 key papers / prior art> - [ ] Define audience, assumptions, constraints> - [ ] Define 3–5 falsifiable hypotheses with success criteria + data sources> [!bug] Core Challenge> Clearly articulate the problem you are addressing. Frame it from a human-centered perspective.
> What pain point, inefficiency, or unmet need exists?
> Where possible, connect this to a real-world observation from your professional or personal experience to add authenticity.
> > [!question] “What-if?”> **Industry:** What issue are you trying to address? Why is it an issue? How does it interact with norms/competitors?
> **Prototyping:** What is the core "what-if" question? Which assumption are you challenging?
> **Research:** What academic theory or design framework informs your approach? Cite 1–2 key works.
> > [!target] Hypotheses → Criteria (contract for C.1)> Each hypothesis → 1 criterion with OWNER + DATA SOURCE. Every criterion must appear in C.1.
---
# R — Research & Realization
> [!todo] Section R: Action Plan> - [ ] Methods + key findings> - [ ] System design + notable technical challenge> - [ ] Iterations + ≥1 **killed** decision gateR.1 Methods & Findings — Describe methods and why chosen; sample; analysis path → **3–5** actionable insights.R.2 System Design & Implementation — Hardest technical problem → alternatives considered → final rationale.R.3 Iterations & Decision Gates — Show evolution (low-fi → high-fi). For each major decision, cite evidence. Include ≥1 **“we killed X because Y”** gate.
---
# C — Characterization, Critique, & Continuation
> [!todo] Section C: Action Plan> - [ ] Fill **C.1** (map rows to **A.4**)> - [ ] Complete **C.2** validity checklist (specific, honest)> - [ ] Define **C.3** plan (owners, dates, triggers, **kill-criteria**)> [!tip] Characterization Tables> Choose the correct table for your mode. Delete the other.### Standard / Lite (Quant/Hybrid)

| Criterion (A.4) | Target | Observed | N / CI or SE | Baseline/Control | Ablation / Note | Data Source | **Status** |
|---|---:|---:|---|---:|---|---|---|
| 4-wk retention | ≥ 35% | 18% | n=412, ±3% | 20% | Low-latency ablation; **d=0.62** | system_log:retention/weekly_cohorts | **Fail** |
| SUS score | ≥ 80 | 88 | n=15, ±5 | 72 | Novice users only | instrument:SUS@1.1 | **Pass** |

> **Status:** `Pass | Partial | Fail` • Include ≥1 **ablation/sensitivity** check and an **effect size** where applicable (d, δ, OR/RR).
### Qual (Exploratory)

| Criterion (A.4) | Operational Definition | Evidence (n/%/saturation) | Reliability (κ/α) | Representative Excerpts (ID, task, date) | **Status** |
|---|---|---|---|---|---|
| Perspective shift | Post-probe rubric ≥ 2/3 items | 9/14 (64%), saturation by #11 | κ=0.73 | P07: “I never thought about it that way.” | **Mixed** |

> **Status:** `Supported | Mixed | Not Supported | Emergent` • Report **IRR** (κ/α) and indicate **saturation** point if used.
**Observed behavior summary** — one paragraph tying results back to **A.4**.> [!warning] Critique (Limits & Validity)> Internal • External • Construct • Statistical validity; Reliability; Instrumentation/Drift; Failure modes;
> Bias/Ethics/Accessibility. Include concrete evidence, not buzzwords.
> **C.3 Continuation (Decision & Plan)**
- **Decision:** **GO / PIVOT / PAUSE**
- **Plan:** 2–5 actions with **owners & dates**
- **Triggers:** thresholds to proceed
- **Kill-criteria:** explicit stop rules
- **Risks & mitigations:** top 1–2
- **Ethics/Compliance:** (e.g., GDPR; consent archived)

---
# Compliance & Reproducibility Footer
**Repo & Artifacts:** [Tagged Repo] • [Data Dictionary] • [Anonymized Sample] • **Build Hash:** [hash]
**Compliance:** IRB/Consent: ${irb_consent} • **License:** ${license} • **Accessibility:** ${accessibility}
**Preregistration:** ${preregistered} (link: ${prereg_link})
**Versioning:** Last updated: ${last_updated} • Case v${case_version} • Repo tag: ${repo_tag}
**Lite disclosure:** If **Lite**, include — “Lite mode used due to project scope/timebox.”
