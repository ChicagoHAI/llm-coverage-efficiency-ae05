#!/usr/bin/env python3
"""
Download datasets for LLM coverage vs efficiency research.

This script downloads key code generation benchmarks from HuggingFace:
- HumanEval: 164 hand-crafted programming challenges
- MBPP: ~1000 crowd-sourced Python programming problems
"""

import os
import json
from datasets import load_dataset

def download_humaneval():
    """Download and save HumanEval dataset."""
    print("Downloading HumanEval dataset...")
    try:
        # HumanEval is available through openai_humaneval
        dataset = load_dataset("openai_humaneval")

        # Save to disk
        dataset.save_to_disk("humaneval")
        print(f"✓ HumanEval saved to humaneval/")

        # Save a few examples
        samples = []
        for i, example in enumerate(dataset['test']):
            if i >= 5:
                break
            samples.append({
                'task_id': example['task_id'],
                'prompt': example['prompt'][:200] + '...',  # Truncate for readability
                'canonical_solution': example['canonical_solution'][:100] + '...',
                'test': example['test'][:100] + '...'
            })

        with open('humaneval_samples.json', 'w') as f:
            json.dump(samples, f, indent=2)
        print(f"✓ Saved {len(samples)} sample examples to humaneval_samples.json")

        # Print stats
        print(f"  Total examples: {len(dataset['test'])}")

    except Exception as e:
        print(f"✗ Error downloading HumanEval: {e}")
        return False

    return True

def download_mbpp():
    """Download and save MBPP dataset."""
    print("\nDownloading MBPP dataset...")
    try:
        # Load MBPP from Google Research Datasets
        dataset = load_dataset("google-research-datasets/mbpp", "sanitized")

        # Save to disk
        dataset.save_to_disk("mbpp")
        print(f"✓ MBPP saved to mbpp/")

        # Save a few examples
        samples = []
        for split_name in dataset.keys():
            split_data = dataset[split_name]
            for i, example in enumerate(split_data):
                if i >= 3:
                    break
                samples.append({
                    'split': split_name,
                    'task_id': example['task_id'],
                    'text': example['text'][:200] + '...',
                    'code': example['code'][:100] + '...',
                    'test_list': [t[:50] + '...' for t in example['test_list'][:2]]
                })

        with open('mbpp_samples.json', 'w') as f:
            json.dump(samples, f, indent=2)
        print(f"✓ Saved {len(samples)} sample examples to mbpp_samples.json")

        # Print stats
        for split_name, split_data in dataset.items():
            print(f"  {split_name}: {len(split_data)} examples")

    except Exception as e:
        print(f"✗ Error downloading MBPP: {e}")
        return False

    return True

def main():
    """Main function to download all datasets."""
    print("=" * 70)
    print("Dataset Download Script for LLM Coverage vs Efficiency Research")
    print("=" * 70)

    # Change to datasets directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    success = True
    success &= download_humaneval()
    success &= download_mbpp()

    print("\n" + "=" * 70)
    if success:
        print("✓ All datasets downloaded successfully!")
    else:
        print("⚠ Some datasets failed to download. Check errors above.")
    print("=" * 70)

if __name__ == "__main__":
    main()
