# Semantic Entropy (語義熵)

> 屬於分類：[[index|知識索引]] > [[methods/Semantic_Entropy]]  
> 經典文獻：Kuhn et al. (Nature 2023 / ICLR)

## 1. 原理概述 (Concept Overview)
傳統以 Token 為單位的預測熵（Token-level Entropy）無法區分「純文字表達多樣性」與「事實概念的不確定性」。**Semantic Entropy** 的核心概念是：**在語義空間（Meaning Space）而非詞元空間（Token Space）計算夏農熵**。

---

## 2. 演算法四步驟 (Algorithm Pipeline)

1. **採樣多個輸出 (Sample Generations)**：
   給定輸入提示詞 $x$，利用溫度採樣（Temperature Sampling）生成 $K$ 個候選回覆：$\{y_1, y_2, \dots, y_K\}$。
2. **語義聚類 (Semantic Clustering via NLI)**：
   使用雙向自然語言蘊涵模型（Natural Language Inference, 如 DeBERTa），判斷兩兩回覆是否互為蘊涵：
   $$ y_i \equiv y_j \iff (y_i \models y_j) \land (y_j \models y_i) $$
   藉此將 $K$ 個回覆劃分為 $C$ 個互斥的語義等價類別：$\{c_1, c_2, \dots, c_C\}$。
3. **計算各類別機率 (Cluster Probabilities)**：
   $$ P(c) = \sum_{y_i \in c} P(y_i | x) $$
4. **計算語義熵 (Compute Semantic Entropy)**：
   $$ \mathcal{SE}(x) = -\sum_{c=1}^C P(c) \log P(c) $$

---

## 3. 在 Agent 決策上的延伸與價值
- **Agent 工具參數驗證**：若多次採樣產生的 SQL 查詢或 API 參數語義完全等價，即使字面上微小不同，語義熵依然接近 0，代表決策高度可靠。
- **侷限性**：需要多次採樣（$K \ge 5$）以及多次 NLI 矩陣比對，計算開銷較大，在即時性要求極高的 Agent 互動中需權衡延遲。

---

## 4. 關聯頁面 (Backlinks)
- 概念所屬：[[taxonomy/Token_Level_Uncertainty]], [[taxonomy/Action_Level_Uncertainty]]
