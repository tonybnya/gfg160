"""
Script Name : test_gfg_014_atoi.py
Description : Describe what this script does
Author      : @tonybnya
"""

import pytest
from gfg_014_atoi import myatoi


@pytest.mark.parametrize(
    "s, expected",
    [
        ("0", 0),
        ("123", 123),
        ("-123", -123),
        ("+123", 123),
        ("   42", 42),
        ("   -42", -42),
        ("   +0", 0),
        ("  -0012gfg4", -12),
        (" -", 0),
        ("+", 0),
        ("", 0),                       # empty string (if allowed by caller)
        ("   ", 0),
        ("2147483647", 2147483647),    # INT_MAX
        ("2147483648", 2147483647),    # overflow -> clamp to INT_MAX
        ("-2147483648", -2147483648),  # INT_MIN
        ("-2147483649", -2147483648),  # underflow -> clamp to INT_MIN
        ("00000000000000000000123", 123),
        ("9223372036854775808", 2147483647),  # very large positive
        ("-9223372036854775809", -2147483648),# very large negative
        ("  00000", 0),
        ("  +000001", 1),
        ("4193 with words", 4193),
        ("words and 987", 0),
        ("3.14159", 3),
        ("-3.14159", -3),
        ("  +  413", 0),               # plus followed by space => no digits
        ("+-2", 0),                    # invalid sign sequence -> no digits read
        ("  -0012345678901234567890", -2147483648), # long negative overflow
        ("  000002147483647", 2147483647), # exact max with leading zeros
        ("  000002147483648", 2147483647), # just above max with leading zeros
    ]
)
def test_fgf_014_atoi(s: str, expected: int) -> None:
    assert myatoi(s) == expected
