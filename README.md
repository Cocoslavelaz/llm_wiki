# LLM Agent Uncertainty Estimation Wiki & Seminar Deck

> 基於 Andrej Karpathy 的 **LLM Wiki 模式**（*"Stop retrieving, start compiling"*）所構建的學術論文知識庫。  
> 專注於 **LLM Agent 的不確定性估計（Uncertainty Estimation）**、**決策校準（Calibration）** 與 **安全執行（Safe Execution / Human-in-the-Loop）**。

---

## 🌟 專案亮點

1. **編譯式知識庫 (Compiled Knowledge Base)**：
   - 拒絕傳統 RAG 碎片化與隨機的向量檢索，將原始 PDF 論文「編譯」為具有雙向鏈結（Obsidian 相容 Wikilinks `[[]]`）的永久筆記網絡。
2. **學術級四層不確定性架構 (4-Tier Taxonomy)**：
   - 涵蓋 `Token-level`、`Semantic-level`、`Action-level` 與 `Trajectory-level` 不確定性。
3. **簡約科技風教學簡報 (Minimalist Tech Presentation)**：
   - 位於 `presentations/slides.html`，具備鍵盤翻頁（`←` / `→` / `Space`）、進度條、全螢幕（`F`）、LaTeX 數學公式（KaTeX）與現代深色科技卡片介面。

---

## 📁 目錄結構

```text
llm_wiki/
├── AGENTS.md                  # 給 AI Agent 的核心守則與指令集 (包含 Ingest, Synthesize, Slides 規則)
├── README.md                  # 本專案說明手冊
├── raw/                       # 【唯讀層】原始資料 (不可被 Agent 篡改)
│   ├── papers/                # 放置下載的 PDF 論文 (例如 2023_Kuhn_Semantic_Entropy.pdf)
│   └── notes/                 # 研討會筆記、個人觀察與零散草稿
├── wiki/                      # 【編譯層】LLM 維護的 Obsidian 相容知識庫
│   ├── index.md               # 知識地圖總導覽 (MOC, Map of Content)
│   ├── log.md                 # 稽核歷程 (紀錄何時 ingest 了哪篇論文)
│   ├── taxonomy/              # 不確定性分類定義 (Token, Action, Trajectory 等)
│   ├── methods/               # 估計演算法 (Semantic Entropy, Verbalized Confidence 等)
│   ├── papers/                # 論文精讀卡片 (含 TL;DR, 數學推導, 實驗指標, 局限性)
│   ├── benchmarks/            # 評測集與指標 (ECE, ToolBench, WebArena 等)
│   └── syntheses/             # 橫向對比綜述與發展趨勢
├── presentations/             # 【產出層】自動編譯的教學 HTML 簡報
│   └── slides.html            # 簡約科技風、可獨立開啟的互動式教學簡報
└── scripts/                   # 輔助自動化工具
    └── extract_pdf.py         # PDF 文字與章節提取腳本
```

---

## 🚀 快速上手指南

### 1. 論文入庫：完全零指令（方案 C 靜默自動巡檢）
**你完全不需要輸入任何指令，也不用記檔名！**
1. 只要將下載的 PDF 丟進 `raw/papers/`。
2. 平常進行任何對話（例如詢問任何問題，甚至只說一聲「嗨」或「今天進度」）。
3. Agent 在回應時會**自動作為前置反射動作**掃描 `raw/papers/`：
   - 自動找出尚未入庫的 PDF。
   - 提取論文文字與數學公式。
   - 生成精讀卡、擴充關聯方法庫與分類。
   - 同步更新 `wiki/index.md` 與 `presentations/slides.html`。
*(若需要手動觸發，亦可隨時輸入 `/ingest`)*

### 2. 主題橫向文獻綜述 (`/synthesize`)
想要跨論文比較技術時，呼叫：
```text
/synthesize 比較白盒 Logits 與黑盒採樣在 Agent 工具調用不確定性上的優缺點與延遲
```
Agent 會僅根據 `wiki/` 內既有編譯內容，輸出對比矩陣並儲存於 `wiki/syntheses/`。

### 3. 查看與更新簡報 (`/build-slides`)
- **直接開啟簡報**：直接使用瀏覽器雙擊開啟 [presentations/slides.html](file:///d:/school/研究所/碩二上/生成式ai/llm_wiki/presentations/slides.html) 即可全螢幕演示。
- **重新編譯簡報**：累積多篇論文後，呼叫 `/build-slides`，Agent 會將最新研究趨勢編譯進簡報。

---

## 🛠️ 開發環境與依賴

本專案無需複雜資料庫，主要依賴 Python（可透過輕量 `uv` 執行）：
- **PDF 文字提取**：
  ```powershell
  uv run --with pypdf python scripts/extract_pdf.py raw/papers/your_paper.pdf
  ```
- **Wiki 閱讀體驗**：可用任何 Markdown 編輯器，推薦使用 **Obsidian** 開啟 `wiki/` 資料夾，即可享有完整雙向鏈結圖譜（Graph View）。
