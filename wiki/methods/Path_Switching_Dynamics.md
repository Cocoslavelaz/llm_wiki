# 路徑切換動態 (Path Switching Dynamics)

> 屬於分類：[[index|知識索引]] > [[methods/Path_Switching_Dynamics]]  
> 提出文獻：[[papers/2026_Li_Last_Step_Matters]]

## 1. 核心定義 (Definition)
**Path Switching（路徑切換）** 指的是自主長程 Agent 在追求複雜目標的過程中，主動放棄當前失敗或無效的探索方向，轉而嘗試全新策略的行為現象（例如 Agent 自發思考 *"Let me try a different approach"*）。

---

## 2. 為什麼路徑切換會瓦解「早期不確定性預測力」？
在傳統假設中，若 Agent 在第 $t$ 步感到高度不確定，通常被認為該次任務容易失敗。然而，[[papers/2026_Li_Last_Step_Matters]] 的實證研究揭示了反直覺的事實：
- **切換前的不確定性是「局部探索特徵」，而非最終成敗信號**：
  在深度檢索任務中，86.8% 的軌跡存在多次路徑切換（平均每條軌跡切換 4.7 ~ 8.5 次）。Agent 遇到死胡同時信心自然偏低，但隨即發動路徑切換成功找到正確答案。
- **相關性斷裂 (Correlation Decoupling)**：
  在最後一次路徑切換前，信心與最終正確性的相關係數（$|\text{Spearman } \rho|$）低於 0.15；唯有在切換確立最終路徑後，相關係數才快速攀升至 0.3~0.5。

---

## 3. 對 Agent Harness 的系統性建議
| 干預機制 | 運作時機 | 效果評估 |
| :--- | :--- | :--- |
| **中途反思干預 (In-trajectory)** | 當中間步驟信心 $< \tau$ 時中斷反思 | ❌ **差**：打斷正常路徑切換，增加無謂運算，高假陽性。 |
| **終點否定重啟 (BrowseConf-Neg)** | 全程執行完畢，檢查最終步信心 $< \tau$ | ✅ **優**：充分給予路徑探索自由，以負向記憶啟動重試，Pareto 最優。 |

---

## 4. 關聯頁面 (Backlinks)
- 來源論文：[[papers/2026_Li_Last_Step_Matters]]
- 相關層級：[[taxonomy/Trajectory_Planning_Uncertainty]], [[taxonomy/Action_Level_Uncertainty]]
- 涉及方法：[[methods/Verbalized_Confidence]]
