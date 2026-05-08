"""
Script Name : test_gfg_015_add_binary_strings.py
Description : Describe what this script does
Author      : @tonybnya
"""

import pytest
from gfg_015_add_binary_strings import add_binary


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("1101", "111", "10100"),
        ("00100", "010", "110"),
        ("0", "0", "0"),
        ("1", "0", "1"),
        ("0", "1", "1"),
        ("1", "1", "10"),
        ("000", "0000", "0"),              # all zeros
        ("0001", "001", "10"),             # leading zeros with carry
        ("1010", "0101", "1111"),
        ("1111", "1", "10000"),            # ripple carry to new digit
        ("1000", "1000", "10000"),
        ("101", "11101", "100010"),
        ("1000000", "1", "1000001"),
        ("1111111", "1111111", "11111110"),# long same-length ones
        ("1"*100, "1", "1" + "0"*100),     # very long carry creation
        ("1010101010", "0101010101", "1111111111"),
        ("0001000", "0000100", "1100"),    # after trimming leading zeros
        ("", "0", "0"),                    # empty string treated as zero (if allowed)
        ("0", "", "0")                     # symmetric empty case
    ]
)
def test_gfg_015_add_binary_strings(s1: str, s2: str, expected: str) -> None:
    assert add_binary(s1, s2) == expected
