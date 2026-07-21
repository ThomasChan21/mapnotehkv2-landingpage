# MapNoteHK Landing Page Revamp Plan (v2)

**Status:** Approved direction (messaging + policy layer + phased delivery)  
**Date:** 2026-07-21  
**Branch:** `features/cir-policy-landing-revamp` (from `develop`)  
**Scope:** Reposition `landingpage/` for **工商舖 / 大手 / 全幢** agents; align copy with real agent jobs-to-be-done (**nearby S16 impact** + **policy intelligence** for whole-building / large deals).  
**Design input:** ui-ux-pro-max (B2B proptech / professional tool; minimal, trust-led, spacious)

---

## 1. Glossary

| Term | Meaning |
|------|---------|
| **ICP** | Ideal Customer Profile — the best-fit user we design product, copy, and signup for. |
| **CIR** | Commercial / Industrial / Retail — English shorthand for **工商舖**. |
| **工商舖** | 商業、工業、零售物業（本地常用叫法）。 |
| **大手** | Large-ticket / institutional-style deals（跟財團、投資方、大型成交）。 |
| **全幢** | Whole-building sale / whole-block deals. |
| **S16** | Town Planning Board section 16 planning applications（代理日常最常問的周邊申請類型）。 |
| **活化工廈 (IB Revitalisation)** | 含最高 20% 地積比放寬、標準金額補地價方案與免補地價整幢改裝等政策參考。 |
| **強拍 (Compulsory Sale)** | 舊樓（含舊工廈／商廈）強拍門檻相關條例參考（例如 70%／65% 門檻資訊）。 |
| **OZP 柱一／柱二 (Col 1/2)** | Column 1（經常准許用途）vs Column 2（須向城規會作 S16 申請用途）。 |

**Audience label (use):** 工商舖／大手／全幢  
**Audience label (avoid):** 地皮代理、大眾地產代理通用工具、以住宅「睇樓跟客」為主的定位  
**Feature language OK:** 地段、地盤、界線、GFA、活化政策、強拍門檻 — describe *capabilities*, not the ICP name.

**Policy disclaimer (required on LP + product):** 僅供參考，非法律／測量／估價意見；政策會更新，請核對官方最新版本並標註資料日期。

---

## 2. Strategic verdict

| Decision | Rationale |
|----------|-----------|
| Niche the LP to 工商舖／大手／全幢 | Higher deal size, clearer data pain, stronger willingness to pay. |
| Do **not** lead with「追改劃」 | Most agents do not “follow rezoning” as a daily habit. |
| **Primary:** nearby S16 → impact on target building | Matches on-site client Q&A (景觀／先例／密度氣氛). |
| **Secondary:** policy cheatsheet (活化／強拍／OZP Col 1·2) | Empowers agents to speak institutional language; not a second hero promise. |
| Messaging first, then product depth | Copy + visuals + form ship first; in-app policy tags / Lot / GFA later. |
| Never claim “shipped” for unfinished MVP | Use 已上線 / 本頁參考 / 開發中 / 登記意向. |

### Agent jobs-to-be-done (core)

Around **their target building**, agents want nearby planning applications (especially **S16**) and a clear read on:

1. **景觀 / view** — 會唔會擋景、outlook 變差？  
2. **改用途先例 / change-of-use precedent** — 附近有無可比成功案例？（如工廈改 Office／Hotel）  
3. **政策與溢價潛力 / policy & value drivers** — 活化放寬、強拍門檻、OZP 柱一／柱二等參考（輔助判斷，非自動合資格結論）  
4. **對「呢幢／呢個盤」的實質影響** — 跟客時講得清楚，展現機構級專家形象  

S12A / rezoning deep-dive stays **secondary** (全幢／重建／部分大手), not the homepage hero.  
**消防** depth is deferred out of Phase 1 IA unless a single crisp bullet is ready.

### Message hierarchy (hard rule)

| Layer | Promise |
|-------|---------|
| **Hero H1** | Nearby **S16** — 景觀、先例、對目標樓影響 |
| **Hero lead** | + 政策參考（活化／強拍／OZP） |
| **Dedicated section** | Policy Cheatsheet（本頁速覽；App tags 開發中） |
| **Supporting** | 筆記綁地圖 · 機構級 PDF |

---

## 3. Positioning

**One-liner**

> MapNoteHK 幫工商舖／大手／全幢代理，在地圖上即時睇清 **目標樓附近的 S16 規劃申請**，並附 **關鍵政策參考**，理解對景觀、改用途先例、發展密度與活化潛力的影響，再把現場筆記整成專業簡報。

**Category**

香港面向工商舖／大手／全幢前線的 **Geo-proptech（地圖筆記 + 城規資料 + 政策智庫）** 工具。

**Not the hero promise**

- 「追改劃、搶市場先機」作為主標題／主 CTA  
- 「地皮代理專用」  
- 半山住宅放盤作為主視覺證明  
- 把「政策地圖已上線」寫成已交付產品（除非 App 真有 policy tags）

---

## 4. Design system notes (ui-ux-pro-max)

| Dial | Value | Intent |
|------|-------|--------|
| Variance | Low (minimal / centered) | Professional B2B, not playful consumer |
| Motion | Standard / subtle | 150–300ms hovers; respect `prefers-reduced-motion` |
| Density | Spacious | Marketing page rhythm; policy as its own section, not hero clutter |

**Section flow:** Hero → Feature ribbon → Planning (S16) → Policy Cheatsheet → Product proof → Pain → Scenarios → Features → Tiers → Premium → Signup  

**Hero budget:** brand + one H1 + one lead + one CTA group + one product visual. No policy wiki in the first viewport.

**Pre-delivery checks**

- [ ] Text contrast ≥ 4.5:1  
- [ ] Form fields have real `<label>`s  
- [ ] Submit loading → success/error feedback  
- [ ] Touch targets ≥ 44px; responsive 375 / 768 / 1024 / 1440  
- [ ] Policy disclaimer visible near cheatsheet  

---

## 5. Messaging — copy targets (Phase 1)

### 5.1 Meta / chrome

| Element | Target copy |
|---------|-------------|
| `<title>` | MapNoteHK｜工商舖／大手／全幢代理的地圖筆記與政策智庫 |
| Meta description | 地圖上即查目標樓附近 S16 規劃申請；掌握景觀、改用途先例與發展密度。附活化／強拍／OZP 政策速覽。現場筆記 + 專業 PDF。登記 MVP 試用名額。 |
| Header CTA | 免費領取 MVP 試用名額 |
| Footer tagline | 專為香港工商舖／大手／全幢代理而設的地圖筆記與政策智庫工具。 |
| Mobile sticky CTA | 同 header CTA |

### 5.2 Hero

| Element | Target copy |
|---------|-------------|
| Eyebrow | 現正收集工商舖／大手／全幢使用意向 · 規劃申請地圖已上線預覽 · 政策智庫陸續開放 |
| **H1** | 周邊 S16 即查 — 景觀、先例、對呢幢影響，跟盤一次講清 |
| Lead | 地圖顯示目標樓附近的 S16 等規劃申請：類型、狀態一目了然，再連去官方詳情。並附活化工廈／強拍門檻／OZP 柱一柱二等政策參考，對標財團與大手客。 |
| Trust lines | 專為工商舖、大手成交與全幢買賣前線打造 · 下一輪 MVP 名額有限 · 已有可運作產品畫面 |
| Primary CTA | 免費領取工商舖／大手／全幢 MVP 試用名額 |

### 5.3 Pain points

1. **跟大手客睇盤，被問「周邊有無規劃申請？會唔會擋景／改密度？」答唔清** → 地圖顯示附近 S16 + 摘要  
2. **想知活化改用途潛力或強拍條件，要翻多份政府文件** → 本頁／日後 App 政策速覽（活化、強拍、OZP Col 1/2）  
3. **畀財團的 Proposal 缺地圖與政策依據** → 筆記 + 周邊 S16 摘要 + 政策 Context → 2 頁 PDF（Premium）

### 5.4 Four pillars (order matters)

1. 周邊 S16 規劃可視化  
2. 合規與政策智庫（本頁速覽；App Tags 開發中）  
3. 現場筆記綁地圖  
4. 機構級 PDF 分享  

### 5.5 Shipping honesty

| Claim | Status label |
|-------|----------------|
| 周邊／規劃申請地圖 | 免費 · 已上線預覽 |
| 政策速覽（LP 內容） | 本頁參考 |
| App 內政策 Tags／Tooltips | 開發中／登記意向 |
| AI／PDF／關注通知 | Premium · 登記意向 |
| 地段／GFA／White-label | 意向 |

---

## 6. Page information architecture (target)

1. Header — brand, nav（規劃地圖 / 政策速覽 / 功能 / Premium / 登記）, primary CTA  
2. Hero — S16-first H1 + policy in lead + email capture  
3. Feature ribbon — 周邊 S16（免費）· 政策速覽（本頁參考）· AI · PDF（Premium）  
4. Planning section — nearby S16 for target building  
5. **Policy Cheatsheet** — 活化 / 強拍 / OZP Col 1·2 + disclaimer（無消防深潛）  
6. Product showcase — CIR／全幢 framing；PDF alt 唔再寫半山住宅為主證明  
7. Pain → solution  
8. Scenarios — 九龍東／葵涌等使用情境  
9. Core features + note templates（ICP 語氣）  
10. Free vs Premium table  
11. Premium trio  
12. Signup — CIR roles + policy interests  
13. Footer + mobile CTA  

---

## 7. Signup form

### Role options

- 工商舖代理  
- 大手／全幢代理  
- 代理行管理層（工商舖／全幢團隊）  
- 測量／估價／收購相關  
- 投資者／業主代表  
- 其他  

### Interest checkboxes

- 周邊 S16／規劃申請地圖（免費）  
- 活化工廈／強拍門檻提示（本頁參考 · App 開發中）  
- OZP 柱一／柱二用途提示（本頁參考 · App 開發中）  
- AI 整理現場筆記（Premium）  
- 可分享 PDF（含周邊 S16 與政策摘要）（Premium）  
- 關注樓宇／範圍有新申請推送（Premium）  
- 地段／界線搜尋（意向）  
- GFA／地積比估算（意向）  
- 品牌／White-label PDF（意向）  

Optional: 主要做：工商舖 / 大手 / 全幢 / 混合  

---

## 8. Visual / asset plan

| Asset | Action |
|-------|--------|
| Hero screenshot | Prefer 工廈／商業／全幢 + nearby S16；policy badge 僅作示意 annotation，勿寫「Eligible」直至規則可維護 |
| PDF sample | 目標：觀塘／葵涌工廈或全幢 + 周邊 S16 摘要；Phase 1 先改 **alt／文案**；換圖可另 commit |
| Planning shot | Caption：目標樓附近 S16，現場答客更專業 |

---

## 9. Phased implementation

### Phase 1 — Landing only（this branch）

| # | Task | Status |
|---|------|--------|
| 1 | Meta, title, footer, CTAs | In progress |
| 2 | Hero rewrite (S16-first) | In progress |
| 3 | Policy Cheatsheet section + disclaimer | In progress |
| 4 | Pain + scenarios rewrite | In progress |
| 5 | Signup roles + policy interests | In progress |
| 6 | Alt text / CIR framing; asset swap when ready | Done (copy/alt); screenshot swap follow-up |  
| 7 | Update this plan doc to v2 | Done |  
| 8 | Implement Phase 1 on `features/cir-policy-landing-revamp` | Done |

### Phase 2 — Product wedge（mobile / server）

- **P0:** Nearby S16 relative to target + portal links  
- **P0:** Policy Tags／Tooltips in App（OZP zone、Pre-1987 flag、強拍門檻資訊等）— 參考非合資格結論  
- **P1:** PDF export with nearby S16 list + policy context box  
- **P2:** Lot boundary + GFA estimate（legal disclaimer）  
- **P3:** White-label PDF；S12A deep-dive for 重建／大手 niche  

### Phase 3 — Monetization

| Tier | Include |
|------|---------|
| Free | 規劃申請地圖 +（日後）基礎政策 tags |
| Premium | AI、PDF（含 S16＋政策摘要）、關注通知 |

---

## 10. Success metrics

| Signal | Why |
|--------|-----|
| Role mix → 工商舖／大手／全幢 | ICP filter working |
| Interest on 活化／強拍／OZP | Policy value validated |
| Sample PDF engagement（when linked） | Institutional proof |

---

## 11. What not to do

- Do not brand as「改劃追蹤器」.  
- Do not use「地皮代理」as ICP.  
- Do not claim App「政策地圖已上線」until tags ship.  
- Do not show hard「Eligible」policy badges without maintainable rules.  
- Do not overload the first viewport with four policy essays.  

---

## 12. Source trail

- Stakeholder CIR direction (2026-07-21), revised to **工商舖／大手／全幢**.  
- Agent JTBD correction: nearby **S16 impact**, not「追改劃」.  
- v2 policy layer: 活化／強拍／OZP Col 1·2 as **secondary** intelligence.  
- Review tighten-ups: hero hierarchy, shipping honesty, disclaimer, 消防 deferred.  
- Baseline: previous general「地產代理」LP in `index.html`.
