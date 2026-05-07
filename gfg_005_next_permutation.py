"""
005. Next Permutation

Given an array of integers arr[] representing a permutation, implement the next
permutation that rearranges the numbers into the lexicographically next greater
permutation. If no such permutation exists, rearrange the numbers
into the lowest possible order (i.e., sorted in ascending order).

Note - A permutation of an array of integers refers to a specific arrangement
of its elements in a sequence or linear order.

Examples:

Input: arr = [2, 4, 1, 7, 5, 0]
Output: [2, 4, 5, 0, 1, 7]
Explanation: The next permutation of the given array is {2, 4, 5, 0, 1, 7}.

Input: arr = [3, 2, 1]
Output: [1, 2, 3]
Explanation: As arr[] is the last permutation,
the next permutation is the lowest one.

Input: arr = [3, 4, 2, 5, 1]
Output: [3, 4, 5, 1, 2]
Explanation: The next permutation of the given array is [3, 4, 5, 1, 2].

Constraints:
1 ≤ arr.size() ≤ 10^5
0 ≤ arr[i] ≤ 10^5

Expected Complexities:
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


def next_permutation_1(arr: list[int]) -> list[int]:
    """
    Solution 1: Generate all permutations
    Time Complexity: O(n! * n)
    Space Complexity: O(n! * n)
    """
    from itertools import permutations

    # Get all the permutations, sorted and unique
    perms: list[list[int]] = sorted([list(perm) for perm in set(permutations(arr))])
    m: int = len(perms)

    for i in range(m):
        # a permutation is the current one we are checking for, return the next one
        if perms[i] == arr:
            return perms[(i + 1) % m]

    # if no next permutation found, return the first one in the list of all permutations
    return perms[0]


def next_permutation_2(arr: list[int]) -> list[int]:
    """
    Solution 2: Next Permutation + Reverse in-place
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(arr)

    # Step 1: Find the pivot (first element from the end that is smaller than the next)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    if i >= 0:
        # Step 2: Find the rightmost element greater than arr[i]
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        # Step 3: Swap them
        arr[i], arr[j] = arr[j], arr[i]

    # Step 4: Reverse the suffix (i+1 to end)
    left, right = i + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr
