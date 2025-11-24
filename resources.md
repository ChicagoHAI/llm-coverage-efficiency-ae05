# Resources Catalog

**Research Project**: LLMs Increase Coverage Not Efficiency

**Date**: November 2025

---

## Summary

This document catalogs all resources gathered for the research project investigating whether Large Language Models primarily increase task coverage (exploration, multiple attempts) rather than efficiency (quality, performance) in code generation tasks.

**Resource Types**:
- 8 research papers (PDFs)
- 2 code generation datasets (HumanEval, MBPP)
- 2 evaluation code repositories
- Supporting documentation and sample data

**Total Size**: ~11 MB papers + ~7 MB datasets + ~2 MB code = ~20 MB

---

## Papers

**Total papers downloaded**: 8

| # | Title | Authors | Year | File | Key Info |
|---|-------|---------|------|------|----------|
| 1 | Systematic Review: Developer Productivity | Multiple | 2024 | [2507.03156_developer_productivity_systematic_review.pdf](papers/2507.03156_developer_productivity_systematic_review.pdf) | 37 studies reviewed, identifies cognitive offloading concerns |
| 2 | GitHub Copilot Productivity Impact | Peng et al. | 2023 | [2302.06590_copilot_productivity_impact.pdf](papers/2302.06590_copilot_productivity_impact.pdf) | 55.8% faster task completion (N=95 RCT) |
| 3 | Human-LLM Dynamic Survey | Multiple | 2024 | [2410.01026_human_llm_dynamic.pdf](papers/2410.01026_human_llm_dynamic.pdf) | 71.9% use LLMs for understanding, not generation |
| 4 | Energy Efficiency of LLM Code | Multiple | 2025 | [2505.20324_energy_efficiency_code.pdf](papers/2505.20324_energy_efficiency_code.pdf) | LLM code 1.17-2x worse energy efficiency |
| 5 | LLM Code Maintainability | Multiple | 2025 | [2508.00700_maintainable_reliable_code.pdf](papers/2508.00700_maintainable_reliable_code.pdf) | Fewer bugs but higher complexity |
| 6 | Code Generation Benchmark Quality | Multiple | 2024 | [2404.10155_code_generation_benchmarks.pdf](papers/2404.10155_code_generation_benchmarks.pdf) | First study of benchmark prompt quality |
| 7 | IBM AI Code Assistant Enterprise Study | IBM Research | 2024 | [2412.06603_ai_code_assistant_enterprise.pdf](papers/2412.06603_ai_code_assistant_enterprise.pdf) | 564 developers, uneven productivity gains |
| 8 | EVOLvE: LLM Exploration Evaluation | Multiple | 2024 | [2410.06238_evolve_llm_exploration.pdf](papers/2410.06238_evolve_llm_exploration.pdf) | LLMs can be optimized for exploration |

**Detailed descriptions**: See [papers/README.md](papers/README.md)

---

## Datasets

**Total datasets downloaded**: 2 (with multiple splits)

| Name | Source | Size | Task | Location | Notes |
|------|--------|------|------|----------|-------|
| **HumanEval** | OpenAI | 164 problems | Python function completion | [datasets/humaneval/](datasets/humaneval/) | Gold standard benchmark, 7.7 tests/problem |
| **MBPP** | Google Research | 974 problems (Train: 374, Test: 500, Val: 90, Prompt: 10) | Python function generation | [datasets/mbpp/](datasets/mbpp/) | Entry-level problems, 3 tests/problem |

### Dataset Details

#### HumanEval
- **Format**: HuggingFace Dataset (Arrow format)
- **Disk size**: ~2 MB
- **Key fields**: `task_id`, `prompt`, `canonical_solution`, `test`, `entry_point`
- **Evaluation**: Functional correctness via unit tests
- **Pass@k metrics**: Standard evaluation approach
- **Sample data**: [datasets/humaneval_samples.json](datasets/humaneval_samples.json)

#### MBPP
- **Format**: HuggingFace Dataset (Arrow format)
- **Disk size**: ~5 MB
- **Key fields**: `task_id`, `text`, `code`, `test_list`, `test_setup_code`
- **Splits**: train/test/validation/prompt
- **Evaluation**: Functional correctness via assertions
- **Sample data**: Available in dataset README

### Download Instructions

See detailed download instructions in [datasets/README.md](datasets/README.md)

**Quick start**:
```bash
cd datasets
python3 download_datasets.py
```

**Manual download**:
```python
from datasets import load_dataset
humaneval = load_dataset("openai_humaneval")
mbpp = load_dataset("google-research-datasets/mbpp")
```

**Git handling**: Datasets are excluded from git via `.gitignore` but can be downloaded locally using the provided scripts.

---

## Code Repositories

**Total repositories**: 2

| Name | URL | Purpose | Location | Notes |
|------|-----|---------|----------|-------|
| **OpenAI Human-Eval** | https://github.com/openai/human-eval | Official HumanEval evaluation framework | [code/human-eval/](code/human-eval/) | Pass@k calculation, safe execution |
| **Google MBPP** | https://github.com/google-research/google-research/tree/master/mbpp | MBPP dataset files | [code/mbpp/](code/mbpp/) | Raw .jsonl files, README |

### Repository Details

#### OpenAI Human-Eval
- **Purpose**: Evaluation harness for HumanEval benchmark
- **Language**: Python
- **Key features**:
  - Safe code execution environment
  - Pass@k metric calculation
  - Example evaluation scripts
- **Key files**:
  - `human_eval/execution.py`: Safe execution
  - `human_eval/evaluation.py`: Pass@k metrics
  - `data/HumanEval.jsonl.gz`: Dataset
- **Installation**: `pip install -e code/human-eval`
- **Security**: Executes untrusted code - review security docs

#### Google MBPP
- **Purpose**: MBPP dataset in raw format
- **Format**: JSONL (JSON per line)
- **Key files**:
  - `mbpp.jsonl`: Full dataset (974 problems)
  - `sanitized-mbpp.json`: Hand-verified subset (427 problems)
  - `README.md`: Dataset documentation
- **Data splits**: Defined by task_id ranges
- **Usage**: Load with standard JSON library

See detailed usage instructions in [code/README.md](code/README.md)

---

## Resource Gathering Notes

### Search Strategy

**Phase 1: Literature Search** (30 minutes)
- Searched arXiv, Semantic Scholar, Papers with Code
- Keywords: "LLM efficiency productivity", "code generation performance", "developer experience"
- Focused on 2024-2025 papers for recent work
- Prioritized empirical studies and systematic reviews

**Phase 2: Dataset Search** (30 minutes)
- Identified HumanEval and MBPP as standard benchmarks
- Both used in multiple reviewed papers
- Available on HuggingFace for easy access
- Complementary: different difficulty levels and formats

**Phase 3: Code Repository Search** (20 minutes)
- Found official evaluation frameworks
- Prioritized maintained repositories with clear documentation
- Selected tools enabling pass@k and quality metrics

### Selection Criteria

**Papers**: Selected for:
- Relevance to hypothesis (coverage vs efficiency)
- Empirical evidence (not just opinion)
- Recent publication (2023-2025)
- Diverse methodologies (RCT, survey, benchmark analysis)
- High-quality venues (arXiv papers with strong citations)

**Datasets**: Selected for:
- Standard benchmarks (used in reviewed papers)
- Availability (HuggingFace, open source)
- Quality (well-validated, canonical solutions available)
- Size (sufficient for statistical analysis)
- Complementarity (different difficulty levels)

**Code**: Selected for:
- Official/authoritative sources
- Active maintenance
- Clear documentation
- Enabling key metrics (pass@k, quality analysis)

### Challenges Encountered

1. **MBPP dataset structure**: Initial confusion about field names
   - Solution: Downloaded both HuggingFace and raw versions
   - Documented field structure in README

2. **Large repository cloning**: google-research repo is huge
   - Solution: Downloaded only MBPP directory files directly
   - Used sparse checkout approach

3. **Paper accessibility**: All target papers freely available on arXiv
   - No paywall issues encountered

4. **Dataset size**: Considered SWE-bench (2,294 problems) but too large
   - Decided to focus on HumanEval + MBPP for initial experiments
   - Can expand later if needed

### Gaps and Workarounds

**Gap 1: Real-world codebases**
- Papers mention enterprise studies but data not available
- **Workaround**: Use HumanEval/MBPP as proxy, well-validated benchmarks

**Gap 2: Energy measurement tools**
- Paper #4 mentions CodeCarbon but not detailed methodology
- **Workaround**: Document recommended tools in code README

**Gap 3: Long-term studies**
- Literature shows gap in longitudinal research
- **Workaround**: Note as limitation, focus on snapshot analysis

**Gap 4: Solution diversity metrics**
- No standard approach found in papers
- **Workaround**: Implement custom metrics (e.g., edit distance, AST similarity)

---

## Recommendations for Experiment Design

Based on gathered resources:

### 1. Primary Dataset: HumanEval
- **Why**: Gold standard, used in 4/8 papers reviewed
- **Size**: 164 problems (manageable, sufficient for stats)
- **Quality**: Well-validated with canonical solutions
- **Metrics**: Enables pass@k, quality comparison

### 2. Secondary Dataset: MBPP
- **Why**: Larger sample (974), different difficulty
- **Size**: Good for robustness checks
- **Quality**: Crowd-sourced, sanitized subset available
- **Metrics**: Same evaluation approach as HumanEval

### 3. Baseline Methods
Recommended comparisons:
- **Human canonical solutions**: From datasets
- **Pass@k analysis**: k ∈ {1, 5, 10, 50, 100}
- **Energy efficiency**: Following Paper #4 approach
- **Code quality**: SonarQube metrics (Papers #5, #6)

### 4. Evaluation Metrics

**Coverage Metrics**:
- Pass@k progression (does k matter?)
- Solution diversity (multiple approaches?)
- Time to first success (exploration time?)

**Efficiency Metrics**:
- Pass@1 (first-attempt success)
- Energy consumption (per Paper #4)
- Runtime performance (vs canonical)
- Code complexity (cyclomatic, etc.)
- Maintainability (technical debt)

**Hybrid Metrics**:
- Quality-quantity trade-off (best of k)
- Task complexity interaction
- Cost-benefit analysis (attempts vs quality)

### 5. Code to Adapt/Reuse

**From OpenAI Human-Eval**:
- `evaluate_functional_correctness()`: Main evaluation function
- `estimate_pass_at_k()`: Statistical pass@k calculation
- Safe execution environment (security critical)

**From Literature**:
- SonarQube integration (Papers #5, #6)
- Energy measurement approach (Paper #4)
- Survey instruments (Papers #1, #7)

**Custom Development Needed**:
- Solution diversity metrics
- LLM API integration for generation
- Results aggregation and analysis
- Visualization of coverage vs efficiency

---

## Resource Statistics

### Papers
- **Total**: 8 papers
- **Total size**: ~11 MB
- **Date range**: 2023-2025
- **Average citations**: High (recent papers)
- **Methodologies**: 3 empirical studies, 2 surveys, 2 benchmarks, 1 review

### Datasets
- **Total**: 2 datasets (4 splits)
- **Total problems**: 1,138 (164 + 974)
- **Total size**: ~7 MB
- **Format**: HuggingFace Dataset (Arrow)
- **Languages**: Python only
- **Canonical solutions**: Available for both

### Code
- **Total**: 2 repositories
- **Total size**: ~2 MB
- **Language**: Python
- **Dependencies**: Standard ML libraries
- **License**: MIT (Human-Eval), Apache 2.0 (MBPP)

---

## Quick Start Guide

### 1. Verify Downloads

```bash
# Check papers
ls -lh papers/*.pdf
# Should show 8 PDF files

# Check datasets
python3 -c "from datasets import load_from_disk; print(len(load_from_disk('datasets/humaneval')['test']))"
# Should print: 164

# Check code
ls -lh code/human-eval/
ls -lh code/mbpp/
```

### 2. Install Dependencies

```bash
# Evaluation framework
pip install -e code/human-eval

# Dataset access
pip install datasets transformers

# Analysis tools (optional)
pip install pylint black
pip install matplotlib seaborn pandas
pip install codecarbon  # for energy measurement
```

### 3. Run Quick Test

```python
# Load a sample problem
from datasets import load_from_disk
dataset = load_from_disk('datasets/humaneval')
problem = dataset['test'][0]

print(f"Task: {problem['task_id']}")
print(f"Prompt: {problem['prompt'][:100]}...")
print(f"Tests available: {len(problem['test'].split('assert'))}")
```

### 4. Review Documentation

- Papers overview: [papers/README.md](papers/README.md)
- Datasets guide: [datasets/README.md](datasets/README.md)
- Code usage: [code/README.md](code/README.md)
- Literature review: [literature_review.md](literature_review.md)

---

## Next Steps for Experimentation

1. **Design experiment protocol**
   - Define LLMs to test (GPT-4, Claude, etc.)
   - Set k values for pass@k (1, 5, 10, 50, 100)
   - Choose quality metrics (energy, complexity, performance)

2. **Implement generation pipeline**
   - LLM API integration
   - Prompt engineering for problems
   - Result storage and tracking

3. **Implement evaluation pipeline**
   - Functional correctness (pass@k)
   - Quality metrics (energy, complexity)
   - Diversity metrics (similarity analysis)

4. **Run experiments**
   - Generate k solutions per problem
   - Execute and evaluate
   - Collect all metrics

5. **Analyze results**
   - Pass@k progression analysis
   - Coverage vs efficiency trade-offs
   - Task complexity interactions
   - Comparison to literature findings

6. **Document findings**
   - Statistical analysis
   - Visualizations
   - Comparison to hypothesis
   - Implications and limitations

---

## Resource Maintenance

### Updating Resources

**Papers**:
- Search for new papers monthly on arXiv
- Filter by citations and relevance
- Add to papers/ directory with updated README

**Datasets**:
- Check for dataset updates quarterly
- Monitor benchmark leaderboards for new standards
- Consider adding domain-specific datasets

**Code**:
- Pull latest from repositories monthly
- Track issues/updates that affect evaluation
- Test compatibility with new versions

### Archival

All resources are stored locally and documented:
- Papers: PDF files in `papers/`
- Datasets: HuggingFace format in `datasets/`
- Code: Git repositories in `code/`
- Documentation: Markdown files in root

**Backup strategy**: Git repository provides version control. Datasets excluded from git but documented for reproduction.

---

## Contact and Support

For issues with:
- **Papers**: See individual paper links on arXiv
- **HumanEval**: https://github.com/openai/human-eval
- **MBPP**: https://github.com/google-research/google-research/tree/master/mbpp
- **This research**: Create issue in project repository

---

## Appendix: Resource URLs

### Papers (arXiv)
1. https://arxiv.org/abs/2507.03156
2. https://arxiv.org/abs/2302.06590
3. https://arxiv.org/abs/2410.01026
4. https://arxiv.org/abs/2505.20324
5. https://arxiv.org/abs/2508.00700
6. https://arxiv.org/abs/2404.10155
7. https://arxiv.org/abs/2412.06603
8. https://arxiv.org/abs/2410.06238

### Datasets (HuggingFace)
- HumanEval: https://huggingface.co/datasets/openai_humaneval
- MBPP: https://huggingface.co/datasets/google-research-datasets/mbpp

### Code (GitHub)
- Human-Eval: https://github.com/openai/human-eval
- MBPP: https://github.com/google-research/google-research/tree/master/mbpp

### Related Tools
- Papers with Code: https://paperswithcode.com/task/code-generation
- Leaderboards: https://paperswithcode.com/sota/code-generation-on-humaneval
- SonarQube: https://www.sonarsource.com/products/sonarqube/

---

**Document version**: 1.0
**Last updated**: November 2025
**Total resources**: 8 papers + 2 datasets + 2 code repositories
