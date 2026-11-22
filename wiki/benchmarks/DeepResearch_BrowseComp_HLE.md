# 長程自主研究基準：BrowseComp 與 Humanity's Last Exam (HLE)

> 屬於分類：[[index|知識索引]] > [[benchmarks/DeepResearch_BrowseComp_HLE]]  
> 代表文獻：[[papers/2026_Li_Last_Step_Matters]]

## 1. 基準背景與任務特質 (Overview)
隨著 LLM Agent 發展，傳統數步之內的短程任務（如 GSM8K、HotpotQA）已無法代表真實世界長程自主研究（Deep-Research）的挑戰。以下兩個評測集是目前最嚴苛的長程測試場：

1. **BrowseComp / BrowseComp-zh** (Wei et al., 2025; Zhou et al., 2025)：
   - **特性**：需要持續在真實網路世界中導覽數十個複雜網頁，解決高度交織、難以單一檢索直接命中的資訊搜尋問題。
   - **平均步數**：20 ~ 32 步，最長可達 80 步。
2. **Humanity's Last Exam (HLE)** (Center for AI Safety et al., 2026)：
   - **特性**：涵蓋數學、物理、人文等全學科之專家級難題，由全球頂尖學者設計，目前頂尖模型準確率僅約 30%~50%。

---

## 2. 在不確定性估計中的獨特現象
- **前中期不確定性難以預測失敗**：在上述長程任務中，早期不確定性指標 AUROC 低於 0.60。
- **路徑切換（Path Switching）頻發**：BrowseComp 中有 86.8% 的軌跡包含路徑切換，平均切換達 8.5 次。

---

## 3. 關聯頁面 (Backlinks)
- 來源文獻：[[papers/2026_Li_Last_Step_Matters]]
- 相關現象：[[methods/Path_Switching_Dynamics]]
- 評測指標：[[taxonomy/Trajectory_Planning_Uncertainty]]
