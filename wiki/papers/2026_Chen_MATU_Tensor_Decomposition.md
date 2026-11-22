---
title: "Every Response Counts: Quantifying Uncertainty of LLM-based Multi-Agent Systems through Tensor Decomposition"
authors: [Tiejin Chen, Huaiyuan Yao, Jia Chen, Evangelos E. Papalexakis, Hua Wei]
year: 2026
venue: "ACL 2026"
primary_taxonomy: "[[taxonomy/Trajectory_Planning_Uncertainty]]"
methods_used: ["[[methods/PARAFAC2_Tensor_Decomposition_MATU]]"]
benchmarks: ["[[benchmarks/HotpotQA_StrategyQA_Calibration]]"]
status: reviewed
---

# 透過張量分解量化多 Agent 系統不確定性 (MATU)

## 1. 一句話總結 (TL;DR)
> 本文提出 **MATU（Multi-Agent Tensor Uncertainty）**，將多 Agent 協同的多輪推理軌跡建構為**不規則高階張量（Ragged Tensor）**，並運用 **PARAFAC2（CP-2）張量分解**提取潛在語義共識，以重建殘差（Reconstruction Error）精確量化多 Agent 系統整體的不確定性與溝通脆弱度。

---

## 2. 研究動機與痛點 (Problem Formulation)
- **多 Agent 協同的三大 UQ 挑戰**：
  1. *多步推理的長度多樣性*：不同 Agent 與不同 Run 的思考步數差異極大，難以直接比對。
  2. *通訊路徑多樣性 (Communication Diversity)*：相同問題下，多次執行可能產生完全不同的討論與工具調用順序。
  3. *拓撲結構異質性*：現有方法無法通用於 Star、Chain、動態路由（AnyMac）等複雜互動圖譜。
- **既有方法的局限**：NLI 雙向蘊涵模型（如 Semantic Entropy 採用的方式）無法處理長篇軌跡，且無法區分單點幻覺與 Agent 間的交接邏輯衝突。

---

## 3. 核心方法論與數學公式 (Methodology)

### 3.1 軌跡嵌入與不規則張量構建 (Ragged Tensor Representation)
- 將每個 Agent $k$ 在第 $j$ 次執行中的各步輸出（文字或工具調用）透過輕量嵌入模型（Qwen3-Embedding-0.6B）編碼為嵌入矩陣 $E^{(j,k)} \in \mathbb{R}^{T_{j,k} \times d}$。
- 將多次執行的嵌入矩陣堆疊為三維不規則張量 $\mathcal{X} = \{E^{(j,k)}\}$（維度為：$N$ 次採樣 $\times K$ 個 Agent $\times T_{j,k}$ 變動步數 $\times d$ 維度）。

### 3.2 PARAFAC2 (CP-2) 張量分解與重建誤差
利用 PARAFAC2 分解在步長變動的條件下對齊潛在語義特徵，尋求低秩近似：
$$ \mathcal{X} \approx \sum_{r=1}^R \lambda_r u_r^{(1)} \otimes u_r^{(2)} \otimes u_r^{(3)} $$
低秩成分代表跨 Run 達成共識的穩定語義模式。最終不確定性分數 $U$ 定義為跨不同 Rank 的**總重建損失（Frobenius Norm Residual）**：
$$ U = \sum_{R=1}^{R_{\max}} \|\mathcal{X} - \hat{\mathcal{X}}_R\|_F^2 $$
- **統計意義**：在理論上等價於多 Agent 潛在語義空間的**整體變異數（Semantic Variance）**。

---

## 4. 關鍵實驗與對比基準 (Empirical Results)

- **涵蓋多種 MAS 架構**：靜態架構（Camel 雙人討論、AutoGen 星狀分工）與動態路由架構（AnyMac）。
- **評測集**：MATH（數學競賽）、MoreHopQA（多跳問答）、MMLU（通用知識）、HumanEval（代碼生成）。
- **核心成果**：
  - 在動態拓撲 AnyMac 上，MATU 在 GPT-4o、Qwen2.5-7B 與 Llama3.1-8B 上全面超越特徵值法 Eigv(Agr) 與白盒 SAUP。
  - **OOD 異常偵測**：當輸入分佈偏移時，MATU 分數呈現劇烈分離（In-distribution 0.13 vs OOD 0.92），顯著優於既有指標。
  - **下游應用**：成功利用 MATU 不確定性門控引導多模型骨幹路由（Backbone Selection），顯著提高任務命中率。

---

## 5. 局限性與批判 (Limitations & Open Questions)
- 需要多次採樣（$N=10$ runs），在推論延遲與 API 調用成本上高於單次前向傳遞方法（如 [[papers/2026_Liu_PropUQ_MAS|PropUQ-MAS]]）。
- 依賴底層 Text Embedding 模型對推理邏輯的語義表徵品質。

---

## 6. 關聯頁面 (Backlinks)
- 屬於分類：[[taxonomy/Trajectory_Planning_Uncertainty]], [[taxonomy/Action_Level_Uncertainty]]
- 涉及方法：[[methods/PARAFAC2_Tensor_Decomposition_MATU]], [[methods/Semantic_Entropy]]
- 相關論文：[[papers/2026_Liu_PropUQ_MAS]] (對比：黑盒多輪採樣 vs 線性單次傳播)
