# HotpotQA 與 StrategyQA 校準評測基準

> 屬於分類：[[index|知識索引]] > [[benchmarks/HotpotQA_StrategyQA_Calibration]]  
> 關聯文獻：[[papers/2026_Donaldson_Bayesian_Uncertainty_Propagation]]

## 1. 基準任務簡介 (Overview)
在多步推理與 Agentic RAG 的不確定性估計中，以下兩個資料集常作為關鍵對比場景：

1. **HotpotQA**：
   - 典型特徵：需要**多跳（Multi-hop）檢索**與資訊整合。Agent 必須根據前一步檢索結果動態決定下一步關鍵字（典型 ReAct 模式）。
   - 適合檢驗：**長鏈條誤差累積**與不確定性跨階段傳遞效果。
2. **StrategyQA**：
   - 典型特徵：題目需要隱式策略推理（如 "Did Aristotle use a laptop?"），但推理步數較少且高度依賴 LLM 內在常識。
   - 適合檢驗：單點知識不確定性與自評校準能力。

---

## 2. 關鍵評估指標 (Key Metrics)

- **AUROC (Area Under ROC Curve)**：
  評估不確定性分數區分「正確回答」與「失敗/幻覺回答」的判別能力（>0.5 代表優於隨機猜測）。
- **AUARC (Area Under Accuracy-Rejection Curve)**：
  評估**選擇性預測（Selective Prediction）**實用性。當依序拒答高不確定性樣本時，保留樣本的整體準確率提升幅度。
- **ECE (Expected Calibration Error)**：
  模型輸出之自信度（Confidence）與實際經驗準確率（Accuracy）之間的平均絕對差值，值越小越好。
- **Brier Score**：
  機率預測的均方誤差：$\text{BS} = \frac{1}{N} \sum_{i=1}^N (p_i - y_i)^2$，基準值為 0.25（隨機預測）。

---

## 3. 實驗觀測結論
根據 [[papers/2026_Donaldson_Bayesian_Uncertainty_Propagation]] 的實驗：
- **在 HotpotQA 上**：多階段傳遞模型（BN Overall）達成最高的 AUROC（0.7240）與最低的 ECE（0.1120），顯著優於單一節點。
- **在 StrategyQA 上**：單節點 Generator $P(\text{True})$ 表現最優，傳遞模型因確定性 OR 門放大上游微弱信號而退化。
