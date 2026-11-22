# 📚 LLM Agent Uncertainty Estimation - Knowledge Index (MOC)

> 歡迎來到 **LLM Agent 不確定性估計知識庫**。本 Wiki 依循 Karpathy 的編譯型架構維護，所有頁面具備雙向鏈結與出處索引。

---

## 🗂️ 核心本體分類 (Taxonomy)

- [[taxonomy/Token_Level_Uncertainty|Token 與語義層級不確定性]]：傳統 Logits 熵、語義熵（Semantic Entropy）、詞彙化機率信心。
- [[taxonomy/Action_Level_Uncertainty|行動與決策層級不確定性]]：Tool-use 選擇不確定性、參數生成信心、Action-space 熵。
- [[taxonomy/Trajectory_Planning_Uncertainty|規劃與軌跡層級不確定性]]：多步推理樹、路徑切換動態（Path Switching）、POMDP 誤差傳遞、Multi-Agent 拓撲傳播。
- [[taxonomy/Calibration_and_Selective_Generation|校準理論與選擇性決策]]：期望校準誤差（ECE）、保證覆蓋率（Conformal Prediction）、求助人類（Human-in-the-Loop）。

---

## 🛠️ 方法庫 (Methods & Algorithms)

- [[methods/Semantic_Entropy|Semantic Entropy (語義熵)]]：透過雙向聚類解決自然語言表達多樣性的語義級不確定性估計。
- [[methods/Verbalized_Confidence|Verbalized Confidence (語言化信心)]]：黑盒模型自評信心、$P(\text{True})$ 與最終步黃金準則。
- [[methods/Path_Switching_Dynamics|Path Switching Dynamics (路徑切換動態)]]：解釋長程任務中前中期不確定性預測失效的根本機制。
- [[methods/Bayesian_Network_Propagation|Bayesian Network Propagation (貝氏網路傳遞)]]：利用機率圖模型與 CPT 追蹤多階段 Agentic RAG 的不確定性累積。
- [[methods/Recursive_Error_Propagation_MAS|Recursive Error Propagation (遞迴誤差傳播)]]：以採納/批判權重追蹤 Multi-Agent DAG 上的線上錯誤傳播 (PropUQ-MAS)。
- [[methods/PARAFAC2_Tensor_Decomposition_MATU|PARAFAC2 Tensor Decomposition (張量分解 UQ)]]：將多輪多 Agent 異質軌跡編碼為不規則張量，以重建殘差量化系統共識脆弱度 (MATU)。
- [[methods/Semantic_Divergence|Semantic Divergence (語義發散度)]]：基於 Wasserstein 距離錨定承諾軌跡，專門解決 Agent 結構化輸出的語義坍縮問題。

---

## 📄 論文精讀存檔 (Paper Archives)

- [[papers/2026_Donaldson_Bayesian_Uncertainty_Propagation|2026_Donaldson et al. - Bayesian Uncertainty Propagation for Agentic RAG Pipelines]] (arXiv 2026, 貝氏網路 + 多跳 RAG 不確定性傳遞)
- [[papers/2026_Li_Last_Step_Matters|2026_Li et al. - Last Step Matters: Early Uncertainty Cannot Predict Failure in Long-Horizon Agents]] (arXiv 2026, 長程 Agent 早期不確定性失效分析與路徑切換)
- [[papers/2026_Liu_PropUQ_MAS|2026_Liu et al. - PropUQ-MAS: Propagation-Aware Uncertainty Quantification for LLM Multi-Agent Systems]] (EMNLP 2026, 多 Agent 系統的線性遞迴誤差傳遞)
- [[papers/2026_Chen_MATU_Tensor_Decomposition|2026_Chen et al. - Every Response Counts: Quantifying Uncertainty of LLM-based MAS through Tensor Decomposition]] (ACL 2026, 基於高階張量分解的黑盒 Multi-Agent UQ)

---

## 📊 評測基準與指標 (Benchmarks & Metrics)

- [[benchmarks/HotpotQA_StrategyQA_Calibration|HotpotQA & StrategyQA 基準]]：AUROC、AUARC 選擇性預測、ECE 與 Brier Score 在多步 Agentic 任務中的校準表現。
- [[benchmarks/DeepResearch_BrowseComp_HLE|DeepResearch: BrowseComp & Humanity's Last Exam (HLE)]]：長程自主瀏覽與專家級問答測試場。

---

## 📑 橫向綜述 (Syntheses & Surveys)

- *(即將透過 `/synthesize` 彙整橫向比較)*

---

## 🖥️ 產出簡報 (Presentations)

- [簡約科技風教學 HTML 簡報](../presentations/slides.html)
