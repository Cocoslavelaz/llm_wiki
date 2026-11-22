# 語義發散度 (Semantic Divergence)

> 屬於分類：[[index|知識索引]] > [[methods/Semantic_Divergence]]  
> 提出文獻：[[papers/2026_Donaldson_Bayesian_Uncertainty_Propagation]] (參考 UProp 框架)

## 1. 核心動機 (Motivation)
在 Agent 迭代檢索與推理過程中，Agent 常需要多次改寫查詢（Query Reformulation）。然而，輕微的偏差會隨著輪次放大，引發**語義漂移（Semantic Drift）**與推理崩潰。

雖然 [[methods/Semantic_Entropy]]（語義熵）能評估自然語言回答的不確定性，但在 Agent 的結構化輸出（如 JSON 格式的 Tool Call）中，微小語法差異在 NLI 模型中容易被判斷為等價，導致**語義類別坍縮（JSON Collapse）**。

---

## 2. 演算法原理 (Wasserstein-based Formulation)
**Semantic Divergence** 採用「錨定於已承諾輸出（Committed Output）」的測量方式：
1. 給定步驟 $t-1$ 的已承諾行動 $y_{t-1}^{(k)}$。
2. 重採樣 $N$ 次該節點的候選輸出分佈。
3. 計算已承諾輸出分佈與重採樣分佈在投射嵌入空間（Projected Embedding Space）中的 **Wasserstein 距離（推土機距離）**。

透過 Wasserstein 距離衡量決策分佈在承諾軌跡點周圍的離散度，作為該節點的內在不確定性（Intrinsic Uncertainty, IU）估計。

---

## 3. 與 Semantic Entropy 的對比
| 特性 | [[methods/Semantic_Entropy]] | **Semantic Divergence** |
| :--- | :--- | :--- |
| **測量核心** | 多個自由文字回覆的雙向蘊涵聚類 | 候選分佈相對於已選決策點的幾何距離 |
| **結構化輸出適用性** | 較差（容易將 JSON 判定為單一群組） | 優秀（嵌入空間距離保持敏感度） |
| **計算負擔** | 高（$O(K^2)$ 雙向 NLI 交叉比對） | 中等（嵌入向量的幾何距離計算） |

---

## 4. 關聯頁面 (Backlinks)
- 來源論文：[[papers/2026_Donaldson_Bayesian_Uncertainty_Propagation]]
- 對應層級：[[taxonomy/Action_Level_Uncertainty]], [[taxonomy/Trajectory_Planning_Uncertainty]]
