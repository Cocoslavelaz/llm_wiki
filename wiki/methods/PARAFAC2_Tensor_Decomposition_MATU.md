# PARAFAC2 不規則張量分解 (PARAFAC2 Tensor Decomposition for MAS)

> 屬於分類：[[index|知識索引]] > [[methods/PARAFAC2_Tensor_Decomposition_MATU]]  
> 代表文獻：[[papers/2026_Chen_MATU_Tensor_Decomposition]] (MATU)

## 1. 核心概念 (Concept)
在 Multi-Agent 系統進行多次重複執行以估計黑盒不確定性時，各次執行產生的對話輪數與工具調用步數通常具有非齊次性（變動長度）。標準張量分解（如 CP 或 Tucker）要求維度長度固定，無法直接處理。

**PARAFAC2（CP-2）** 透過約束潛在因子的正交投影，能夠直接在**不規則張量（Ragged Tensor）**上運行，從異質步長的推理路徑中抽取跨執行的共識特徵。

---

## 2. 數學模型 (Mathematical Formulation)
設三維不規則張量為 $\mathcal{X} = \{E^{(j,k)}\}$，其中 $E^{(j,k)} \in \mathbb{R}^{T_{j,k} \times d}$ 為 Agent $k$ 在第 $j$ 次執行的步驟嵌入矩陣。PARAFAC2 尋求秩為 $R$ 的分解：
$$ \mathcal{X} \approx \sum_{r=1}^R \lambda_r u_r^{(1)} \otimes u_r^{(2)} \otimes u_r^{(3)} $$
其重建損失定義為：
$$ \mathcal{L}_R = \|\mathcal{X} - \hat{\mathcal{X}}_R\|_F^2 $$
總體不確定性 $U = \sum_{R=1}^{R_{\max}} \mathcal{L}_R$ 代表多 Agent 系統的多路徑共識離散度（Semantic Variance）。

---

## 3. 與其他方法的對比
- **優點**：拓撲無關性（Topology-Agnostic），無論是動態路由 AnyMac 還是固定階層 AutoGen 皆能適用；且具備高度可解釋性（可分離出導致失誤的特定語義維度）。
- **缺點**：計算成本較高，需採樣 $N=10$ 次軌跡，適合離線診斷或高價值決策任務。

---

## 4. 關聯頁面 (Backlinks)
- 來源論文：[[papers/2026_Chen_MATU_Tensor_Decomposition]]
- 對比方法：[[methods/Recursive_Error_Propagation_MAS]], [[methods/Semantic_Entropy]]
