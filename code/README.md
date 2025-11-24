# Code Repositories

This directory contains code repositories and evaluation frameworks for the LLM coverage vs efficiency research.

## Repositories

### 1. OpenAI Human-Eval

**Location**: `code/human-eval/`

**Source**: https://github.com/openai/human-eval

**Purpose**: Official evaluation harness for the HumanEval dataset

**Description**:
This repository provides the code for evaluating large language models on code generation tasks. It implements the pass@k metric and safe code execution for testing generated solutions.

**Key Features**:
- Safe execution environment for untrusted code
- Pass@k metric calculation
- HumanEval dataset (164 problems)
- Example usage and evaluation scripts

**Installation**:
```bash
cd code/human-eval
pip install -e .
```

**Usage**:
```bash
# Evaluate functional correctness
evaluate_functional_correctness data/example_samples.jsonl
```

**Important Files**:
- `human_eval/execution.py`: Safe code execution
- `human_eval/evaluation.py`: Pass@k metric calculation
- `data/HumanEval.jsonl.gz`: Dataset

**Security Note**: This code executes untrusted model-generated code. Review the security considerations in the README before use.

**Relevance to Research**:
Essential for computing pass@k metrics which directly measure coverage (how many attempts needed for success) vs efficiency (first-attempt success rate).

---

### 2. Google Research MBPP

**Location**: `code/mbpp/`

**Source**: https://github.com/google-research/google-research/tree/master/mbpp

**Purpose**: MBPP dataset files and evaluation data

**Description**:
Contains the Mostly Basic Programming Problems (MBPP) dataset in raw format, including the sanitized subset.

**Key Files**:
- `mbpp.jsonl`: Full dataset (974 problems)
- `sanitized-mbpp.json`: Hand-verified subset (427 problems)
- `README.md`: Dataset documentation

**Data Structure**:
```json
{
  "task_id": 11,
  "text": "Write a python function to remove first and last occurrence...",
  "code": "def remove_Occ(s,ch): ...",
  "test_list": ["assert remove_Occ(\"hello\",\"l\") == \"heo\"", ...],
  "test_setup_code": "",
  "challenge_test_list": []
}
```

**Data Splits** (as specified in README):
- Task IDs 1-10: Few-shot prompting examples
- Task IDs 11-510: Test set
- Task IDs 511-600: Validation set
- Task IDs 601-974: Training set

**Usage**:
```python
import json

# Load dataset
with open('code/mbpp/mbpp.jsonl', 'r') as f:
    problems = [json.loads(line) for line in f]

# Get test set (IDs 11-510)
test_problems = [p for p in problems if 11 <= p['task_id'] <= 510]
```

**Relevance to Research**:
Raw data files enable custom evaluation scripts to measure solution diversity, code quality metrics, and pass@k across multiple attempts.

---

## Evaluation Frameworks

Both repositories enable measuring:

1. **Pass@k Metrics**:
   - Pass@1: First-attempt success (efficiency indicator)
   - Pass@10, Pass@100: Multi-attempt success (coverage indicator)

2. **Code Quality**:
   - Can integrate with static analysis tools (SonarQube, pylint)
   - Compare generated code to canonical solutions

3. **Solution Diversity**:
   - Generate multiple solutions per problem
   - Analyze semantic and syntactic diversity
   - Measure exploration vs exploitation

## Integration with Datasets

The code repositories work with the datasets in `../datasets/`:

```python
# Load datasets (HuggingFace format)
from datasets import load_from_disk
humaneval_hf = load_from_disk('../datasets/humaneval')
mbpp_hf = load_from_disk('../datasets/mbpp')

# Load evaluation code
import sys
sys.path.append('code/human-eval')
from human_eval.evaluation import evaluate_functional_correctness

# Combine for evaluation
```

## Recommended Additional Tools

For comprehensive code quality analysis, consider integrating:

### Static Analysis
- **SonarQube**: Code quality, security, maintainability
  - Installation: https://www.sonarsource.com/products/sonarqube/
  - Used in papers: 2508.00700, 2411.10656

- **Pylint**: Python-specific linting
  ```bash
  pip install pylint
  pylint generated_code.py
  ```

### Performance Profiling
- **cProfile**: Runtime performance
  ```python
  import cProfile
  cProfile.run('function()')
  ```

- **memory_profiler**: Memory usage
  ```bash
  pip install memory_profiler
  python -m memory_profiler script.py
  ```

### Energy Efficiency
As measured in paper 2505.20324:
- **CodeCarbon**: Track energy consumption
  ```bash
  pip install codecarbon
  ```

## Usage Examples

### Example 1: Calculate Pass@k

```python
import sys
sys.path.append('code/human-eval')

from human_eval.evaluation import estimate_pass_at_k
import numpy as np

# Simulate results: 164 problems, 10 attempts each
n = 164  # number of problems
c = np.random.binomial(10, 0.3, n)  # correct solutions per problem
k = [1, 5, 10]

# Calculate pass@k
for k_val in k:
    pass_at_k = estimate_pass_at_k(n, c, k_val).mean()
    print(f"pass@{k_val}: {pass_at_k:.2%}")
```

### Example 2: Evaluate Code Quality

```python
import json
from pylint import epylint as lint

# Load MBPP problem
with open('code/mbpp/sanitized-mbpp.json', 'r') as f:
    problems = json.load(f)

problem = problems[0]
code = problem['code']

# Save to file and run pylint
with open('temp_code.py', 'w') as f:
    f.write(code)

(pylint_stdout, pylint_stderr) = lint.py_run('temp_code.py', return_std=True)
print(pylint_stdout.getvalue())
```

### Example 3: Measure Solution Diversity

```python
import difflib
from itertools import combinations

# Generate multiple solutions (pseudo-code)
solutions = [generate_solution(problem) for _ in range(100)]

# Calculate pairwise similarity
similarities = []
for s1, s2 in combinations(solutions, 2):
    ratio = difflib.SequenceMatcher(None, s1, s2).ratio()
    similarities.append(ratio)

avg_similarity = sum(similarities) / len(similarities)
diversity_score = 1 - avg_similarity
print(f"Diversity score: {diversity_score:.2%}")
```

## Testing the Hypothesis

These tools enable testing "LLMs increase coverage not efficiency":

### Coverage Indicators
✓ Pass@10 >> Pass@1: Multiple attempts needed
✓ High solution diversity: Exploring many approaches
✓ Time to first success varies widely

### Efficiency Indicators
✓ Pass@1 score: First-attempt correctness
✓ Code quality metrics: Maintainability, performance
✓ Energy efficiency: Runtime and resource usage
✓ Code compared to canonical solutions

### Expected Outcomes If Hypothesis True
- Pass@100 > Pass@10 >> Pass@1 (coverage benefit from multiple tries)
- High diversity in generated solutions (exploration happening)
- Generated code quality lower than canonical (efficiency concern)
- Energy/performance metrics worse than human code (efficiency concern)

## Dependencies

```bash
# Core evaluation
pip install -e code/human-eval

# Additional tools
pip install pylint pytest black
pip install memory_profiler
pip install codecarbon  # for energy measurement

# For custom analysis
pip install numpy pandas matplotlib seaborn
pip install scikit-learn  # for clustering/diversity metrics
```

## Notes

- **HumanEval execution**: Requires careful sandboxing for security
- **MBPP format**: Raw JSONL, need custom parser or use HuggingFace version
- **Baseline comparisons**: Both datasets include canonical human solutions
- **Metric calculations**: HumanEval repo provides standard pass@k implementation

## Citation

If using these tools in research:

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
