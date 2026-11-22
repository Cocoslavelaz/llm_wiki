# Token 與語義層級不確定性 (Token & Semantic Level Uncertainty)

> 屬於分類：[[index|知識索引]] > [[taxonomy/Token_Level_Uncertainty]]

## 1. 核心定義 (Definition)
這是自然語言處理中最基礎的不確定性估計層次，聚焦於 LLM 在生成文字序列時，針對單一 Token 或整段語句的預測信賴度。

## 2. 兩種核心範式 (Two Paradigms)
1. **Token-Level Entropy (詞元層級熵)**：
   - 直接依賴模型最後一層輸出的 Softmax 機率分佈 $P(y_t | y_{<t}, x)$：
     $$ H(y_t) = -\sum_{v \in V} P(v) \log P(v) $$
   - **缺點**：自然語言具有「同義表達（Lexical Variety）」。同一個事實可以用多種詞彙表達（如 "Paris" vs "City of Light"），這會導致 Token 熵偏高，但實質上模型並無語義上的不確定性。
2. **Semantic-Level Uncertainty (語義層級不確定性)**：
   - 解決同義詞造成的假性不確定性，將採樣到的候選答案依據「雙向蘊涵（Bidirectional Entailment）」聚類為語義等價群組，計算語義群組的分佈熵。
   - 代表方法：[[methods/Semantic_Entropy]]。

## 3. 在 Agent 情境下的角色
- 可作為偵測幻覺（Hallucination）的第一道防線。
- 當 Agent 在生成思考鏈（Chain-of-Thought）或觀察總結（Observation Summary）時，語義層級不確定性可評估推理過程的穩健度。

---

## 4. 關聯鏈結 (Related Links)
- 代表方法：[[methods/Semantic_Entropy]]
- 下一層級：[[taxonomy/Action_Level_Uncertainty]]
