'''
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

'''


class Solution(object):
    '''
    Binary Search: Time O(logn) Space O(1)
    Take advantage that the given array is sorted in an ascending order possibly rotated at unknown index k. Thus, that index k is the pivot point where every element on the right subarray is smaller than left subarray and both subarrays are sorted.

    - Use binary search to find the k position where previous value is greater than the current value. 
    - Determine which subarray contains the target based on the k position we found.
    - Within the subarray, use binary search to find the index of the target, if the target does not exist, return -1.

    '''

    def search(self, nums, target):
        def getPivot(nums):
            l, r = 0, len(nums)-1
            while l <= r:
                m = l + (r-l)//2
                if m > 0 and nums[m] < nums[m-1]:
                    return m
                elif nums[m] > nums[len(nums)-1]:
                    l = m+1
                else:
                    r = m-1
            return l

        def searchTarget(start, end):
            while start <= end:
                m = start + (end-start)//2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    start = m+1
                else:
                    end = m-1
            return -1

        pivot = getPivot(nums)

        if nums[pivot] == target:
            return pivot
        elif target > nums[-1]:
            return searchTarget(0, pivot)
        else:
            return searchTarget(pivot, len(nums)-1)
