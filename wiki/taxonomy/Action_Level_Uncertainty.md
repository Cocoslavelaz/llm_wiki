# 行動與決策層級不確定性 (Action-Level Uncertainty)

> 屬於分類：[[index|知識索引]] > [[taxonomy/Action_Level_Uncertainty]]

## 1. 核心定義 (Definition)
**Action-Level Uncertainty** 專注於 LLM Agent 在互動環境中所執行的「決策行動（Actions）」之置信程度。與傳統單純生成文字回答不同，Agent 的輸出通常包含具體的**執行意圖**（如：調用特定 API、執行 Bash 指令、向用戶提問、終止任務等）。

在行動層面，不確定性主要來源於兩個子層級：
1. **工具 / API 選擇不確定性 (Tool Selection Uncertainty)**：在眾多可用工具中，Agent 不確定哪一個工具適合達成目標。
2. **參數指定不確定性 (Argument / Parameter Uncertainty)**：選定了工具，但對傳入的參數數值或格式信心不足。

---

## 2. 為什麼 Agent 的行動不確定性特別致命？
- **真實世界不可逆性 (Side Effects)**：Agent 的行動通常具有副作用（例如：發送 Email、刪除資料庫、下單交易），一旦在高度不確定狀態下貿然行動，可能導致災難性後果。
- **誤差複合傳遞 (Compounding Error)**：在多步規劃中，第 $t$ 步的錯誤行動會改變環境狀態 $s_{t+1}$，導致後續所有決策皆基於無效狀態。

---

## 3. 主要估計策略 (Estimation Strategies)
- **行動空間熵 (Action-Space Entropy)**：計算候選工具或候選指令之條件機率分佈的夏農熵。
- **採樣一致性 (Sample Consistency across Rollouts)**：多次採樣 Agent 生成的 Action JSON，計算工具選擇的一致度。
- **決策門控機制 (Uncertainty-Gated Execution)**：
  $$ \text{Decision} = \begin{cases} \text{Execute Tool}(a_t), & \text{if } U(a_t) < \tau \\ \text{Ask Human for Clarification}, & \text{otherwise} \end{cases} $$

---

## 4. 關聯方法與文獻 (Related Links)
- 基礎方法：[[methods/Semantic_Entropy]], [[methods/Verbalized_Confidence]]
- 相關層級：[[taxonomy/Trajectory_Planning_Uncertainty]], [[taxonomy/Token_Level_Uncertainty]]
