---
title: "PropUQ-MAS: Propagation-Aware Uncertainty Quantification for LLM Multi-Agent Systems"
authors: [Yaokun Liu, Yifan Liu, Daniel Yue Zhang, Ruichen Yao, Zelin Li, Dong Wang]
year: 2026
venue: "EMNLP 2026"
arxiv_id: "2608.22130"
primary_taxonomy: "[[taxonomy/Trajectory_Planning_Uncertainty]]"
methods_used: ["[[methods/Recursive_Error_Propagation_MAS]]", "[[methods/Verbalized_Confidence]]"]
benchmarks: ["[[benchmarks/HotpotQA_StrategyQA_Calibration]]"]
status: reviewed
---

# PropUQ-MAS：大語言模型多 Agent 系統的傳播感知不確定性量化

## 1. 一句話總結 (TL;DR)
> 本文提出 **PropUQ-MAS**，將多 Agent 協同執行軌跡展開為通用的**有向無環圖（DAG）**，並推導出一套結合「局部生成不確定性」與「跨 Agent 溝通採納/批判權重」的遞迴不確定性傳遞公式，在單次前向傳播中即時監控中間節點與最終輸出的失誤風險。

---

## 2. 研究動機與痛點 (Problem Formulation)
- **多 Agent 系統（MAS）的可靠性瓶頸**：在軟體工程與多步問題求解中，MAS 的可靠性取決於互動動態（Interaction Dynamics）。上游 Agent 的輕微錯誤常被下游 Agent 當作有效上下文採納並進一步放大。
- **既有 UQ 方法的盲點**：
  - 單 Agent 局部 UQ（如單步 Verbalized Confidence、Token Logits）將每個回覆視為獨立，下游 Agent 即使繼承了錯誤資訊，其「局部信心」仍可能很高（即產生「自信的錯誤回答」）。
  - 現有多 Agent UQ（如 MATU）多依賴多輪重複採樣（Sampling-based post-mortem），計算開銷龐大且無法即時進行逐步線上監控（Online monitoring）。

---

## 3. 核心方法論與數學公式 (Methodology)

### 3.1 執行圖（Execution DAG）與誤差事件分解
將任意拓撲的 MAS 展開為時間序列 DAG $\mathcal{G} = (\mathcal{V}, \mathcal{E})$。節點 $v$ 的整體錯誤事件 $E_v \in \{0, 1\}$ 由兩部分組成：
$$ E_v = I_v \lor \left( \bigvee_{p \in \text{Pa}(v)} Z_{pv} \right) $$
- $I_v$：節點 $v$ 自身的局部推理/生成內在錯誤（Local Error），發生機率 $u_v = P(I_v = 1)$。
- $Z_{pv}$：上游污染事件（Contamination Event），即父節點 $p$ 發生錯誤（$E_p = 1$）且節點 $v$ 選擇採納（Acceptance, $M_{pv} = A$）。

### 3.2 遞迴不確定性傳遞公式 (Recursive Propagation Rule)
在邊緣條件獨立與局部傳播獨立假設下，節點 $v$ 的傳播感知不確定性 $r_v = P(E_v = 1)$ 滿足：
$$ r_v = 1 - (1 - u_v) \prod_{p \in \text{Pa}(v)} (1 - \hat{\alpha}_{pv} r_p) $$
- $\hat{\alpha}_{pv} \in [0, 1]$：節點 $v$ 對父節點 $p$ 訊息的自我匯報採納權重（Adoption Weight）。若下游 Agent 批判/反駁上游，則 $\hat{\alpha}_{pv} \to 0$；若完全採信，則 $\hat{\alpha}_{pv} \to 1$。
- **非單調性與衰減 (Uncertainty Attenuation)**：嚴謹的批判（Critique）或具備高信心的重構能有效阻斷上游錯誤，使得下游不確定性 $r_v < R_v = \max r_p$。

---

## 4. 關鍵實驗與對比基準 (Empirical Results)

- **涵蓋三種經典 MAS 拓撲**：Sequential（循序鏈）、Hierarchical（階層式專家彙整）、Decentralized（去中心化網狀辯論）。
- **測試任務**：GSM8K（數學推理）、MedQA（醫學問答）、MBPP-Plus（代碼生成）。
- **主要提升**：
  - 最終輸出 UQ：平均 AUROC 相對提升 **+6.10% ~ +7.32%**，預測拒答率（PRR）提升 **+41.36% ~ +47.58%**。
  - 中間步驟 UQ：成功在長鏈條中精準定位出引入錯誤的 Critic 或 Refiner 節點。
  - **計算效率**：相較於 MATU（41~56 秒/題），PropUQ-MAS 僅需 **1.3~5.7 秒/題**（單次前向傳播，線性複雜度 $O(|V|+|E|)$）。

---

## 5. 局限性與批判 (Limitations & Open Questions)
- 依賴自我回報的採納分數 $\hat{\alpha}_{pv}$ 作為真實轉移機率的代理，可能受限於模型自身的校準偏差。
- 假設邊緣間條件獨立，在強提示注入或高度混亂的上下文過載情境下，多個上游錯誤的交互關聯可能被低估。

---

## 6. 關聯頁面 (Backlinks)
- 屬於分類：[[taxonomy/Trajectory_Planning_Uncertainty]], [[taxonomy/Action_Level_Uncertainty]]
- 涉及方法：[[methods/Recursive_Error_Propagation_MAS]], [[methods/Verbalized_Confidence]]
- 相關論文：[[papers/2026_Donaldson_Bayesian_Uncertainty_Propagation]], [[papers/2026_Chen_MATU_Tensor_Decomposition]]
