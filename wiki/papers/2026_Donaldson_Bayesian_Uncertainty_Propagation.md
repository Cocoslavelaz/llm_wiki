---
title: "Bayesian Uncertainty Propagation for Agentic RAG Pipelines: A Proof-of-Concept Study on Multi-Hop Question Answering"
authors: [Louis Donaldson, Connor Walker, Koorosh Aslansefat, Yiannis Papadopoulos]
year: 2026
venue: "arXiv"
arxiv_id: "2607.00972v1"
primary_taxonomy: "[[taxonomy/Trajectory_Planning_Uncertainty]]"
methods_used: ["[[methods/Bayesian_Network_Propagation]]", "[[methods/Semantic_Divergence]]", "[[methods/Verbalized_Confidence]]"]
benchmarks: ["[[benchmarks/HotpotQA_StrategyQA_Calibration]]"]
status: reviewed
---

# 貝氏網路在 Agentic RAG 管線中的不確定性傳遞 (Bayesian Uncertainty Propagation)

## 1. 一句話總結 (TL;DR)
> 本文提出利用**貝氏網路（Bayesian Network, BN）**對多階段 Agentic RAG（Planner、Evaluator、Generator）進行不確定性傳遞建模，結合 Wasserstein 語義發散度（Semantic Divergence）與 $P(\text{True})$ 自評信號，成功在多跳推理任務（HotpotQA）中實現優於 UProp 的系統級失敗檢測與高精度校準。

---

## 2. 研究動機與痛點 (Problem Formulation)
- **多步推理中的誤差累積 (Cascading Errors)**：Agentic RAG 本質上是一個部分可觀察馬可夫決策過程（POMDP），上游規劃（Planner）或檢索評估（Evaluator）的微小偏差會在後續步驟中被放大，導致「推理崩潰（Reasoning Collapse）」與無謂的運算開銷。
- **傳統方法的盲點**：
  - 傳統單一節點的 Logits Entropy 或 Semantic Entropy 無法反映多 Agent 協同架構中的**跨階段依賴性**。
  - Semantic Entropy（SE）在面對 Agent 的結構化 JSON 輸出時，容易將重複格式坍縮為單一語義類別，無法準確測量決策分佈的分散度。

---

## 3. 核心方法論與數學公式 (Methodology)

### 3.1 節點層級不確定性信號 (Node-level Uncertainty Signals)
1. **Planner 節點**：採用長度正規化的對數機率（Length-normalized log probabilities）：
   $$ s_i = \frac{1}{L_i} \sum_{t=1}^{L_i} \log p_\theta(z_t \mid z_{<t}, x), \quad q_i = \exp(s_i) $$
   經過校準函數 $f_{\text{cal}}(q_i)$ 映射為先驗成功機率 $P(X_i = \text{success} \mid q_i)$。
2. **Evaluator 節點（語義發散度 Semantic Divergence）**：
   以受拘束的執行軌跡為基準，計算輸出分佈與重採樣分佈在嵌入空間中的 **Wasserstein 距離**，衡量內在不確定性（Intrinsic Uncertainty, IU），有效避免 JSON 格式的語義坍縮。
3. **Generator 節點（$P(\text{True})$ 語言化自信評估）**：
   在產出答案後詢問模型 *"Are you sure that the answer provided is correct?"*，以模型賦予 `True` / `Yes` 詞元的機率作為自信度指標。

### 3.2 貝氏網路傳遞架構 (Bayesian Network Propagation)
將 Planner ($X_1$)、Evaluator ($X_2$)、Generator ($X_3$) 作為隨機變數節點，聯合機率分佈分解為：
$$ P(X_1, \dots, X_n) = \prod_{i=1}^n P(X_i \mid \text{Pa}(X_i)) $$
- **系統級 Overall 節點**：採用**確定性 OR 門（Deterministic OR Gate）**。只要管線中有任一節點的不確定性超過閾值（設定為 0.5），整體系統即判定為 `FAIL`：
  $$ P(\text{Overall} = \text{OK} \mid X_1, X_2, X_3) = \begin{cases} 1.0 & \text{if } X_1=\text{OK} \land X_2=\text{OK} \land X_3=\text{OK} \\ 0.0 & \text{otherwise} \end{cases} $$

---

## 4. 關鍵實驗與對比基準 (Empirical Results)

測試基準採用 **StrategyQA**（單跳隱式推理）與 **HotpotQA**（多跳推理檢索），使用 GPT-3.5-Turbo 與 GPT-4.1-Nano。

| 測試集 | 模型 | Generator 單節點 AUROC | **BN Overall (本文)** | UProp Baseline | ECE (校準誤差) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **HotpotQA** (多步複雜) | GPT-3.5-Turbo | 0.6993 | **0.7160** | 0.7470 | **0.1376** (最優) |
| **HotpotQA** (多步複雜) | GPT-4.1-Nano | 0.7145 | **0.7240** | 0.7188 | **0.1120** (最優) |
| **StrategyQA** (單步淺層) | GPT-3.5-Turbo | 0.5881 | 0.5592 | 0.6040 | 0.4814 |
| **StrategyQA** (單步淺層) | GPT-4.1-Nano | 0.6213 | 0.6083 | 0.5440 | 0.4942 |

### 核心發現：
- **複雜多跳任務極度有效**：在需要多輪檢索與推理的 **HotpotQA** 上，BN 傳遞顯著優於單節點信號，ECE 大幅降低至 0.1120，證實不確定性傳遞在長程 Agentic 任務中的必要性。
- **任務難度的雙面刃**：在較簡單的 **StrategyQA** 上，Planner 和 Evaluator 表現接近隨機猜測，而確定性 OR 門會均等放大雜訊，反而削弱了 Generator 優秀的單點判斷。

---

## 5. 局限性與批判 (Limitations & Open Questions)
1. **確定性 OR 門的脆弱性**：無法自適應調節節點權重。未來應引入 **Noisy-OR** 參數化模型，學習抑制雜訊較高的上游節點。
2. **$P(\text{True})$ 的系統性過度保守**：Generator 普遍給出較高不確定性，導致在簡單任務上高估失敗率（Brier Score 偏高），需搭配 Platt Scaling 等後驗校準技術。
3. **靜態 DAG 限制**：目前 BN 僅反映單次執行軌跡（Abstracted Execution Trace），尚未能對 Agent 的**動態重試循環（Feedback Loops）**與回溯機制進行時序建模。

---

## 6. 關聯頁面 (Backlinks)
- 屬於分類：[[taxonomy/Trajectory_Planning_Uncertainty]], [[taxonomy/Action_Level_Uncertainty]]
- 涉及方法：[[methods/Bayesian_Network_Propagation]], [[methods/Semantic_Divergence]], [[methods/Verbalized_Confidence]]
- 相關評測：[[benchmarks/HotpotQA_StrategyQA_Calibration]]
- 衍生比對：[[methods/Semantic_Entropy]] (作為其對比基礎)
