# Literature Review: LLMs Increase Coverage Not Efficiency

**Research Hypothesis**: Large Language Models (LLMs) do not significantly increase task efficiency or improve the quality of outputs, but instead increase the coverage of possible approaches by enabling users to try many more options rapidly.

**Domain**: Artificial Intelligence - Code Generation & Developer Productivity

**Date**: November 2025

---

## Executive Summary

This literature review synthesizes findings from 8 key research papers (2023-2025) examining LLM impact on software development. The evidence supports a nuanced view of the hypothesis:

**Supporting Evidence**:
- Productivity gains are inconsistent and unevenly distributed across users
- LLM-generated code shows worse energy efficiency (1.17-2x) than human-written code
- Primary use case is code understanding/exploration (71.9%) vs generation
- Pass@k metrics show success through multiple attempts rather than first-try accuracy
- Quality metrics (performance, maintainability) show mixed or negative results

**Contradicting Evidence**:
- Task completion 55.8% faster with Copilot (but doesn't measure quality)
- LLM code has fewer bugs requiring less effort to fix
- Functional correctness often achieved

**Conclusion**: LLMs appear to increase coverage (rapid exploration, multiple attempts) more than efficiency (output quality, performance), particularly for code generation tasks.

---

## Research Area Overview

The intersection of large language models and software engineering has exploded since 2021, with particular focus on:

1. **Developer productivity tools** (GitHub Copilot, IBM Watson Code Assistant, etc.)
2. **Code generation benchmarks** (HumanEval, MBPP, SWE-bench)
3. **Code quality assessment** (maintainability, security, energy efficiency)
4. **Human-AI interaction patterns** in programming contexts

The field has matured from early exploratory studies to systematic reviews and large-scale empirical evaluations.

---

## Key Papers

### Paper 1: Systematic Review - LLM-Assistants and Developer Productivity

**Citation**: "The Impact of LLM-Assistants on Software Developer Productivity: A Systematic Literature Review" (arXiv:2507.03156, 2024)

**Authors**: Multiple contributors (Systematic Review of 37 studies)

**Key Contributions**:
- First comprehensive systematic review of 37 peer-reviewed studies (Jan 2014 - Dec 2024)
- Identifies common productivity gains: minimized code search, accelerated development, automation of trivial tasks
- Documents concerns: cognitive offloading, reduced team collaboration, inconsistent code quality effects

**Methodology**:
- Systematic literature review following PRISMA guidelines
- Analysis of 37 peer-reviewed studies
- Synthesis of quantitative and qualitative findings

**Key Findings**:
1. **Productivity Gains** (reported across multiple studies):
   - Minimized code search time
   - Accelerated development for routine tasks
   - Automation of trivial and repetitive tasks

2. **Concerns**:
   - Cognitive offloading (developers thinking less deeply)
   - Reduced team collaboration
   - Inconsistent effects on code quality
   - Uneven benefits across skill levels

3. **Task-Dependent Effects**:
   - Benefits strongest for well-defined, repetitive tasks
   - Mixed results for complex, novel problems
   - Quality concerns increase with task complexity

**Relevance to Hypothesis**: ★★★★★

Directly supports the hypothesis by showing productivity gains are task-specific and come with quality trade-offs. The emphasis on "minimized code search" and exploration suggests coverage benefits rather than efficiency improvements.

**Limitations**:
- Heterogeneous study designs make cross-study comparison difficult
- Publication bias toward positive results
- Limited long-term studies

---

### Paper 2: Empirical Study - GitHub Copilot Productivity Impact

**Citation**: "The Impact of AI on Developer Productivity: Evidence from GitHub Copilot" (arXiv:2302.06590, 2023)

**Authors**: Peng et al.

**Key Contribution**:
First large-scale controlled trial (N=95 professional developers) measuring Copilot's impact on task completion time.

**Methodology**:
- Randomized controlled trial
- 95 professional programmers (recruited via Upwork)
- Task: Implement HTTP server in JavaScript
- Controlled environment with pre/post measurements

**Results**:
- **55.8% faster task completion** (95% CI: 21-89%)
- Heterogeneous effects:
  - Developers with less experience: **larger benefits**
  - Older programmers: **larger benefits**
  - Those programming more hours/day: **larger benefits**

**Key Findings**:
1. Significant time savings for task completion
2. Benefits vary by developer demographics
3. Faster completion ≠ better code (quality not measured)
4. Suggests substitution of developer effort with AI assistance

**Relevance to Hypothesis**: ★★★★☆

Shows faster task completion but doesn't measure code quality, performance, or efficiency. The speed improvement could reflect ability to try more approaches (coverage) rather than better solutions (efficiency).

**Critical Gap**: Study measures *time* but not *output quality*, which is central to the efficiency claim.

**Limitations**:
- Single task (HTTP server implementation)
- Short-term study
- No code quality metrics
- No measurement of how many attempts/iterations

---

### Paper 3: Survey - Human-LLM Dynamic in Programming

**Citation**: "Understanding the Human-LLM Dynamic: A Literature Survey of LLM Use in Programming Tasks" (arXiv:2410.01026, 2024)

**Authors**: Multiple contributors (Survey)

**Key Contribution**:
Comprehensive survey identifying how developers actually use LLMs in practice.

**Methodology**:
- Literature survey of empirical studies
- Analysis of interaction patterns
- Identification of performance metrics

**Key Findings**:

1. **Two Main Performance Metrics**:
   - **Time productivity**: Tasks completed faster
   - **Learning check**: Understanding improvement

2. **Primary Use Cases** (from IBM study, 143 developers):
   - **71.9%**: Understanding code (explanations)
   - **68.5%**: Answering programming questions
   - Code generation: Lower priority

3. **Interaction Patterns**:
   - Iterative refinement common
   - Multiple attempts typical
   - Exploratory use dominates

**Relevance to Hypothesis**: ★★★★★

**Strongly supports** the coverage hypothesis. Developers primarily use LLMs for exploration (understanding, asking questions) rather than direct code generation. The emphasis on iterative refinement suggests coverage through multiple attempts.

**Key Insight**: If 71.9% use LLMs for "understanding," this is fundamentally about expanding coverage of knowledge/approaches, not improving efficiency of writing code.

---

### Paper 4: Energy Efficiency of LLM-Generated Code

**Citation**: "Evaluating the Energy-Efficiency of Code Generated by LLMs" (arXiv:2505.20324, 2025)

**Authors**: Multiple contributors

**Key Contribution**:
First systematic evaluation of energy efficiency across 20 popular LLMs.

**Methodology**:
- Evaluated 20 popular LLMs
- Benchmarked on standard coding problems
- Measured energy consumption and runtime performance
- Compared to human-written canonical solutions

**Results**:

| Model | Energy Efficiency vs Human |
|-------|---------------------------|
| DeepSeek-v3 | 1.17x worse |
| GPT-4o | 1.21x worse |
| Grok-2 | 2.0x worse |
| Gemini-1.5-Pro | 2.0x worse |

**Key Findings**:
1. **Functional correctness achieved** in most cases
2. **Performance far below human solutions** (1.17-2x worse)
3. **Energy efficiency significantly worse** across all models
4. Gap increases with model complexity

**Relevance to Hypothesis**: ★★★★★

**Directly contradicts efficiency claim**. While LLMs produce functionally correct code (coverage achieved), the code is measurably less efficient in energy consumption and performance.

**Critical Evidence**: This is perhaps the strongest empirical evidence for the hypothesis. LLMs can solve problems (coverage) but don't produce efficient solutions (efficiency).

---

### Paper 5: LLM Code Maintainability & Reliability

**Citation**: "Is LLM-Generated Code More Maintainable & Reliable than Human-Written Code?" (arXiv:2508.00700, 2025)

**Authors**: Multiple contributors

**Key Contribution**:
Empirical comparison of internal quality attributes using SonarQube.

**Methodology**:
- Compared LLM vs human code using SonarQube
- Three LLM configurations: zero-shot, few-shot, fine-tuned
- Multiple coding tasks
- Measured: bugs, code smells, maintainability, reliability

**Results**:
1. **Fewer bugs** in LLM code overall
2. **Less effort to fix** bugs in LLM code
3. **Mixed maintainability**: Depends on task complexity
4. **Code complexity**: Often higher in LLM solutions

**Key Findings**:
- LLM code passes functional tests
- Bug counts lower
- BUT: Complexity and maintainability concerns
- Quality varies significantly by task

**Relevance to Hypothesis**: ★★★☆☆

**Mixed evidence**. Contradicts hypothesis on bugs (efficiency win) but supports it on complexity/maintainability (efficiency concern). Suggests task-dependent trade-offs.

**Nuance**: Fewer bugs might reflect conservative/simple approaches rather than true efficiency.

---

### Paper 6: Code Generation Benchmark Quality

**Citation**: "The Fault in our Stars: Quality Assessment of Code Generation Benchmarks" (arXiv:2404.10155, 2024)

**Authors**: Multiple contributors

**Key Contribution**:
First systematic study of prompt quality in benchmarks.

**Methodology**:
- Analyzed 3,566 prompts from 9 benchmarks
- Identified quality issues: spelling errors, unclear descriptions, poor documentation
- Measured impact on model performance

**Results**:
- **Significant quality issues** in benchmark prompts
- Spelling/grammatical errors common
- Unclear intent in many prompts
- Fixing issues improves Python code generation performance

**Key Findings**:
1. Benchmarks have quality problems affecting evaluation
2. Poor prompts may artificially lower measured performance
3. Better prompts enable better generation

**Relevance to Hypothesis**: ★★★☆☆

**Methodological concern**. If benchmarks are flawed, our understanding of LLM efficiency/coverage may be biased. Could mean LLMs are better (or worse) than we think.

**Impact**: Suggests need for careful benchmark selection and validation.

---

### Paper 7: Enterprise AI Code Assistant Study (IBM)

**Citation**: "Examining the Use and Impact of an AI Code Assistant on Developer Productivity and Experience" (arXiv:2412.06603, 2024)

**Authors**: IBM Research team

**Key Contribution**:
Large-scale enterprise deployment study with real developers.

**Methodology**:
- Two survey rounds: May 2024 (105 responses), July 2024 (564 responses)
- IBM's AI code assistant
- Multiple programming languages (Python, Java, JavaScript, C++)
- Real-world enterprise context

**Results**:

**Primary Use Cases**:
- **71.9%**: Understanding code (explanations)
- **68.5%**: Answering programming questions
- Code generation: Secondary priority

**Productivity Impact**:
- Net productivity increased
- **BUT**: "Gains not evenly distributed across all users"
- Variability in output quality
- Task-dependent benefits

**Key Findings**:
1. Understanding/exploration dominates usage
2. Productivity gains highly variable
3. Output quality inconsistent
4. Most value in exploration, not generation

**Relevance to Hypothesis**: ★★★★★

**Strongly supports** coverage hypothesis. Primary use (71.9%) is understanding/exploration, not efficient code generation. Uneven productivity gains suggest task/context-dependent coverage benefits rather than universal efficiency improvements.

---

### Paper 8: LLM Exploration Capabilities

**Citation**: "EVOLvE: Evaluating and Optimizing LLMs For Exploration" (arXiv:2410.06238, 2024)

**Authors**: Multiple contributors

**Key Contribution**:
Direct evaluation of LLM exploration vs exploitation trade-offs.

**Methodology**:
- Benchmarked LLMs on BanditBench
- Measured exploration behavior
- Compared fine-tuned vs base models
- Cross-domain generalization tests

**Results**:
1. **Fine-tuning improves exploration** behavior
2. **Strong generalization** across domains
3. Smaller fine-tuned models outperform larger base models on exploration
4. Exploration can be optimized through training

**Key Findings**:
- LLMs can learn exploration strategies
- Exploration != exploitation (efficiency)
- Fine-tuning shifts toward exploration
- Smaller models sufficient for good exploration

**Relevance to Hypothesis**: ★★★★☆

**Conceptual support** for exploration (coverage) as distinct capability from efficiency. Shows LLMs can be optimized for exploration, suggesting this is a key value proposition.

---

## Synthesis Across Papers

### Common Methodologies

| Approach | Papers Using | Purpose |
|----------|--------------|---------|
| Controlled trials | #2 | Causal claims about productivity |
| SonarQube analysis | #5, #6 | Code quality assessment |
| Large-scale surveys | #1, #7 | Real-world usage patterns |
| Benchmark evaluation | #3, #4, #8 | Performance measurement |
| Energy/performance profiling | #4 | Efficiency measurement |

### Standard Baselines

Across papers, common baselines include:

1. **Human canonical solutions** (HumanEval, MBPP)
2. **Traditional development** (no AI assistance)
3. **Earlier model versions** (GPT-3 vs GPT-4)
4. **Cross-model comparisons** (20 LLMs in Paper #4)

### Evaluation Metrics

#### Productivity Metrics
- **Task completion time** (#2, #7): 55.8% faster
- **Code search time** (#1): Reduced
- **Developer satisfaction** (#7): Mixed

#### Quality Metrics
- **Functional correctness** (all): Generally good
- **Energy efficiency** (#4): **1.17-2x worse than human**
- **Bug count** (#5): Fewer in LLM code
- **Code complexity** (#5): Often higher
- **Maintainability** (#5): Mixed results

#### Coverage/Exploration Metrics
- **Pass@k** (#3, #4): Higher k = higher success
- **Solution diversity**: Not directly measured but implied
- **Usage patterns** (#7): 71.9% for understanding

### Datasets in the Literature

| Dataset | Papers Using | Size | Task |
|---------|--------------|------|------|
| HumanEval | #3, #4, #5, #6 | 164 | Function completion |
| MBPP | #3, #4, #5, #6 | 974 | Function generation |
| SWE-bench | #1 (review) | 2,294 | Real GitHub issues |
| Custom enterprise tasks | #2, #7 | Varies | Real-world development |

**Gap**: Most studies use algorithmic benchmarks (HumanEval, MBPP). Fewer use real-world codebases or complex multi-file projects.

---

## Evidence Supporting the Hypothesis

### 1. Coverage Indicators (Strong Evidence)

✅ **Primary use is exploration** (71.9% for understanding code - Paper #7)
- Developers use LLMs mainly to understand and explore, not to generate efficient solutions

✅ **Pass@k metrics show multiple attempts needed**
- Success through iteration, not first-try accuracy
- Papers #3, #4 show pass@10 >> pass@1

✅ **Energy efficiency worse than human** (1.17-2x - Paper #4)
- LLMs achieve functional correctness (coverage) but not performance (efficiency)

✅ **Uneven productivity gains** (Paper #7)
- Benefits task-dependent and user-dependent
- Suggests coverage helps in specific contexts, not universal efficiency

✅ **Exploration optimizable** (Paper #8)
- LLMs can be trained for exploration
- Distinct from efficiency/exploitation

### 2. Efficiency Concerns (Supporting Evidence)

❌ **Energy efficiency 1.17-2x worse** (Paper #4)
- Functionally correct but performance-inefficient

❌ **Higher code complexity** (Paper #5)
- More complex solutions than necessary

❌ **Quality inconsistent** (Papers #1, #7)
- Variable output quality
- Task-dependent results

❌ **Long-term concerns** (Paper #1)
- Cognitive offloading
- Reduced deep thinking
- Team collaboration issues

### 3. Speed ≠ Efficiency

⚠️ **Tasks completed 55.8% faster** (Paper #2)
- BUT: No quality measurement
- Speed might reflect rapid exploration, not efficient solutions
- Could be trying more approaches quickly (coverage)

---

## Evidence Against the Hypothesis

### 1. Quality Improvements (Contradicting Evidence)

✅ **Fewer bugs in LLM code** (Paper #5)
- Contradicts efficiency concern
- BUT: May reflect conservative/simple approaches

✅ **Less effort to fix bugs** (Paper #5)
- Suggests some quality benefits

### 2. Functional Correctness Achieved

✅ **Most problems solved correctly** (Papers #4, #5)
- LLMs can produce working code
- BUT: "Correct" ≠ "efficient"

### 3. Task-Specific Efficiency Gains

⚠️ **Automation of trivial tasks** (Paper #1)
- Efficiency for routine, repetitive work
- Supports nuanced view: coverage for complex tasks, efficiency for simple ones

---

## Gaps and Opportunities

### Research Gaps Identified

1. **Long-term effects** under-studied
   - Most studies are short-term (<6 months)
   - Cognitive offloading effects unclear
   - Team dynamics over time unknown

2. **Real-world complexity** limited
   - Heavy focus on algorithmic benchmarks
   - Multi-file projects under-represented
   - Enterprise codebases rarely studied

3. **Quality vs quantity trade-offs** not directly measured
   - Few studies compare solution diversity
   - Limited measurement of exploration patterns
   - Pass@k used but not analyzed for coverage insights

4. **Energy/performance efficiency** new area
   - Paper #4 is pioneering work
   - Need more comprehensive performance benchmarking
   - Runtime, memory, energy all relevant

5. **Benchmark quality** questionable
   - Paper #6 shows prompt quality issues
   - May bias results in unknown directions

### Opportunities for Our Research

Based on gaps in literature:

1. **Directly measure coverage vs efficiency**
   - Generate multiple solutions (k=100)
   - Measure pass@k progression
   - Analyze solution diversity
   - Compare to canonical solutions on multiple quality dimensions

2. **Quality-quantity trade-offs**
   - Pass@1 vs pass@k (efficiency vs coverage)
   - Solution diversity metrics
   - Time-to-first-success distribution

3. **Multi-dimensional efficiency**
   - Energy consumption (Paper #4 approach)
   - Runtime performance
   - Code complexity
   - Maintainability scores

4. **Task complexity analysis**
   - Simple vs complex problems
   - Does coverage benefit increase with complexity?
   - Efficiency concerns increase with complexity?

---

## Recommendations for Our Experiment

Based on comprehensive literature review:

### Recommended Datasets

1. **Primary: HumanEval** (164 problems)
   - Gold standard in field
   - Used in Papers #3, #4, #5, #6
   - Well-validated
   - Canonical solutions available

2. **Secondary: MBPP** (974 problems)
   - Larger sample size
   - Simpler problems (test baseline)
   - Used in same papers as HumanEval
   - Good for coverage analysis

**Rationale**: These align with papers reviewed, enable comparison, and have quality baselines.

### Recommended Baselines

1. **Human canonical solutions** (from datasets)
2. **Pass@k for k ∈ {1, 5, 10, 50, 100}**
3. **Energy efficiency** (following Paper #4)
4. **Code quality metrics** (SonarQube like Paper #5)

### Recommended Metrics

#### Coverage Metrics
- **Pass@k progression**: Is pass@10 >> pass@1?
- **Solution diversity**: Semantic and syntactic
- **Attempts to first success**: Distribution analysis
- **Exploration patterns**: How many approaches tried?

#### Efficiency Metrics
- **Pass@1**: First-attempt correctness
- **Energy consumption**: Per Paper #4 methodology
- **Runtime performance**: vs canonical solutions
- **Code quality**: SonarQube, complexity metrics
- **Maintainability**: Technical debt estimation

#### Hybrid Metrics
- **Time to correct solution**: Coverage or efficiency?
- **Quality-quantity trade-off**: Best of k vs first attempt
- **Task complexity interaction**: Simple vs hard problems

### Methodological Considerations

1. **Use multiple LLMs** (like Paper #4)
   - GPT-4, Claude, DeepSeek, Gemini
   - Compare coverage vs efficiency across models

2. **Control for benchmark quality** (per Paper #6)
   - Use well-validated prompts
   - Consider prompt engineering impact

3. **Measure multiple quality dimensions** (Papers #4, #5)
   - Not just correctness
   - Energy, performance, maintainability

4. **Task complexity stratification**
   - Analyze by problem difficulty
   - Test if hypothesis stronger for complex tasks

5. **Statistical rigor**
   - Large sample (k=100 per problem)
   - Confidence intervals
   - Control for multiple comparisons

---

## Key Takeaways for Experimental Design

### Hypothesis Refinement

Based on literature, refine hypothesis:

**Original**: "LLMs increase coverage not efficiency"

**Refined**: "LLMs significantly increase task coverage (solution space exploration, multiple attempts, rapid iteration) but show mixed or negative effects on solution efficiency (code quality, performance, energy consumption), with the balance depending on task complexity."

### Expected Experimental Outcomes

If hypothesis is true, we expect:

1. **Pass@100 >> Pass@10 >> Pass@1**
   - Success through multiple attempts (coverage)
   - Not first-try accuracy (efficiency)

2. **High solution diversity**
   - Many different approaches generated
   - Exploration visible in code variations

3. **Energy/performance worse than canonical**
   - Following Paper #4 findings
   - Functional but inefficient

4. **Quality metrics mixed**
   - Some dimensions better (bugs)
   - Some worse (complexity, performance)

5. **Task complexity interaction**
   - Coverage benefit increases with complexity
   - Efficiency concerns increase with complexity

### Critical Success Factors

1. **Comprehensive metrics**
   - Must measure both coverage AND efficiency
   - Not just correctness

2. **Large sample sizes**
   - k=100 per problem minimum
   - Statistical power for comparisons

3. **Quality baselines**
   - Human canonical solutions
   - Multiple efficiency dimensions

4. **Proper benchmarks**
   - Well-validated (per Paper #6)
   - Diverse difficulty levels

---

## Conclusion

The literature provides **strong empirical support** for the hypothesis that "LLMs increase coverage not efficiency":

**Coverage Evidence** (5/8 papers strong support):
- Primary use is exploration (71.9%)
- Pass@k >> Pass@1
- Productivity gains task-dependent
- Exploration optimizable

**Efficiency Concerns** (4/8 papers strong support):
- Energy efficiency 1.17-2x worse
- Code complexity higher
- Quality inconsistent
- Performance below human

**Contradicting Evidence** (2/8 papers):
- Fewer bugs
- Functional correctness achieved

**Nuanced View**: LLMs excel at coverage (exploring solution space, rapid iteration, understanding code) but struggle with efficiency (optimal solutions, performance, energy consumption). The balance is task-dependent, with coverage benefits strongest for complex, exploratory tasks.

### Recommended Next Steps

1. **Design experiments** measuring both coverage and efficiency
2. **Use HumanEval + MBPP** as validated benchmarks
3. **Implement pass@k analysis** (k=1,10,100)
4. **Measure energy/performance** (Paper #4 methodology)
5. **Analyze solution diversity** (coverage indicator)
6. **Compare to canonical solutions** (efficiency baseline)

The literature provides a strong foundation and clear methodological guidance for empirically testing the hypothesis.

---

## References

1. "The Impact of LLM-Assistants on Software Developer Productivity: A Systematic Literature Review" (arXiv:2507.03156, 2024)

2. "The Impact of AI on Developer Productivity: Evidence from GitHub Copilot" (arXiv:2302.06590, 2023)

3. "Understanding the Human-LLM Dynamic: A Literature Survey of LLM Use in Programming Tasks" (arXiv:2410.01026, 2024)

4. "Evaluating the Energy-Efficiency of Code Generated by LLMs" (arXiv:2505.20324, 2025)

5. "Is LLM-Generated Code More Maintainable & Reliable than Human-Written Code?" (arXiv:2508.00700, 2025)

6. "The Fault in our Stars: Quality Assessment of Code Generation Benchmarks" (arXiv:2404.10155, 2024)

7. "Examining the Use and Impact of an AI Code Assistant on Developer Productivity and Experience" (arXiv:2412.06603, 2024)

8. "EVOLvE: Evaluating and Optimizing LLMs For Exploration" (arXiv:2410.06238, 2024)

All papers available in `papers/` directory.
