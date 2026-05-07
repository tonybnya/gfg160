"""
006. Majority Element II

You are given an array of integer arr[] where each number represents a vote
to a candidate. Return the candidates that have votes greater than one-third
of the total votes, If there's not a majority vote, return an empty array.

Note: The answer should be returned in an increasing format.

Examples:

Input: arr[] = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
Output: [5, 6]
Explanation: 5 and 6 occur more n/3 times.

Input: arr[] = [1, 2, 3, 4, 5]
Output: []
Explanation: o candidate occur more than n/3 times.

Constraint:
1 <= arr.size() <= 10^6
-109 <= arr[i] <= 10^9

Expected Complexities:
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


def find_majority_1(arr: list[int]) -> None:
    """
    Solution 1: Use Hashmap
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # step 1: set an empty dict
    hmap: dict[int, int] = {}  # O(n) SC
    # step 2: traverse arr and map each num with its occurrences
    for n in arr:
        hmap[n] = hmap.get(n, 0) + 1
    # step 3: set an empty list
    # at most, 2 elements can occur more than n/3 times, so SC is O(1)
    ans: list[int] = []
    n: int = len(arr)
    mv: int = n // 3
    for key, val in hmap.items():
        if val > mv:
            ans.append(key)

    # sorting a list with at most 2 elements is O(n) TC
    # return sorted(lst) if ans else []
    # or
    # as we know that there are at most 2 elements
    # we can just swap the two elements if they are not sorted
    if len(ans) == 2 and ans[0] > ans[-1]:
        ans[0], ans[-1] = ans[-1], ans[0]
    return ans


def find_majority_2(arr: list[int]) -> list[int]:
    """
    Solution 2: Moore’s Voting Algorithm (optimized for n/3)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not arr:
        return []

    # Step 1: Find potential candidates
    candidate1, candidate2 = None, None
    count1, count2 = 0, 0

    for num in arr:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # Step 2: Verify the candidates
    count1 = count2 = 0
    for num in arr:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    ans = []
    n = len(arr)
    if count1 > n // 3:
        ans.append(candidate1)
    if count2 > n // 3:
        ans.append(candidate2)

    return sorted(ans)
