# 貝氏網路不確定性傳遞 (Bayesian Network Propagation)

> 屬於分類：[[index|知識索引]] > [[methods/Bayesian_Network_Propagation]]  
> 首次引入文獻：[[papers/2026_Donaldson_Bayesian_Uncertainty_Propagation]]

## 1. 核心概念 (Overview)
在多階段或多 Agent（Multi-Agent System, MAS）系統中，Agent 的決策通常依賴前一步驟的產出。**Bayesian Network Propagation（貝氏網路傳遞）** 透過機率圖模型（Directed Acyclic Graph, DAG），將每個階段（如 Planner, Evaluator, Generator）視為圖中的隨機變數節點，精確刻畫局部不確定性如何沿著決策鏈累積為系統整體的失誤風險。

---

## 2. 數學形式化 (Formulation)
設 Agent 工作流由隨機變數集合 $X = \{X_1, X_2, \dots, X_n\}$ 組成，則整體聯合機率分佈為：
$$ P(X_1, \dots, X_n) = \prod_{i=1}^n P(X_i \mid \text{Pa}(X_i)) $$
其中 $\text{Pa}(X_i)$ 為節點 $X_i$ 的父節點集合。

### 條件機率表（CPT）與門控模式
- **確定性 OR 門 (Deterministic OR Gate)**：
  任一子階段失敗（FAIL），整體輸出即視為失敗。適用於高安全要求（Safety-critical）之任務（如工業設備維護、金融交易）。
- **雜訊 OR 門 (Noisy-OR Gate - 演進方向)**：
  為各階段設定獨立的失效率阻隔參數 $q_i$，允許系統容忍部分上游雜訊，避免單點誤報導致全盤崩潰。

---

## 3. 在 Agent 決策上的價值
- **可解釋的瓶頸定位 (Root-Cause Diagnosis)**：當系統級不確定性偏高時，可沿 DAG 向上回溯後驗機率，找出究竟是 Planner 規劃失誤、檢索資訊不足、還是 Generator 妄下結論。
- **動態執行截斷 (Early Exit / Abort)**：若上游累積不確定性過高，Agent 可在早期步驟立即中止任務或請求人類介入（HITL），大幅節省 API 成本並防範不可逆副作用。

---

## 4. 關聯文獻 (Backlinks)
- 來源文獻：[[papers/2026_Donaldson_Bayesian_Uncertainty_Propagation]]
- 相關概念：[[taxonomy/Trajectory_Planning_Uncertainty]], [[methods/Semantic_Divergence]]
