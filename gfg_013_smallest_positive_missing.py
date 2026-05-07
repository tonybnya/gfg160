"""
Script Name : gfg_013_smallest_positive_missing.py

Description : 013. Smallest Positive Missing
You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.

Note: Positive number starts from 1. The array can have negative integers too.

Examples:
Input: arr[] = [2, -3, 4, 1, 1, 7]
Output: 3
Explanation: Smallest positive missing number is 3.

Input: arr[] = [5, 3, 2, 5, 1]
Output: 4
Explanation: Smallest positive missing number is 4.

Input: arr[] = [-8, 0, -1, -4, -3]
Output: 1
Explanation: Smallest positive missing number is 1.

Constraints:
1 ≤ arr.size() ≤ 10^5
-10^6 ≤ arr[i] ≤ 10^6

Expected Complexities:
Time Complexity: O(n)
Auxiliary Space: O(1)

Author      : @tonybnya
"""


# def missing_number(arr: list[int]) -> int:
#     """
#     Naive approach
#     TC: O(nlogn)
#     SC: O(1)
#     """
#     arr.sort()
#     # res will hold the current smallest missing number,
#     # initially set to 1
#     res = 1
#     for num in arr:
#         # If we have found 'res' in the array,
#         # 'res' is no longer missing, so increment it
#         if num == res:
#             res += 1
#         # If the current element is larger than 'res',
#         # 'res' cannot be found in the array,
#         # so it is our final answer
#         elif num > res:
#             break
#     return res


# def missing_number(arr: list[int]) -> int:
#     """
#     Better approach
#     TC: O(n)
#     SC: O(1)
#     """
#     n = len(arr)
#     # To mark the occurrence of elements
#     vis = [False] * n
#     for i in range(n):
#         # if element is in range from 1 to n
#         # then mark it as visited
#         if 0 < arr[i] <= n:
#             vis[arr[i] - 1] = True
#     # Find the first element which is unvisited
#     # in the original array
#     for i in range(1, n + 1):
#         if not vis[i - 1]:
#             return i
#     # if all elements from 1 to n are visited
#     # then n+1 will be first positive missing number
#     return n + 1


# def missing_number(arr: list[int]) -> int:
#     """
#     Expected approach
#     TC: O(n)
#     SC: O(1)
#     """
#     n = len(arr)
#     n = len(arr)
#     for i in range(n):
#         # if arr[i] is within the range 1 to n
#         # and arr[i] is not placed at (arr[i]-1)th index in arr
#         while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:
#             # then swap arr[i] and arr[arr[i]-1] to place arr[i]
#             # to its corresponding index
#             temp = arr[i]
#             arr[i] = arr[arr[i] - 1]
#             arr[temp - 1] = temp
#     # If any number is not at its corresponding index, then it
#     # is the missing number
#     for i in range(1, n + 1):
#         if i != arr[i - 1]:
#             return i
#     # If all number from 1 to n are present 
#     # then n + 1 is smallest missing number
#     return n + 1


# def missing_number(arr: list[int]) -> int:
#     """
#     Alternate Approach - 1
#     TC: O(n)
#     SC: O(1)
#     """
#     def partition(arr):
#         pivotIdx = 0
#         n = len(arr)
#         for i in range(n):
#             # Move positive elements to the left
#             if arr[i] > 0:
#                 arr[i], arr[pivotIdx] = arr[pivotIdx], arr[i]
#                 pivotIdx += 1
#         # return index of the first non-positive number
#         return pivotIdx
#
#     k = partition(arr)
#
#     # Traverse the positive part of the array
#     for i in range(k):
#         # Find the absolute value to get the original number
#         val = abs(arr[i])
#         # If val is within range, then mark the element at
#         # index val-1 to negative
#         if val - 1 < k and arr[val - 1] > 0:
#             arr[val - 1] = -arr[val - 1]
#     # Find first unmarked index
#     for i in range(k):
#         if arr[i] > 0:
#             return i + 1
#     # If all numbers from 1 to k are marked
#     # then missing number is k + 1
#     return k + 1


def missing_number(arr: list[int]) -> int:
    """
    Alternate Approach - 2
    TC: O(n)
    SC: O(1)
    """
    n = len(arr)
    flag = False
    # Check if 1 is present in array or not
    for i in range(n):
        if arr[i] == 1:
            flag = True
            break
    # If 1 is not present
    if not flag:
        return 1
    # Change out of range values to 1
    for i in range(n):
        if arr[i] <= 0 or arr[i] > n:
            arr[i] = 1
    # Mark the occurrence of numbers 
    # directly within the same array
    for i in range(n):
        arr[(arr[i] - 1) % n] += n
    # Finding which index has value less than n
    for i in range(n):
        if arr[i] <= n:
            return i + 1
    # If array has values from 1 to n
    return n + 1
