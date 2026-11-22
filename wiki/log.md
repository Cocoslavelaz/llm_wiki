# 📝 Wiki Activity & Audit Log

> 記錄每次知識庫編譯（Ingest）、重構（Lint）、綜述（Synthesize）與簡報編譯（Build-Slides）的操作歷程。

---

## 2026-11-22
- **Action**: Initialized Knowledge Base Repository
  - **Operator**: Antigravity Assistant & Researcher
  - **Details**: 
    - 建立 `AGENTS.md`、`scripts/extract_pdf.py` 與基礎資料夾架構。
    - 建立核心分類架構：`taxonomy/`、`methods/`、`benchmarks/`、`syntheses/`。
    - 生成初始簡約科技風教學簡報模板 `presentations/slides.html`。

## 2026-11-22 (Auto-Ingest)
- **Action**: Ingested `raw/papers/Bayesian Uncertainty Propagation for Agentic.pdf`
  - **Title**: *Bayesian Uncertainty Propagation for Agentic RAG Pipelines: A Proof-of-Concept Study on Multi-Hop Question Answering* (Donaldson et al., 2026)
  - **New Created Pages**:
    - `wiki/papers/2026_Donaldson_Bayesian_Uncertainty_Propagation.md`
    - `wiki/methods/Bayesian_Network_Propagation.md`
    - `wiki/methods/Semantic_Divergence.md`
    - `wiki/taxonomy/Trajectory_Planning_Uncertainty.md`
    - `wiki/benchmarks/HotpotQA_StrategyQA_Calibration.md`
  - **Updated Pages**:
    - `wiki/index.md`
    - `presentations/slides.html`

## 2026-11-22 (Policy Update)
- **Action**: Adopted Option C (Zero-Prompt Passive Auto-Scan) as repository default
  - **Details**: Agent will automatically check for newly dropped PDFs in `raw/papers/` at the start of interactions without requiring user invocation.

## 2026-11-22 (Batch Auto-Ingest via Option C)
- **Action**: Detected 3 newly dropped papers in `raw/papers/`
  1. `raw/papers/Last Step Matters - Early Uncertainty Cannot Predict Failure in Long-Horizon Agents.pdf`
     - Card: `wiki/papers/2026_Li_Last_Step_Matters.md`
  2. `raw/papers/PropUQ MAS Propagation Aware Uncertainty Quantification for LLM.pdf` & `raw/papers/PropUQ-MAS.pdf`
     - Card: `wiki/papers/2026_Liu_PropUQ_MAS.md`
  3. `raw/papers/Quantifying Uncertainty of LLM-based MATU.pdf`
     - Card: `wiki/papers/2026_Chen_MATU_Tensor_Decomposition.md`
  - **New Created Methods & Benchmarks**:
    - `wiki/methods/Path_Switching_Dynamics.md`
    - `wiki/methods/Recursive_Error_Propagation_MAS.md`
    - `wiki/methods/PARAFAC2_Tensor_Decomposition_MATU.md`
    - `wiki/benchmarks/DeepResearch_BrowseComp_HLE.md`
  - **Updated Pages**:
    - `wiki/methods/Verbalized_Confidence.md`
    - `wiki/index.md`
    - `presentations/slides.html`

## 2026-11-22 (Slide Deck Upgrade)
- **Action**: Upgraded `presentations/slides.html` from 9 slides to 18 in-depth didactic slides
  - **Details**:
    - Added comprehensive mathematical formulations for Semantic Entropy, Wasserstein Divergence, PropUQ-MAS recurrence, MATU PARAFAC2 decomposition, and PRR/ECE metrics.
    - Deepened case studies from all 4 ingested papers (Donaldson 2026, Li 2026, Liu 2026, Chen 2026).
    - Added interactive slide jump navigation menu in header.

## 2026-11-22 (Graph-Based Presentation Implementation)
- **Action**: Compiled and finalized Graph-based slide deck in `presentations/slides.html`
  - **Details**:
    - Converted linear slide sequence into a State Graph architecture with distinct Stage Nodes, Inspection Gates, and State Transitions.
    - Embedded Master Pipeline banner on Slide 1.
    - Explicitly detailed Inspection Gates: Format Check (SE vs Divergence), Safety Gating (HITL thresholding), Progress Check (Path Switching vs Final Step), Adoption/Critique Attenuation Gate (PropUQ-MAS), and Ragged Tensor Reconstruction Gate (MATU).
    - Fully updated top jump navigation dropdown and KaTeX math delimiters.

## 2026-11-22 (GitHub Deployment)
- **Action**: Successfully pushed repository to GitHub
  - **Remote URL**: `https://github.com/Cocoslavelaz/llm_wiki.git`
  - **Branch**: `main` (tracking `origin/main`)
