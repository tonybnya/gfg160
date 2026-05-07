"""
Script Name : gfg_012_max_circular_subarray_sum.py

Description : 012. Max Circular Subarray Sum
You are given a circular array arr[] of integers, find the maximum possible sum of a non-empty subarray. In a circular array, the subarray can start at the end and wrap around to the beginning. Return the maximum non-empty subarray sum, considering both non-wrapping and wrapping cases.

Examples:

Input: arr[] = [8, -8, 9, -9, 10, -11, 12]
Output: 22
Explanation: Starting from the last element of the array, i.e, 12, and moving in a circular fashion, we have max subarray as 12, 8, -8, 9, -9, 10, which gives maximum sum as 22.

Input: arr[] = [10, -3, -4, 7, 6, 5, -4, -1]
Output: 23
Explanation: Maximum sum of the circular subarray is 23. The subarray is [7, 6, 5, -4, -1, 10].

Input: arr[] = [5, -2, 3, 4]
Output: 12
Explanation: The circular subarray [3, 4, 5] gives the maximum sum of 12.

Constraints:
1 ≤ arr.size() ≤ 10^5
-10^4 ≤ arr[i] ≤ 10^4

Expected Complexities:
Time Complexity: O(n)
Auxiliary Space: O(1)

Author      : @tonybnya
"""


# def max_circular_sum(arr: list[int]) -> int:
#     """
#     Naive approach
#     TC: O(n^2)
#     SC: O(1)
#     """
#     n: int = len(arr)
#     res: int = arr[0]
#     # Subarray that starts with index i
#     for i in range(n):
#         currSum = 0
#         # Considering all possible endpoints of the 
#         # Subarray that begins with index i
#         for j in range(n):
#
#             # Circular index
#             idx = (i + j) % n
#             currSum += arr[idx]
#             res = max(res, currSum)
#     return res


# def max_circular_sum(arr: list[int]) -> int:
#     """
#     Better approach
#     TC: O(n)
#     SC: O(1)
#     """
#     n = len(arr)
#     suffixSum = arr[n - 1]
#     # maxSuffix array to store the value of 
#     # maximum suffix occurred so far.
#     maxSuffix = [0] * (n + 1)
#     maxSuffix[n - 1] = arr[n - 1]
#     for i in range(n - 2, -1, -1):
#         suffixSum += arr[i]
#         maxSuffix[i] = max(maxSuffix[i + 1], suffixSum)
#     # circularSum is Maximum sum of circular subarray
#     circularSum = arr[0]
#     # normalSum is Maximum sum subarray considering 
#     # the array is non-circular
#     normalSum = arr[0]
#     currSum = 0
#     prefix = 0
#     for i in range(n):
#         # Kadane's algorithm
#         currSum = max(currSum + arr[i], arr[i])
#         normalSum = max(normalSum, currSum)
# 		# Calculating maximum Circular Sum
#         prefix += arr[i]
#         circularSum = max(circularSum, prefix + maxSuffix[i + 1])
#     return max(circularSum, normalSum)


def max_circular_sum(arr: list[int]) -> int:
    """
    Expected approach
    TC: O(n)
    SC: O(1)
    """
    totalSum = 0
    currMaxSum = 0
    currMinSum = 0
    maxSum = arr[0]
    minSum = arr[0]
    for i in range(len(arr)):
        # Kadane's to find maximum sum subarray
        currMaxSum = max(currMaxSum + arr[i], arr[i])
        maxSum = max(maxSum, currMaxSum) 
        # Kadane's to find minimum sum subarray
        currMinSum = min(currMinSum + arr[i], arr[i])
        minSum = min(minSum, currMinSum)
        # Sum of all the elements of input array
        totalSum += arr[i]
    normalSum = maxSum
    circularSum = totalSum - minSum
    # If the minimum subarray is equal to total Sum
    # then we just need to return normalSum
    if minSum == totalSum:
        return normalSum
    return max(normalSum, circularSum)
