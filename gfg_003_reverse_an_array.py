"""
003. Reverse an Array

You are given an array of integers arr[].
Your task is to reverse the given array.

Note: Modify the array in place.

Examples:

Input: arr = [1, 4, 3, 2, 6, 5]
Output: [5, 6, 2, 3, 4, 1]
Explanation: The elements of the array are 1 4 3 2 6 5.
After reversing the array, the first element goes to the last position,
the second element goes to the second last position and so on.
Hence, the answer is 5 6 2 3 4 1.

Input: arr = [4, 5, 2]
Output: [2, 5, 4]
Explanation: The elements of the array are 4 5 2.
The reversed array will be 2 5 4.

Input: arr = [1]
Output: [1]
Explanation: The array has only single element,
hence the reversed array is same as the original.

Constraints:
1<=arr.size()<=10^5
0<=arr[i]<=10^5

Expected Complexities:
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


def reverse_an_array_1(arr: list[int]) -> list[int]:
    """
    Solution 1: Temporary Array
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n: int = len(arr)
    if n < 2:
        return arr
    temp: list[int] = [0] * n
    j: int = 0
    for i in range(n - 1, -1, -1):
        temp[j] = arr[i]
        j += 1
    return temp


def reverse_an_array_2(arr: list[int]) -> list[int]:
    """
    Solution 1: Inward Traversal with two pointers
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n: int = len(arr)
    if n < 2:
        return arr
    l, r = 0, n - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr
