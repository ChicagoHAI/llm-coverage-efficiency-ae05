# Research Planning Document

**Project**: LLMs Increase Coverage Not Efficiency
**Date**: November 23, 2025
**Time Budget**: 1 hour (3600 seconds)
**Budget**: $100
**Compute**: CPU only

---

## Research Question

**Primary Question**: Do Large Language Models (LLMs) primarily increase task coverage (ability to explore multiple approaches, multiple attempts, rapid iteration) rather than task efficiency (quality of outputs, performance, energy consumption)?

**Refined Question**: When using LLMs for code generation, do they excel at enabling exploration of the solution space (high pass@k with many attempts) while producing less efficient solutions (lower quality metrics like energy, performance, complexity) compared to human-written canonical code?

---

## Background and Motivation

### Why This Matters

The literature review reveals a critical gap in understanding LLM value propositions:
- **Industry narrative**: LLMs make developers more productive (55.8% faster)
- **Hidden reality**: Speed may reflect exploration, not quality
- **Key finding**: 71.9% of developers use LLMs for understanding/exploration, not generation
- **Quality concerns**: LLM code shows 1.17-2x worse energy efficiency

This research addresses whether LLMs are being misunderstood - they may be excellent exploration tools (coverage) but poor optimization tools (efficiency).

### Gap This Research Fills

1. **Lack of coverage vs efficiency decomposition**: No studies directly compare pass@1 vs pass@k progression against quality metrics
2. **Missing diversity analysis**: Solution diversity not systematically measured
3. **Incomplete quality assessment**: Few studies measure energy, performance, AND complexity together

---

## Hypothesis Decomposition

### Main Hypothesis
"LLMs increase coverage not efficiency"

### Sub-Hypotheses (Testable)

**H1: Coverage Hypothesis**
- **H1a**: Pass@k increases significantly with k (pass@10 >> pass@5 >> pass@1)
- **H1b**: Multiple attempts are needed for success (low pass@1, high pass@100)
- **H1c**: Solution diversity is high across k attempts

**H2: Efficiency Hypothesis**
- **H2a**: LLM code is less energy efficient than canonical solutions
- **H2b**: LLM code has worse runtime performance than canonical solutions
- **H2c**: LLM code has higher complexity than canonical solutions

**H3: Task Complexity Interaction**
- **H3a**: Coverage benefit (pass@k improvement) increases with problem difficulty
- **H3b**: Efficiency gap (quality deficit) increases with problem difficulty

---

## Proposed Methodology

### Approach: Multi-Model Pass@k Evaluation with Quality Metrics

**High-Level Strategy**:
1. Generate k=50 solutions per problem using 2-3 LLMs (budget constrained)
2. Evaluate functional correctness (pass@k for k ∈ {1, 5, 10, 25, 50})
3. Measure quality metrics (performance, complexity) on successful solutions
4. Compare against human canonical solutions
5. Analyze coverage (pass@k progression, diversity) vs efficiency (quality metrics)

**Rationale**:
- Pass@k progression tests coverage hypothesis (do more attempts help?)
- Quality metrics test efficiency hypothesis (is output high-quality?)
- Comparison to canonical solutions provides grounded baseline
- Multiple models test generalizability

**Budget Considerations**:
- With $100 budget and ~$0.02 per problem (estimation), we can afford ~5000 API calls
- HumanEval has 164 problems: 164 × 50 = 8,200 calls (TOO EXPENSIVE)
- **Revised**: Sample 40 problems × 50 attempts × 2 models = 4,000 calls (~$80)
- This leaves buffer for retries and analysis

### Experimental Steps

**Step 1: Dataset Preparation** (10 min)
- Load HumanEval dataset (164 problems)
- Stratified sampling: Select 40 problems across difficulty levels
  - 10 easy (high pass@1 in literature)
  - 20 medium (moderate pass@1)
  - 10 hard (low pass@1 in literature)
- Extract prompts, canonical solutions, test cases
- **Rationale**: Stratified sampling tests H3 (task complexity interaction)

**Step 2: LLM Solution Generation** (20 min)
- Select 2 LLMs within budget:
  - **GPT-4o** (state-of-the-art, used in literature)
  - **DeepSeek-v3** or **Claude Sonnet 4.5** (comparison point)
- Generate k=50 solutions per problem per model
- Temperature=0.7 (enable diversity while maintaining quality)
- **Rationale**: k=50 balances coverage measurement with budget constraints

**Step 3: Functional Correctness Evaluation** (10 min)
- Use OpenAI human-eval framework (already available in code/)
- Execute generated solutions against test cases
- Calculate pass@k for k ∈ {1, 5, 10, 25, 50}
- Track which solutions pass for quality analysis
- **Rationale**: Standard evaluation approach from literature

**Step 4: Quality Metrics Collection** (15 min)
- For each PASSING solution:
  - **Runtime performance**: Execute and time
  - **Code complexity**: Calculate cyclomatic complexity (radon library)
  - **Code length**: Lines of code (proxy for simplicity)
- For canonical solutions: Same metrics
- **Rationale**: Energy measurement too complex for 1-hour constraint, use runtime as proxy

**Step 5: Diversity Analysis** (10 min)
- For each problem, measure solution diversity:
  - **Syntactic diversity**: Normalized edit distance between solutions
  - **Semantic diversity**: AST (Abstract Syntax Tree) structural differences
- Calculate mean pairwise diversity
- **Rationale**: Tests coverage hypothesis - high coverage = high diversity

**Step 6: Statistical Analysis** (15 min)
- Pass@k progression: Test if pass@50 > pass@10 > pass@1 (paired t-test)
- Quality comparison: LLM vs canonical (Wilcoxon signed-rank test, non-parametric)
- Task complexity: Correlation between difficulty and coverage/efficiency metrics
- Effect sizes: Cohen's d for all comparisons
- **Rationale**: Rigorous statistical testing of hypotheses

### Baselines

1. **Human Canonical Solutions** (from HumanEval dataset)
   - Used in Papers #4, #5 as gold standard
   - Enables quality comparison

2. **Pass@1 Performance**
   - Internal baseline for coverage analysis
   - If pass@50 ≈ pass@1, no coverage benefit

3. **Literature Benchmarks**
   - Paper #4: Energy efficiency 1.17-2x worse
   - Expected pass@k progression from prior work
   - Validate our findings against published results

**Why These Baselines?**
- Canonical solutions: Ground truth for efficiency
- Pass@1: Tests if multiple attempts matter (coverage)
- Literature: Validates methodology and findings

### Evaluation Metrics

#### Coverage Metrics

1. **Pass@k Progression**
   - **What**: Success rate with k attempts
   - **Why**: Core coverage metric - does more exploration help?
   - **Threshold**: pass@50 > 2× pass@1 suggests strong coverage benefit

2. **Solution Diversity**
   - **What**: Average pairwise edit distance / AST difference
   - **Why**: High diversity = exploring different approaches
   - **Threshold**: Diversity > 0.5 (normalized) suggests meaningful exploration

3. **Attempts to First Success**
   - **What**: How many attempts before first passing solution
   - **Why**: Measures exploration cost
   - **Threshold**: Median > 5 suggests trial-and-error exploration

#### Efficiency Metrics

1. **Runtime Performance Ratio**
   - **What**: LLM runtime / Canonical runtime
   - **Why**: Direct efficiency comparison
   - **Threshold**: Ratio > 1.5 indicates significant efficiency loss

2. **Cyclomatic Complexity**
   - **What**: Number of independent paths through code
   - **Why**: Proxy for maintainability and cognitive load
   - **Threshold**: Complexity > 1.5× canonical indicates over-complication

3. **Code Length**
   - **What**: Lines of code (LOC)
   - **Why**: Simpler code often better (KISS principle)
   - **Threshold**: LOC > 2× canonical suggests verbosity

4. **Pass@1 (First-Attempt Success)**
   - **What**: Probability of success on first try
   - **Why**: Efficiency = getting it right immediately
   - **Threshold**: pass@1 < 30% indicates low efficiency

#### Hybrid Metrics

1. **Quality-Quantity Trade-off**
   - **What**: Best solution quality (from k=50) vs canonical
   - **Why**: Tests if volume compensates for individual quality
   - **Insight**: If best-of-50 ≈ canonical, coverage strategy works

2. **Task Complexity Interaction**
   - **What**: Correlation between problem difficulty and metrics
   - **Why**: Tests H3 - does benefit vary by task?
   - **Analysis**: Spearman correlation, difficulty stratification

### Statistical Analysis Plan

**Statistical Tests**:

1. **Pass@k Progression** (H1a, H1b)
   - Test: Repeated measures ANOVA or Friedman test (non-parametric)
   - Null hypothesis: pass@1 = pass@5 = pass@10 = pass@25 = pass@50
   - Alternative: pass@k increases with k
   - Significance level: α = 0.05
   - Post-hoc: Bonferroni correction for pairwise comparisons

2. **LLM vs Canonical Quality** (H2a, H2b, H2c)
   - Test: Wilcoxon signed-rank test (paired, non-parametric)
   - Null hypothesis: LLM quality = Canonical quality
   - Alternative: LLM quality < Canonical quality (one-tailed)
   - Significance level: α = 0.05
   - Effect size: Cohen's d or rank-biserial correlation

3. **Task Complexity Correlation** (H3a, H3b)
   - Test: Spearman rank correlation
   - Variables: Problem difficulty rank vs coverage/efficiency metrics
   - Null hypothesis: ρ = 0 (no correlation)
   - Significance level: α = 0.05

**Multiple Comparisons Correction**:
- Use Bonferroni correction for multiple metrics
- Adjusted α = 0.05 / number_of_tests
- Conservative approach to avoid false positives

**Effect Sizes**:
- Report Cohen's d for all comparisons
- Interpretation: |d| > 0.8 = large effect, 0.5-0.8 = medium, 0.2-0.5 = small

**Confidence Intervals**:
- Report 95% CI for all metrics
- Use bootstrap (1000 iterations) for non-normal distributions

---

## Expected Outcomes

### If Hypothesis is SUPPORTED:

**Coverage Indicators**:
✓ Pass@50 significantly higher than pass@1 (e.g., 80% vs 30%)
✓ High solution diversity (mean pairwise distance > 0.5)
✓ Attempts to first success: median > 5

**Efficiency Concerns**:
✓ LLM runtime > 1.5× canonical
✓ LLM complexity > 1.5× canonical
✓ Pass@1 < 30% (low first-attempt success)

**Task Complexity**:
✓ Positive correlation: harder problems → greater coverage benefit
✓ Positive correlation: harder problems → larger efficiency gap

### If Hypothesis is REFUTED:

**Contradicting Patterns**:
✗ Pass@k flat (pass@50 ≈ pass@1) → No coverage benefit
✗ LLM quality ≈ or > canonical → Efficiency maintained
✗ Pass@1 > 50% → High first-attempt efficiency
✗ Low solution diversity → Not exploring solution space

### Ambiguous Results:

**Mixed Evidence Scenarios**:
⚠️ Coverage strong BUT efficiency also strong → Both hypotheses wrong
⚠️ Coverage weak BUT efficiency weak → Different explanation needed
⚠️ Strong task dependency → Hypothesis is context-specific

---

## Timeline and Milestones

**Total Time**: 3600 seconds (60 minutes)

### Phase Breakdown:

| Phase | Duration | Key Deliverables |
|-------|----------|------------------|
| **Planning** | 5 min | This document ✓ |
| **Setup** | 5 min | Environment, dependencies installed |
| **Data Prep** | 5 min | 40 problems selected, prompts formatted |
| **Generation** | 15 min | 4,000 solutions generated (2 models × 40 problems × 50 attempts) |
| **Evaluation** | 10 min | Pass@k calculated, functional correctness |
| **Quality Metrics** | 10 min | Runtime, complexity, diversity measured |
| **Analysis** | 10 min | Statistical tests, visualizations |
| **Documentation** | 10 min | REPORT.md with findings |

**Critical Path**: Generation → Evaluation → Analysis (dependent sequence)

**Buffer**: 5 minutes (8% buffer for debugging)

### Milestones:

- [x] M1: Planning complete (5 min)
- [ ] M2: Environment ready, datasets loaded (10 min)
- [ ] M3: First LLM responses received (15 min)
- [ ] M4: All 4,000 solutions generated (25 min)
- [ ] M5: Pass@k calculated (35 min)
- [ ] M6: Quality metrics collected (45 min)
- [ ] M7: Statistical analysis complete (55 min)
- [ ] M8: REPORT.md written (60 min)

---

## Potential Challenges

### Challenge 1: API Rate Limits
**Risk**: OpenAI/Anthropic may rate limit 4,000 rapid requests
**Mitigation**:
- Implement exponential backoff retry logic
- Use batch API if available
- Reduce k to 25 if necessary (still sufficient for coverage analysis)
- Run sequentially with delays if needed

### Challenge 2: Execution Timeouts
**Risk**: Some generated solutions may have infinite loops or errors
**Mitigation**:
- Use human-eval's safe execution environment (built-in timeouts)
- Set strict time limits (5 seconds per test case)
- Log failures for error analysis

### Challenge 3: Budget Overrun
**Risk**: API costs exceed $100 budget
**Mitigation**:
- Start with 20 problems × 25 attempts = 1,000 calls (cheaper)
- Monitor costs in real-time
- Scale up if budget allows
- Use cheaper models (GPT-4o-mini) if needed

### Challenge 4: Time Constraints
**Risk**: 60 minutes insufficient for all phases
**Mitigation**:
- Prioritize core analyses (pass@k, runtime)
- Drop diversity analysis if time-constrained
- Use pre-existing code from human-eval repo
- Parallelize where possible (generation can be batched)

### Challenge 5: Statistical Power
**Risk**: 40 problems may have insufficient power for some tests
**Mitigation**:
- Focus on effect sizes, not just p-values
- Use non-parametric tests (fewer assumptions)
- Report confidence intervals
- Acknowledge power limitations in discussion

### Challenge 6: Code Quality Metric Collection
**Risk**: Measuring energy/performance may be slow or complex
**Mitigation**:
- Use runtime as primary performance metric (simpler)
- Use radon library for complexity (fast)
- Skip energy measurement (not critical for hypothesis test)
- Focus on metrics feasible within time budget

---

## Success Criteria

### Must-Have (Critical):

1. ✓ **Pass@k analysis complete** for k ∈ {1, 10, 50}
   - Shows coverage (hypothesis test)

2. ✓ **Quality comparison** (LLM vs canonical) on ≥2 metrics
   - Shows efficiency (hypothesis test)

3. ✓ **Statistical significance** reported with confidence intervals
   - Enables valid conclusions

4. ✓ **REPORT.md** documents actual experimental results
   - Primary deliverable

### Should-Have (Important):

5. ◐ Solution diversity analysis
   - Strengthens coverage evidence

6. ◐ Task complexity stratification
   - Tests H3 interaction hypothesis

7. ◐ Comparison to literature findings
   - Validates methodology

### Nice-to-Have (Optional):

8. ○ Multiple LLM comparison (3+ models)
   - Tests generalizability

9. ○ Detailed error analysis
   - Insights into failure modes

10. ○ Visualizations (plots, charts)
    - Improves presentation

**Definition of Success**: At minimum, must-haves 1-4 completed with valid statistical analysis supporting or refuting hypothesis.

---

## Resource Planning

### Computational Requirements

**CPU**: Sufficient for:
- Code execution (lightweight Python functions)
- Statistical analysis (scipy, pandas)
- API calls (network I/O bound, not CPU)

**Memory**: ~2-4 GB
- Dataset: ~2 MB (HumanEval)
- Generated solutions: ~10 MB (4,000 × 2.5 KB average)
- Analysis results: ~1 MB

**Storage**: ~20 MB total
- Datasets: 7 MB
- Code: 2 MB
- Results: ~10 MB (all solutions + metrics)

**Network**: Moderate
- 4,000 API calls (~10 MB total payload)
- Should complete in 10-15 minutes with batching

### Dataset Access

✓ **HumanEval**: Already downloaded in datasets/humaneval/
✓ **Canonical solutions**: Included in HumanEval dataset
✓ **Test cases**: Included in HumanEval dataset

**Verification**:
```python
from datasets import load_from_disk
dataset = load_from_disk('datasets/humaneval')
assert len(dataset['test']) == 164
```

### Code Dependencies

**Required Libraries**:
- `datasets` - HuggingFace dataset loading
- `openai` or `anthropic` - LLM API clients
- `radon` - Cyclomatic complexity
- `numpy`, `scipy` - Statistical analysis
- `pandas` - Data manipulation
- `matplotlib`, `seaborn` - Visualization (optional)

**Installation**:
```bash
source .venv/bin/activate
uv add datasets openai anthropic radon numpy scipy pandas matplotlib seaborn
```

**Evaluation Framework**:
- Use code/human-eval/ (already cloned)
- `pip install -e code/human-eval` for safe execution

### API Access

**Required**:
- OpenAI API key (GPT-4o)
- Anthropic API key (Claude) OR OpenRouter key

**Environment Variables**:
```bash
export OPENAI_API_KEY="..."
export ANTHROPIC_API_KEY="..."  # or OPENROUTER_API_KEY
```

**Cost Estimation**:
- GPT-4o: ~$0.01 per problem (input) + $0.01 per solution (output) = $0.02/call
- 2,000 calls × $0.02 = $40 per model
- 2 models × $40 = $80 total (within $100 budget)

---

## Alternative Approaches Considered

### Alternative 1: Use Pre-Generated LLM Solutions
**Approach**: Download existing benchmark results (e.g., from Papers with Code)
**Pros**: No API costs, instant results
**Cons**: No control over k, can't measure diversity, can't test our specific hypothesis
**Decision**: REJECTED - Need fresh generation for pass@k and diversity analysis

### Alternative 2: Use Open-Source Local Models
**Approach**: Download and run models like CodeLlama, DeepSeek locally
**Pros**: No API costs, unlimited generation
**Cons**: Requires GPU (not available), slow on CPU, outdated models
**Decision**: REJECTED - GPU constraint, state-of-the-art models needed for validity

### Alternative 3: Focus Only on HumanEval (No MBPP)
**Approach**: Use only HumanEval (164 problems)
**Pros**: Well-validated, used in literature
**Cons**: MBPP provides larger sample
**Decision**: ACCEPTED - HumanEval sufficient, MBPP backup if time allows

### Alternative 4: Measure Energy Directly (CodeCarbon)
**Approach**: Use CodeCarbon library to measure energy consumption
**Pros**: Matches Paper #4 methodology exactly
**Cons**: Complex setup, slow measurement, time-intensive
**Decision**: REJECTED - Use runtime as proxy, energy measurement too time-consuming

### Alternative 5: Human Evaluation of Code Quality
**Approach**: Manually review and rate code quality
**Pros**: Captures subjective quality dimensions
**Cons**: Time-intensive, subjective, not scalable
**Decision**: REJECTED - Focus on objective metrics (runtime, complexity)

### Alternative 6: Single Model Deep Dive
**Approach**: Use only GPT-4o, but with k=100 and more problems
**Pros**: Deeper analysis of one model
**Cons**: Generalizability concerns, single point of failure
**Decision**: REJECTED - 2 models provide robustness, k=50 sufficient

---

## Methodology Justification

### Why HumanEval?
✓ Gold standard in LLM code generation (used in Papers #3, #4, #5, #6)
✓ Well-validated with canonical solutions
✓ Appropriate difficulty range for testing hypothesis
✓ Already downloaded and ready to use

### Why Pass@k with k ∈ {1, 10, 50}?
✓ pass@1: Tests efficiency (first-attempt success)
✓ pass@10: Common benchmark in literature (comparable)
✓ pass@50: Sufficient for coverage analysis (diminishing returns beyond)
✓ Literature uses k up to 100, but 50 is sufficient and budget-friendly

### Why GPT-4o and Claude/DeepSeek?
✓ GPT-4o: Current SOTA, used in literature
✓ Claude Sonnet 4.5: Strong coding performance, different architecture
✓ Two models test generalizability of findings
✓ Both within budget constraints

### Why Runtime Instead of Energy?
✓ Runtime strongly correlates with energy (Paper #4 findings)
✓ Much faster to measure (no special setup)
✓ Objective and reproducible
✓ Sufficient proxy for efficiency hypothesis

### Why Stratified Sampling (40 Problems)?
✓ Tests task complexity interaction (H3)
✓ Ensures representation across difficulty levels
✓ Reduces variance in estimates
✓ Fits budget ($80 for 40 problems × 50 × 2 models)

### Why Wilcoxon Signed-Rank Test?
✓ Non-parametric (no normality assumption)
✓ Paired comparison (LLM vs canonical for same problem)
✓ Robust to outliers (common in code metrics)
✓ Appropriate for small sample size (N=40)

---

## Threats to Validity

### Internal Validity Threats

**1. Confounding: Prompt Quality**
- **Threat**: Poor prompts may underestimate LLM capability
- **Mitigation**: Use HumanEval prompts (well-validated, used in literature)
- **Residual Risk**: Low - prompts are standard

**2. Confounding: Model Temperature**
- **Threat**: Temperature affects both coverage and quality
- **Mitigation**: Use temperature=0.7 (balanced), document choice
- **Residual Risk**: Medium - optimal temperature unknown, but consistent across models

**3. Selection Bias: Problem Sampling**
- **Threat**: Non-representative sample may bias results
- **Mitigation**: Stratified sampling across difficulty levels
- **Residual Risk**: Medium - 40/164 is limited, but stratified

**4. Measurement Error: Execution Timing**
- **Threat**: Runtime variability due to system load
- **Mitigation**: Run each solution 3 times, take median
- **Residual Risk**: Low - median robust to noise

### External Validity Threats

**1. Generalization: Benchmark Tasks**
- **Threat**: HumanEval may not represent real-world coding
- **Limitation**: Acknowledged - results apply to algorithmic problems
- **Mitigation**: Compare findings to enterprise studies (Paper #7)

**2. Generalization: Language**
- **Threat**: Results specific to Python
- **Limitation**: Acknowledged - cannot generalize to other languages
- **Mitigation**: Python is most common language in literature

**3. Generalization: Models**
- **Threat**: Only 2 models tested
- **Limitation**: Acknowledged - cannot claim all LLMs behave similarly
- **Mitigation**: Choose models with different architectures (OpenAI vs Anthropic)

**4. Temporal Validity: Model Versions**
- **Threat**: Results may not apply to future model versions
- **Limitation**: Acknowledged - document exact model versions used
- **Mitigation**: Compare to historical benchmarks in literature

### Construct Validity Threats

**1. Coverage Operationalization**
- **Threat**: Pass@k may not fully capture "coverage" concept
- **Mitigation**: Also measure diversity, attempts to first success
- **Residual Risk**: Medium - coverage is multifaceted

**2. Efficiency Operationalization**
- **Threat**: Runtime and complexity may not fully capture "efficiency"
- **Mitigation**: Use multiple metrics (runtime, complexity, pass@1)
- **Residual Risk**: Medium - energy measurement ideal but infeasible

**3. Measurement Validity: Canonical Solutions**
- **Threat**: Canonical solutions may not be optimal
- **Limitation**: Acknowledged - canonical = human-written, not provably optimal
- **Mitigation**: Still valid baseline (human performance)

### Statistical Conclusion Validity Threats

**1. Low Statistical Power**
- **Threat**: N=40 may miss small effects
- **Mitigation**: Report effect sizes and confidence intervals, not just p-values
- **Residual Risk**: Medium - prioritize practical significance

**2. Multiple Comparisons**
- **Threat**: Multiple tests increase false positive risk
- **Mitigation**: Bonferroni correction, report adjusted p-values
- **Residual Risk**: Low - conservative approach

**3. Violated Assumptions**
- **Threat**: Non-normal distributions may invalidate tests
- **Mitigation**: Use non-parametric tests (Wilcoxon, Spearman)
- **Residual Risk**: Low - methods robust

---

## Conclusion

This experimental plan provides a rigorous, feasible approach to testing the hypothesis that "LLMs increase coverage not efficiency" in code generation tasks.

**Key Strengths**:
✓ Grounded in comprehensive literature review (8 papers)
✓ Uses validated benchmarks (HumanEval, gold standard)
✓ Tests multiple dimensions (coverage AND efficiency)
✓ Appropriate statistical methods (non-parametric, effect sizes)
✓ Fits constraints (time, budget, compute)
✓ Clear success criteria and expected outcomes

**Key Limitations** (acknowledged upfront):
- Small sample (40 problems) due to budget
- Only 2 LLMs tested
- Python only (no cross-language generalization)
- Runtime proxy for energy (not direct measurement)
- Short time frame (1 hour) limits depth

**Expected Contribution**:
If successful, this research will provide empirical evidence for the coverage vs efficiency distinction, informing how LLMs should be positioned and used in software development. The findings will either:
1. **Support hypothesis**: LLMs are exploration tools, not efficiency tools
2. **Refute hypothesis**: LLMs provide both coverage and efficiency
3. **Nuanced view**: Context-dependent trade-offs

**Next Steps**: Proceed to implementation phase immediately (fully automated workflow).

---

**Planning Phase Complete** ✓
**Time Elapsed**: ~5 minutes
**Next**: Phase 2 - Environment Setup & Data Preparation
