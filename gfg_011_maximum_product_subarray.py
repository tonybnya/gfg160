"""
011. Maximum Product Subarray

Given an array arr[] that contains positive and negative integers
(may contain 0 as well). Find the maximum product that we can get in a subarray
of arr[].

Note: It is guaranteed that the output fits in a 32-bit integer.

Examples

Input: arr[] = [-2, 6, -3, -10, 0, 2]
Output: 180
Explanation: The subarray with maximum product is {6, -3, -10}
with product = 6 * (-3) * (-10) = 180.

Input: arr[] = [-1, -3, -10, 0, 6]
Output: 30
Explanation: The subarray with maximum product is {-3, -10}
with product = (-3) * (-10) = 30.

Input: arr[] = [2, 3, 4]
Output: 24
Explanation: For an array with all positive elements, the result is product
of all elements.

Constraints:
1 ≤ arr.size() ≤ 10^6
-10  ≤  arr[i]  ≤  10

Expected Complexities:
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


def max_product_1(arr: list[int]) -> int:
    """
    Solution 1: Nested Loops
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n: int = len(arr)
    max_p: int = arr[0]

    for i in range(n):
        prod: int = 1
        for j in range(i, n):
            prod *= arr[j]
            max_p = max(max_p, prod)

    return max_p


def max_product_2(arr: list[int]) -> int:
    """
    Solution 2:
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n: int = len(arr)
    current_min: int = arr[0]
    current_max: int = arr[0]
    max_prod: int = arr[0]

    for i in range(1, n):
        temp: int = max(arr[i], arr[i] * current_max, arr[i] * current_min)
        current_min = min(arr[i], arr[i] * current_max, arr[i] * current_min)
        current_max = temp
        max_prod = max(max_prod, current_max)
    return max_prod
