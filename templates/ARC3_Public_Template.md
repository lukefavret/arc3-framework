# ARC³ Case Framework — Public Template

Use in any editor (Word, Google Docs, Pages, Notion, plaintext). No plugins.

---

## How to Use
1) Choose Mode — Standard | Qual | Lite  
2) Fill **STAR** (one screen)  
3) Complete **A** and lock **A.4** (3–5 criteria)  
4) Do **R**; include ≥1 killed decision gate  
5) Report **C.1**; assess **C.2**; decide **C.3**  
6) Add the compliance footer (license, accessibility, last updated)

**Status vocabulary**: Quant → `Pass | Partial | Fail` • Qual → `Supported | Mixed | Not Supported | Emergent`  
**Reliability target**: κ/α ≥ 0.70 where applicable.  
**Data sources**: `system_log:<table>/<field>`, `instrument:<tool>@<version>`.  
**Style**: SI units; ISO dates.

---

## STAR (Dual-Lane)

**S — Situation:** one line (context & stakes).  
**T — Target (from A.4):** 3–5 criteria (each with **OWNER** + **DATA SOURCE**).  
**A — Approach:** methods + system + **design type**; sample frame; constraints; **instruments/logs**.  
**R — Results:**  
- **Impact:** ROI/adoption/efficiency/risk deltas.  
- **Evidence:** observed vs target; **effect sizes**; **CI/SE**; assumption checks; key **ablations**.  
**Decision:** **GO / PIVOT / PAUSE** → see **C.3**.

---

## A — Anchor & Aim
- **A.1 Provocation & Problem** — core challenge; stakes.  
- **A.2 Prior Art & Theory** — 1–2 key works; how this enters the conversation.  
- **A.3 Audience, Assumptions, Constraints** — who; beliefs; hard bounds.  
- **A.4 Hypotheses & Success Criteria** — **Each hypothesis → 1 criterion** (OWNER + DATA SOURCE).

---

## R — Research & Realization
- **R.1 Methods & Findings** — how you obtained **3–5** insights.  
- **R.2 System Design & Implementation** — hardest problem → alternatives → final.  
- **R.3 Iterations & Decision Gates** — visual evolution; include ≥1 **killed** gate.

---

## C — Characterization, Critique, & Continuation

### C.1 Standard / Lite (Quant/Hybrid)
```
| Criterion (A.4) | Target | Observed | N / CI or SE | Baseline/Control | Ablation / Note | Data Source | Status |
|---|---:|---:|---|---:|---|---|---|
```
*Status:* Pass | Partial | Fail • Include ≥1 ablation and effect size if applicable.

### C.1 Qual (Exploratory)
```
| Criterion (A.4) | Operational Definition | Evidence (n/%/saturation) | Reliability (κ/α) | Excerpts (ID, task, date) | Status |
|---|---|---|---|---|---|
```
*Status:* Supported | Mixed | Not Supported | Emergent • Report IRR & saturation if used.

**Observed behavior summary:** one paragraph tying results back to **A.4**.

### C.2 Critique (Limits & Validity)
Internal / External / Construct / Statistical validity; Reliability; Instrumentation/Drift; Failure modes; Bias/Ethics/Accessibility.

### C.3 Continuation (Decision & Plan)
**Decision** (GO/PIVOT/PAUSE) • **Plan** (owners, dates) • **Triggers** • **Kill-criteria** • **Risks & mitigations** • **Ethics/Compliance**
