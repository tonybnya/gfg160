"""
002. Move All Zeroes to End

You are given an array arr[] of non-negative integers.
Your task is to move all the zeros in the array to the right end
while maintaining the relative order of the non-zero elements.
The operation must be performed in place,
meaning you should not use extra space for another array.

Examples:

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.

Input: arr[] = [10, 20, 30]
Output: [10, 20, 30]
Explanation: No change in array as there are no 0s.

Input: arr[] = [0, 0]
Output: [0, 0]
Explanation: No change in array as there are all 0s.

Constraints:
1 ≤ arr.size() ≤ 10^5
0 ≤ arr[i] ≤ 10^5

Expected Complexities:
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


def move_all_zeroes_to_end_1(arr: list[int]) -> list[int]:
    """
    Solution 1: Temporary array
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n: int = len(arr)
    temp: list[int] = [0] * n
    i: int = 0
    for n in arr:
        if n != 0:
            temp[i] = n
            i += 1
    return temp


def move_all_zeroes_to_end_2(arr: list[int]) -> list[int]:
    """
    Solution 2: Unidirectional traversal with two pointers
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n: int = len(arr)
    i, j = 0, 0
    while j < n:
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1

    return arr
