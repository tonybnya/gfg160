"""
004. Rotate Array

Given an array arr[].
Rotate the array to the left (counter-clockwise direction) by d steps,
where d is a positive integer. Do the mentioned change in the array in place.

Note: Consider the array as circular.

Examples :

Input: arr[] = [1, 2, 3, 4, 5], d = 2
Output: [3, 4, 5, 1, 2]
Explanation: when rotated by 2 elements, it becomes 3 4 5 1 2.

Input: arr[] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d = 3
Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]
Explanation: when rotated by 3 elements, it becomes 8 10 12 14 16 18 20 2 4 6.

Input: arr[] = [7, 3, 9, 1], d = 9
Output: [3, 9, 1, 7]
Explanation: when we rotate 9 times, we'll get 3 9 1 7 as resultant array.

Constraints:
1 <= arr.size(), d <= 10^5
0 <= arr[i] <= 10^5

Expected Complexities:
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


def rotate_array_1(arr: list[int], d: int) -> list[int]:
    """
    Solution 1: Slicing Array
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n: int = len(arr)
    if d in (0, n):
        return arr
    if d > n:
        d %= n

    return arr[d:] + arr[:d]


def rotate_array_2(arr: list[int], d: int) -> list[int]:
    """
    Solution 2: Use Temporary Array
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n: int = len(arr)
    if d in (0, n):
        return arr
    if d > n:
        d %= n

    temp: list[int] = [0] * n

    i, j = d, 0
    while i < n:
        temp[j] = arr[i]
        j += 1
        i += 1

    i = 0
    while i < d:
        temp[j] = arr[i]
        j += 1
        i += 1

    return temp


def rotate_array_3(arr: list[int], d: int) -> list[int]:
    """
    Solution 3: Reverse in place using Inward Traversal Two Pointers
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def rev(arr: list[int], left: int, right: int) -> None:
        """
        Helper function to reverse an array in place.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    n: int = len(arr)
    if d in (0, n):
        return arr
    if d > n:
        d %= n

    # step 1: reverse the first d elements
    rev(arr, 0, d - 1)

    # step 1: reverse elements from d index to the end
    rev(arr, d, n - 1)

    # step 1: reverse the entire array
    rev(arr, 0, n - 1)

    return arr
