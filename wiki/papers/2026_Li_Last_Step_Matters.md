---
title: "Last Step Matters: Early Uncertainty Cannot Predict Failure in Long-Horizon Agents"
authors: [Zongyue Li, Chengyue Yu, Lei Zang, Chenyi Zhuang, Linjian Mo, Leilei Gan]
year: 2026
venue: "arXiv"
arxiv_id: "2608.29685v1"
primary_taxonomy: "[[taxonomy/Trajectory_Planning_Uncertainty]]"
methods_used: ["[[methods/Verbalized_Confidence]]", "[[methods/Path_Switching_Dynamics]]"]
benchmarks: ["[[benchmarks/DeepResearch_BrowseComp_HLE]]"]
status: reviewed
---

# 最後一步至關重要：早期不確定性無法預測長程 Agent 失敗 (Last Step Matters)

## 1. 一句話總結 (TL;DR)
> 本文系統性評估長程 Agent（Deep-Research）在執行過程中的不確定性動態，發現**執行前中期（0~80% 進度）的所有不確定性信號（AUROC < 0.60）均幾乎無法預測最終成敗**，主因是 Agent 頻繁的**「路徑切換（Path Switching）」**；相反地，**最終步（Final-step）的語言化信心具備高達 0.85 的平均 AUROC**，證實「完成後重試（Post-completion retry）」遠比「執行中途干預（In-trajectory intervention）」更為優越。

---

## 2. 研究動機與痛點 (Problem Formulation)
- **早期干預的未驗證假設**：學界與工業界普遍假設「在多步長流程中，若能在早期捕捉到 Agent 的高不確定性並提早干預，就能節省推論與工具調用成本」。
- **長程研究任務的特性**：在長達數十步的網頁搜尋（BrowseComp）與專家級問答（Humanity's Last Exam, HLE）中，不確定性何時開始具有判別力？現有文獻從未評估過中間過程的信號有效性。

---

## 3. 核心發現與理論機制 (Findings & Mechanism)

### 3.1 核心實證發現
- **前中期信號失效**：在 50% 軌跡進度時，無論是 Verbal Confidence、Perplexity (PPL)、Shannon Entropy 還是 Max NLL，平均 AUROC 皆低於 0.60（接近隨機猜測）。即使到 90% 進度，指標亦低於 0.70。
- **最終步信心突增 (Post-Switch Confidence Surge)**：成功軌跡在接近完成時信心平均暴增 15 個百分點，而失敗軌跡則微幅下降 6 個百分點，使得最終步 AUROC 躍升至 0.85。

### 3.2 解釋機制：路徑切換 (Path Switching)
- Agent 在長程檢索中平均會進行 **4.7 ~ 8.5 次方向切換**（例如自言自語 *"Let me try a different approach"*）。
- 切換前的低信心反映的是被放棄的死胡同，而非最終答案的成敗。切換後，信心與最終正確性的相關係數（Spearman $\rho$）從不到 0.15 劇增至 0.3~0.5。

```text
[Step 1~2: 搜尋方向 A] (Conf: 65%) ──> [Step 3: 切換方向 B] (Conf: 55%) ──> [Step 4~7: 鎖定正確方向 C] (Conf: 95% -> 成功)
                              └─ 切換前低信心與最終成功解耦 ─┘
```

---

## 4. 對 Agent 架構 (Harness) 的關鍵啟示
1. **摒棄中途干預 (In-trajectory Intervention, 如 AUQ)**：
   在中途信心下降時暫停反思，會打斷 Agent 自身的自然路徑切換機制，徒增成本且產生高假陽性。
2. **採用「最後一步信心引導的重啟策略」(BrowseConf-Neg)**：
   放手讓 Agent 跑完全程，在最後一步若 Verbal Confidence $< 0.9$，則附帶「前次答案為錯誤」的上下文重新啟動。此策略在準確率與推論步數的 Pareto 前沿上全面碾壓中途干預。
3. **任務持久性（環境狀態變化）的差異**：
   在唯讀的網頁檢索任務上，路徑切換頻繁；而在具備狀態持久性（State-changing）的 Coding 任務（TerminalBench 2.0）中，早期不確定性較有判別力（AUROC 0.66~0.78），因為中途無法隨意抹消前期的實體操作。

---

## 5. 局限性與批判 (Limitations & Open Questions)
- 評估的 Agent 工具集相對單純（Search 與 Visit），在具備複雜多工具協同或高風險物理操作場景中，中途干預是否仍有其必要性仍需權衡。
- 主要測試單 Agent 深度檢索，尚未探討 Multi-Agent 體系下的路徑切換傳播。

---

## 6. 關聯頁面 (Backlinks)
- 分類：[[taxonomy/Trajectory_Planning_Uncertainty]], [[taxonomy/Action_Level_Uncertainty]]
- 涉及方法：[[methods/Verbalized_Confidence]], [[methods/Path_Switching_Dynamics]]
- 評測基準：[[benchmarks/DeepResearch_BrowseComp_HLE]]
- 相關論文：[[papers/2026_Donaldson_Bayesian_Uncertainty_Propagation]] (比對：多跳檢索中的誤差傳播)
