"""
Script Name : test_gfg_012_max_circular_subarray_sum.py
Description : Describe what this script does
Author      : @tonybnya
"""

import pytest
from gfg_012_max_circular_subarray_sum import max_circular_sum


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([8, -8, 9, -9, 10, -11, 12], 22),
        ([10, -3, -4, 7, 6, 5, -4, -1], 23),
        ([5, -2, 3, 4], 12),

        # Single element
        ([5], 5),
        ([-5], -5),
        ([0], 0),

        # All positive
        ([1, 2, 3, 4, 5], 15),

        # All negative
        ([-1, -2, -3, -4], -1),
        ([-8, -1, -6, -2, -5], -1),

        # Contains zeros
        ([0, 0, 0], 0),
        ([0, -1, 0], 0),
        ([0, 5, 0], 5),

        # Wrapping gives better result
        ([5, -3, 5], 10),
        ([3, -1, 2, -1], 4),
        ([2, -2, 2, 7, 8, 0], 19),
        ([9, -4, -7, 9], 18),

        # Non-wrapping gives better result
        ([1, -2, 3, -2], 3),
        ([-2, 4, -1, 4, -1, 4, -1], 10),

        # Large negative gap
        ([10, -12, 11], 21),
        ([15, -20, 25], 40),

        # Alternating positive/negative
        ([4, -1, 2, 1], 7),
        ([1, -1, 1, -1, 1, -1, 1], 2),

        # Maximum subarray uses almost all elements
        ([8, -1, 3, 4], 15),
        ([20, -1, -2, -3], 20),

        # Edge wrapping cases
        ([100, -90, 80, -70, 60], 170),
        ([50, -5, 50], 100),

        # Duplicate values
        ([2, 2, 2, 2], 8),
        ([-2, -2, -2], -2),

        # Minimum/maximum constraint-style values
        ([10000, -10000, 10000], 20000),
        ([-10000, -10000, -10000], -10000),

        # Complex mixed cases
        ([6, -1, -2, 6], 12),
        ([7, -5, 4, -3, 9], 17),
        ([1, -2, 3, -2, 5], 7),
        ([2, -1, 2, -1, 2, -1, 2], 6),

        # Cases where excluding minimum subarray is optimal
        ([8, -4, 3, -5, 4], 12),
        ([10, -2, -3, 10], 20),
    ]
)
def test_012_max_circular_subarray_sum(
    arr: list[int],
    expected: int
) -> None:
    assert max_circular_sum(arr) == expected
