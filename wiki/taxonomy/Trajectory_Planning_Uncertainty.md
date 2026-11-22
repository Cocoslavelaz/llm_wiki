# 規劃與軌跡層級不確定性 (Trajectory & Planning Level Uncertainty)

> 屬於分類：[[index|知識索引]] > [[taxonomy/Trajectory_Planning_Uncertainty]]

## 1. 核心定義 (Definition)
**Trajectory-Level Uncertainty** 聚焦於 Agent 在**長程多步推理與執行軌跡（Sequential Decision Trajectory）**中的不確定性傳播與累積。

Agent 的運行本質上是部分可觀察馬可夫決策過程（POMDP），序列中包含環境狀態 $s_t$、思考 $c_t$、行動 $a_t$ 與觀察反饋 $o_t$。軌跡層級不確定性試圖回答：
> *「當前整條推理鏈條是否已經偏離目標？未來的多步探索是否值得信任？」*

---

## 2. 核心挑戰：複合誤差傳遞 (Cascading Error)
1. **語義漂移 (Semantic Drift)**：在多輪搜尋或多步工具調用中，上游 Planner 的微小瑕疵會導致下游 Retriever 檢索錯誤資訊，最終使 Generator 產生看似合理的胡言亂語（Confabulation）。
2. **死循環與崩潰 (Reasoning Collapse)**：Agent 在缺乏信心時反覆調用相同工具，或在局部最優解中無限循環。

---

## 3. 代表性建模範式 (Modeling Paradigms)
- **機率圖傳遞模型 (Bayesian Networks)**：
  - 將各階段抽象為 DAG 節點，利用 CPT 條件機率矩陣評估系統級失敗風險。
  - 代表研究：[[papers/2026_Donaldson_Bayesian_Uncertainty_Propagation]]。
- **互資訊分解 (UProp Framework)**：
  - 將軌跡不確定性分解為內在不確定性（Intrinsic Uncertainty, IU）與外在累積不確定性（Extrinsic Uncertainty, EU），利用點互資訊（PMI）追蹤累積量。
- **樹搜尋價值信賴度 (MCTS / Tree-of-Thoughts Confidence)**：
  - 在探索不同分支時，評估每個狀態節點的價值估計變異數。

---

## 4. 關聯頁面 (Backlinks)
- 來源文獻：[[papers/2026_Donaldson_Bayesian_Uncertainty_Propagation]]
- 相關方法：[[methods/Bayesian_Network_Propagation]], [[methods/Semantic_Divergence]]
- 銜接下層：[[taxonomy/Action_Level_Uncertainty]]
