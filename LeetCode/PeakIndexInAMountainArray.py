'''
852. Peak Index in a Mountain Array

Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

Example 1:

Input: arr = [0,1,0]
Output: 1

Example 2:
Input: arr = [0,2,1,0]
Output: 1

Example 3:
Input: arr = [0,10,5,2]
Output: 1

Example 4:
Input: arr = [3,4,5,1]
Output: 2

Example 5:
Input: arr = [24,69,100,99,79,78,67,36,26,19]
Output: 2
'''
arr = [3, 4, 5, 1]

# Bruth Force
# Time O(n) Space O(1)


def foo1(arr):
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            return i
    return -1


# Binary Search
# Time O(logn) Space O(1)
def foo2(arr):
    l, r = 1, len(arr) - 2
    while l <= r:
        m = (l+r) // 2
        if arr[m] > arr[m+1] and arr[m] > arr[m-1]:
            return m
        elif arr[m] < arr[m+1]:
            l = m + 1
        elif arr[m] < arr[m-1]:
            r = m - 1
    return l
