# Datasets for LLM Coverage vs Efficiency Research

This directory contains datasets for evaluating the hypothesis: "LLMs increases coverage not efficiency."

**IMPORTANT**: Data files are NOT committed to git due to size. Follow the download instructions below.

## Overview

The research examines whether LLMs primarily improve task coverage (enabling more exploration and attempts) rather than task efficiency (quality and performance of outputs). These datasets enable empirical evaluation of code generation quality, diversity, and performance.

## Datasets

### 1. HumanEval

#### Overview
- **Source**: OpenAI
- **HuggingFace**: `openai_humaneval`
- **Size**: 164 hand-crafted programming challenges
- **Format**: HuggingFace Dataset
- **Task**: Python function completion from docstrings
- **Evaluation**: Functional correctness via unit tests
- **License**: MIT

#### Why This Dataset?
HumanEval is the gold standard for evaluating LLM code generation capabilities. It's highly relevant for our hypothesis because:
- Allows measuring pass@k (coverage): how many attempts needed to get correct solution
- Enables comparison of solution diversity (coverage metric)
- Tests functional correctness without measuring efficiency/performance
- Widely used in papers we reviewed

#### Download Instructions

**Using Python script (recommended):**
```bash
cd datasets
python3 download_datasets.py
```

**Manual download with Python:**
```python
from datasets import load_dataset

# Download HumanEval
dataset = load_dataset("openai_humaneval")
dataset.save_to_disk("datasets/humaneval")
```

**Alternative using HuggingFace CLI:**
```bash
pip install huggingface_hub[cli]
huggingface-cli download openai_humaneval --repo-type dataset --local-dir datasets/humaneval
```

#### Loading the Dataset

Once downloaded:
```python
from datasets import load_from_disk

dataset = load_from_disk("datasets/humaneval")

# Access examples
for example in dataset['test']:
    print(f"Task: {example['task_id']}")
    print(f"Prompt: {example['prompt']}")
    print(f"Solution: {example['canonical_solution']}")
    print(f"Tests: {example['test']}")
```

#### Sample Data

Example challenge from HumanEval:
```python
# Task: HumanEval/0
# Prompt:
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer
    to each other than given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
```

See `humaneval_samples.json` for 5 complete examples.

#### Evaluation Metrics

- **pass@1**: Probability that a single generated solution passes all tests
- **pass@10**: Probability that at least 1 of 10 solutions passes all tests
- **pass@100**: Probability that at least 1 of 100 solutions passes all tests

**Relevance to hypothesis**: Higher pass@k for k>1 suggests LLMs provide coverage through multiple attempts rather than efficiency through single correct solutions.

### 2. MBPP (Mostly Basic Python Problems)

#### Overview
- **Source**: Google Research
- **HuggingFace**: `google-research-datasets/mbpp`
- **Size**: 974 crowd-sourced Python programming problems
  - Train: 374 examples
  - Test: 500 examples
  - Validation: 90 examples
  - Prompt: 10 examples
- **Format**: HuggingFace Dataset
- **Task**: Python function generation from natural language descriptions
- **Evaluation**: Functional correctness via 3 automated test cases per problem
- **License**: Apache 2.0

#### Why This Dataset?
MBPP complements HumanEval with entry-level programming problems:
- Larger dataset (974 vs 164) for more robust evaluation
- Simpler problems test baseline competence
- Natural language descriptions (vs docstrings) test understanding
- Crowd-sourced reflects real developer queries
- Used extensively in papers we reviewed (energy efficiency, code quality studies)

#### Download Instructions

**Using Python script (recommended):**
```bash
cd datasets
python3 download_datasets.py
```

**Manual download with Python:**
```python
from datasets import load_dataset

# Download MBPP
dataset = load_dataset("google-research-datasets/mbpp")
dataset.save_to_disk("datasets/mbpp")
```

**Alternative:**
```bash
pip install datasets
python3 -c "from datasets import load_dataset; load_dataset('google-research-datasets/mbpp').save_to_disk('datasets/mbpp')"
```

#### Loading the Dataset

Once downloaded:
```python
from datasets import load_from_disk

dataset = load_from_disk("datasets/mbpp")

# Access training examples
for example in dataset['train']:
    print(f"Task ID: {example['task_id']}")
    print(f"Description: {example['text']}")
    print(f"Code: {example['code']}")
    print(f"Tests: {example['test_list']}")
```

#### Sample Data

Example from MBPP:
```python
{
  "task_id": 11,
  "text": "Write a python function to remove first and last occurrence of a given character from the string.",
  "code": "def remove_Occ(s,ch): \n    for i in range(len(s)): \n        if (s[i] == ch): \n            s = s[0 : i] + s[i + 1:] \n            break\n    for i in range(len(s) - 1,-1,-1):  \n        if (s[i] == ch): \n            s = s[0 : i] + s[i + 1:] \n            break\n    return s",
  "test_list": [
    "assert remove_Occ(\"hello\",\"l\") == \"heo\"",
    "assert remove_Occ(\"abcda\",\"a\") == \"bcd\"",
    "assert remove_Occ(\"PHP\",\"P\") == \"H\""
  ]
}
```

#### Dataset Splits

- **train** (374): For training or few-shot prompting
- **test** (500): Primary evaluation set
- **validation** (90): For hyperparameter tuning
- **prompt** (10): Examples for prompt engineering

#### Evaluation Metrics

- **Functional correctness**: % of solutions passing all test cases
- **First-attempt accuracy**: pass@1 metric
- **Coverage metrics**: pass@k for k=1,10,100
- **Code quality**: Can analyze generated code with static analysis tools

**Relevance to hypothesis**: Compare pass@1 vs pass@10 to measure whether LLMs succeed through exploration (many attempts) vs efficiency (correct on first try).

## Dataset Statistics Summary

| Dataset | Size | Task | Avg Tests/Problem | Difficulty | Year |
|---------|------|------|-------------------|------------|------|
| HumanEval | 164 | Function completion | 7.7 | Medium-Hard | 2021 |
| MBPP | 974 | Function generation | 3.0 | Easy-Medium | 2021 |

## Experimental Use Cases

### Testing the Hypothesis

These datasets enable several experiments relevant to our hypothesis:

#### 1. Coverage vs Efficiency Analysis
```python
# Generate k solutions per problem
for k in [1, 5, 10, 50, 100]:
    pass_at_k = evaluate(generate_solutions(problems, n=k))
    print(f"pass@{k}: {pass_at_k}")

# If pass@1 << pass@10, suggests coverage benefit
# If pass@1 ≈ pass@10, suggests efficiency benefit
```

#### 2. Code Quality vs Quantity
```python
# Measure quality of successful solutions
for solution in successful_solutions:
    complexity = calculate_complexity(solution)
    performance = benchmark_runtime(solution)
    energy = measure_energy_efficiency(solution)

# Compare to human baselines from canonical_solution
```

#### 3. Solution Diversity (Coverage Indicator)
```python
# Measure diversity in generated solutions
solutions = [generate_solution(problem) for _ in range(100)]
diversity = calculate_solution_diversity(solutions)

# High diversity = high coverage
# Low diversity = focused efficiency
```

#### 4. Time to First Success
```python
# Simulate iterative development
attempts = []
for i in range(max_attempts):
    solution = generate_solution(problem)
    if passes_tests(solution):
        attempts.append(i + 1)
        break

# Distribution of attempts reveals coverage pattern
```

## Comparison to Papers

Our datasets align with those used in reviewed papers:

| Paper | Datasets Used | Our Coverage |
|-------|---------------|--------------|
| Energy Efficiency Study (2505.20324) | HumanEval, MBPP | ✓ Both |
| Code Quality (2508.00700) | HumanEval, MBPP, custom | ✓ Core benchmarks |
| Benchmark Quality (2404.10155) | HumanEval, MBPP, 7 others | ✓ Main ones |
| Copilot Study (2302.06590) | Custom tasks | ○ Different domain |

## Additional Dataset Candidates

Other datasets relevant to the hypothesis but not downloaded (due to size/complexity):

1. **SWE-bench** (2,294 real GitHub issues)
   - Too large and complex for initial experiments
   - Requires full repository context
   - Better for follow-up work

2. **CodeXGLUE** (14 sub-datasets)
   - Comprehensive but overlaps with HumanEval/MBPP
   - Could add for expanded evaluation

3. **LeetCode** (proprietary)
   - Not freely available
   - Similar to HumanEval in spirit

## Notes and Limitations

### Dataset Biases
- **Language bias**: Both datasets are Python-only
- **Problem type bias**: Algorithmic/data structure problems
- **Simplicity bias**: MBPP focuses on basic problems
- **Test coverage**: Limited tests may miss edge cases

### Relevance to Hypothesis
✓ **Good for**: Measuring pass@k (coverage), solution diversity, functional correctness
✗ **Limited for**: Real-world task complexity, multi-file projects, efficiency under time constraints

### Size Considerations
- HumanEval: ~2 MB on disk
- MBPP: ~5 MB on disk
- Total: ~7 MB (easily manageable)

## Citation

If you use these datasets in research, cite:

**HumanEval:**
```
@article{chen2021evaluating,
  title={Evaluating Large Language Models Trained on Code},
  author={Chen, Mark and Tworek, Jerry and Jun, Heewoo and others},
  journal={arXiv preprint arXiv:2107.03374},
  year={2021}
}
```

**MBPP:**
```
@article{austin2021program,
  title={Program Synthesis with Large Language Models},
  author={Austin, Jacob and Odena, Augustus and Nye, Maxwell and others},
  journal={arXiv preprint arXiv:2108.07732},
  year={2021}
}
```

## Quick Start

```bash
# 1. Download datasets
cd datasets
python3 download_datasets.py

# 2. Verify downloads
python3 -c "from datasets import load_from_disk; print(len(load_from_disk('humaneval')['test']))"
# Should print: 164

python3 -c "from datasets import load_from_disk; d=load_from_disk('mbpp'); print(f'train:{len(d['train'])}, test:{len(d['test'])}')"
# Should print: train:374, test:500

# 3. Explore samples
cat humaneval_samples.json
```

## Dependencies

```bash
pip install datasets transformers
```

## Support

For issues with:
- **HumanEval**: See https://github.com/openai/human-eval
- **MBPP**: See https://github.com/google-research/google-research/tree/master/mbpp
- **This research**: Check project README or create an issue
