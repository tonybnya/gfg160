"""
Script Name : test_gfg_013_smallest_positive_missing.py
Description : Describe what this script does
Author      : @tonybnya
"""

import pytest
from gfg_013_smallest_positive_missing import missing_number


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, -3, 4, 1, 1, 7], 3),
        ([5, 3, 2, 5, 1], 4),
        ([-8, 0, -1, -4, -3], 1),

        # Single element
        ([1], 2),
        ([2], 1),
        ([-1], 1),
        ([0], 1),

        # Consecutive positives starting from 1
        ([1, 2, 3, 4, 5], 6),
        ([1, 2, 3], 4),

        # Missing 1
        ([2, 3, 4], 1),
        ([7, 8, 9, 11, 12], 1),

        # Duplicates
        ([1, 1, 2, 2], 3),
        ([2, 2, 2, 2], 1),
        ([1, 1, 1, 1], 2),

        # Includes negatives and zeros
        ([0, -1, -2], 1),
        ([0, 1, 2], 3),
        ([-1, 4, 2, 1, 9, 10], 3),

        # Unsorted arrays
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
        ([6, 5, 4, 3, 2, 1], 7),

        # Missing middle number
        ([1, 2, 4, 5, 6], 3),
        ([2, 3, 1, 5], 4),

        # Large gaps
        ([100, 101, 102], 1),
        ([1, 1000], 2),

        # Repeated mixed values
        ([3, 4, 4, 1, 1], 2),
        ([2, 5, 1, 1, 3], 4),

        # All negatives
        ([-1, -2, -3, -4], 1),
        ([-1000000], 1),

        # Zeros mixed with positives
        ([0, 2, 2, 1, 1], 3),
        ([0, 0, 1, 2], 3),

        # Edge constraint-style values
        ([1000000, -1000000, 1, 2, 3], 4),
        ([1, 2, 3, 1000000], 4),

        # Complex mixed cases
        ([10, -10, 1, 3, 6, 4, 1, 2], 5),
        ([2, 1, 0, -1, 3, 5], 4),
        ([4, 3, 2, 7, 8, 2, 3, 1], 5),

        # Arrays where answer is arr.size() + 1
        ([1, 2, 3, 4], 5),
        ([2, 1], 3),

        # Arrays with only one missing positive in sequence
        ([1, 2, 3, 5], 4),
        ([1, 3, 4, 5], 2),

        # Large duplicate blocks
        ([1, 2, 2, 2, 3, 3, 5], 4),
        ([5, 5, 5, 5], 1),
    ]
)
def test_013_missing_number(arr: list[int], expected: int) -> None:
    assert missing_number(arr) == expected
