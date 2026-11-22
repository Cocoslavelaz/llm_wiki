# 遞迴誤差傳播演算法 (Recursive Error Propagation for MAS)

> 屬於分類：[[index|知識索引]] > [[methods/Recursive_Error_Propagation_MAS]]  
> 代表文獻：[[papers/2026_Liu_PropUQ_MAS]] (PropUQ-MAS)

## 1. 核心概念 (Concept)
在 Multi-Agent 系統中，各個 Agent 之間透過結構化訊息溝通，錯誤往往不是獨立產生的，而是「繼承」自上游。**Recursive Error Propagation** 建立在 DAG 執行圖上，在單次前向傳播中，將每個節點的邊際失誤風險解耦為**局部生成風險**與**上游污染風險**。

---

## 2. 核心遞迴公式 (Recurrence Formula)
對任意執行節點 $v$，其傳播感知不確定性 $r_v$ 定義為：
$$ r_v = 1 - (1 - u_v) \prod_{p \in \text{Pa}(v)} (1 - \hat{\alpha}_{pv} r_p) $$
- $u_v \in [0, 1]$：節點 $v$ 自身的局部不確定性（可用 Verbalized Confidence 或 Logits 衡量）。
- $r_p$：父節點 $p$ 的累積不確定性。
- $\hat{\alpha}_{pv} \in [0, 1]$：節點 $v$ 對父節點資訊的採納權重（Adoption Weight）。

### 重要數學性質：
1. **有界性 (Boundedness)**：保證 $0 \le r_v \le 1$。
2. **不確定性衰減 (Attenuation under Critique)**：若下游 Agent 採取嚴格批判（$\hat{\alpha}_{pv} \to 0$），即使上游 $r_p$ 極高，下游不確定性仍可成功被阻斷並下降，保證非單調傳遞。
3. **線性複雜度 (Linear Scalability)**：時間複雜度僅為 $\mathcal{O}(|\mathcal{V}| + |\mathcal{E}|)$，可無縫支援即時線上監控。

---

## 3. 關聯頁面 (Backlinks)
- 來源文獻：[[papers/2026_Liu_PropUQ_MAS]]
- 對比範式：[[methods/Bayesian_Network_Propagation]] (貝氏網路離散門控), [[methods/PARAFAC2_Tensor_Decomposition_MATU]] (高階張量分解)
