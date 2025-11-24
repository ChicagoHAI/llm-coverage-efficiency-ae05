#!/usr/bin/env python3
"""Download MBPP dataset separately."""

import json
from datasets import load_dataset

print("Downloading MBPP dataset (full version)...")
try:
    # Try the full version instead of sanitized
    dataset = load_dataset("mbpp", "full")

    # Save to disk
    dataset.save_to_disk("mbpp")
    print(f"✓ MBPP saved to mbpp/")

    # Save a few examples
    samples = []
    for split_name in dataset.keys():
        split_data = dataset[split_name]
        print(f"  {split_name}: {len(split_data)} examples")

        # Print first example to understand structure
        if len(split_data) > 0:
            print(f"  Example keys: {split_data[0].keys()}")
            for i, example in enumerate(split_data):
                if i >= 3:
                    break
                # Adapt to actual structure
                sample = {
                    'split': split_name,
                    'task_id': example.get('task_id', i),
                }
                # Add fields that exist
                for key in example.keys():
                    if isinstance(example[key], str) and len(example[key]) < 500:
                        sample[key] = example[key]
                    elif isinstance(example[key], list) and len(example[key]) <= 5:
                        sample[key] = example[key]

                samples.append(sample)

    with open('mbpp_samples.json', 'w') as f:
        json.dump(samples, f, indent=2)
    print(f"✓ Saved {len(samples)} sample examples to mbpp_samples.json")

except Exception as e:
    print(f"✗ Error: {e}")
    print("\nTrying alternative approach...")

    try:
        dataset = load_dataset("google-research-datasets/mbpp", "full")
        dataset.save_to_disk("mbpp")

        # Print stats
        for split_name, split_data in dataset.items():
            print(f"  {split_name}: {len(split_data)} examples")
            if len(split_data) > 0:
                print(f"  Example: {split_data[0]}")

        print("✓ MBPP downloaded successfully with alternative method")
    except Exception as e2:
        print(f"✗ Alternative also failed: {e2}")
