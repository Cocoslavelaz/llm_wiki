# 語言化信心 (Verbalized Confidence)

> 屬於分類：[[index|知識索引]] > [[methods/Verbalized_Confidence]]  
> 經典文獻：Tian et al. (EMNLP 2023), Kadavath et al. (2022)  
> 最新進展：[[papers/2026_Li_Last_Step_Matters]], [[papers/2026_Donaldson_Bayesian_Uncertainty_Propagation]]

## 1. 核心概念 (Concept)
**Verbalized Confidence（語言化信心）** 是指透過 Prompt 引導大語言模型直接以文字、數值（0~100）或布林值（如 $P(\text{True})$）評估自己產出之正確信賴度。

由於閉源頂級模型（如 GPT-4o、Claude 3.5 Sonnet）不提供 Softmax Logits，語言化信心已成為**純黑盒環境下最重要的不確定性估計途徑**。

---

## 2. 兩種主流引出模式 (Elicitation Modes)

1. **單字機率法 ($P(\text{True})$ Self-Evaluation)**：
   - 先生成回覆，再詢問 *"Are you sure this answer is correct? (True/False)"*，抓取 `True` 詞元的機率作為信心值。
   - [[papers/2026_Donaldson_Bayesian_Uncertainty_Propagation]] 中 Generator 節點即採用此法，表現出極高的錯誤判別力（AUROC > 0.70），但容易出現系統性過度保守。
2. **逐步自我數值標註 (In-tool-call / In-content Confidence)**：
   - 在 Agent 呼叫工具前，強制要求輸出自評信心分數（如 `conf: 85%`）。

---

## 3. 在 Agent 長程任務中的實證突破
根據 [[papers/2026_Li_Last_Step_Matters]] 的大規模實證：
- **最終步黃金法則 (Final-Step Baseline)**：在長程研究任務中，最終步的 Verbalized Confidence 平均 AUROC 高達 **0.85**，顯著勝過 Token Entropy 與 Perplexity。
- **早期無效性**：在任務執行到 50% 時，Verbalized Confidence 的判別力僅約 0.58~0.60，主因是 [[methods/Path_Switching_Dynamics]]（路徑切換）使得前期的低信心被後續的成功切換稀釋。

---

## 4. 關聯頁面 (Backlinks)
- 概念所屬：[[taxonomy/Token_Level_Uncertainty]], [[taxonomy/Action_Level_Uncertainty]]
- 相關論文：[[papers/2026_Li_Last_Step_Matters]], [[papers/2026_Donaldson_Bayesian_Uncertainty_Propagation]], [[papers/2026_Liu_PropUQ_MAS]]
