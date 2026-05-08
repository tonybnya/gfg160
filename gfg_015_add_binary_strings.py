"""
Script Name : gfg_015_add_binary_strings.py

Description : 015. Add Binary Strings
Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
Note: The input strings may contain leading zeros but the output string should not have any leading zeros.

Input: s1 = "1101", s2 = "111"
Output: 10100
Explanation:
 1101
+ 111
10100

Input: s1 = "00100", s2 = "010"
Output: 110
Explanation: 
  100
+  10
  110

Constraints:
1 ≤s1.size(), s2.size()≤ 106

Expected Complexities:
Time Complexity: O(n)
Auxiliary Space: O(n)

Author      : @tonybnya
"""


def add_binary(s1: str, s2: str) -> str:
    """
    Complexities:
    TC: O()
    SC: O()
    """
    i, j = len(s1) - 1, len(s2) - 1
    carry: int = 0
    out: list[int] = []

    while i >= 0 or j >= 0 or carry:
        v1: int = ord(s1[i]) - 48 if i >= 0 else 0
        v2: int = ord(s2[j]) - 48 if j >= 0 else 0
        total: int = v1 + v2 + carry
        out.append('1' if total % 2 else '0')
        carry = total // 2
        i -= 1
        j -= 1
    res: str = ''.join(reversed(out)).lstrip('0')
    return res if res != "" else "0"
