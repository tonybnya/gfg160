"""
001. Second Largest

Given an array of positive integers arr[],
return the second largest element from the array.
If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.

Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.

Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.

Constraints:
2 ≤ arr.size() ≤ 10^5
1 ≤ arr[i] ≤ 10^5

Expected Complexities:
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


def get_second_largest_1(arr: list[int]) -> int:
    """
    Solution 1: Sorting
    Time Complexity: O(nlogn)
    Space Complexity: O(1)
    """
    # step 1: sort the arr in place
    arr.sort()  # O(nlogn) TC
    # step 2: traverse the arr in reverse order
    #         start at the second-to-last element (the last is the largest)
    #         return an element which if it is different to the largest
    #         otherwise return -1
    n: int = len(arr)
    for i in range(n - 2, -1, -1):
        if arr[i] != arr[n - 1]:
            return arr[i]
    return -1


def get_second_largest_2(arr: list[int]) -> int:
    """
    Solution 2: Two Pass
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # step 1: get the max number with built-in max() function in O(n) TC
    maximum: int = max(arr)
    # step 2: initialize a variable containing the second largest with -1
    second: int = -1
    # traverse the array
    # whenever an element is different to the max and greater than second
    # the new second is this element
    for n in arr:
        if n != maximum and n > second:
            second = n
    return second


def get_second_largest_3(arr: list[int]) -> int:
    """
    Solution 3: One Pass
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    largest, second_largest = -1, -1
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        if num > second_largest and num != largest:
            second_largest = num
    return second_largest
