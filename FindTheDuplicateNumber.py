'''
287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [1,1]
Output: 1
Example 4:

Input: nums = [1,1,2]
Output: 1
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
'''


class Solution(object):
    '''
    Floyd's Algorithm(Tortoise and Hare, cycle detection)
    Use two pointers, slow and fast. slow moves one element at a time and fast move two elements at a time. When both of the pointers meet at the first meeting point, we will move one pointer to the beginning of the starting point. Now, we move both pointers by one element at a time. The second meeting point will be the first duplicate value, which is the enterance of the cycle.
    Time O(n) Space O(1)
    '''

    def findDuplicate(self, nums):
        if len(nums) <= 1:
            return -1
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

    '''
    Set
    If we can modify the given array, we can simply use set to find the duplicate.
    '''
    # def findDuplicate(self, nums):
    #     seen = set()
    #     for num in nums:
    #         if num in seen:
    #             return num
    #         seen.add(num)
    #     return -1

    '''
    Mark with negative
    If we can modify the given array, we can multiply the visited value with negative and if we encounter a negative number, that means that we found the duplicate value.
    '''

    # def findDuplicate(self, nums):
    #     for value in nums:
    #         absValue = abs(value)
    #         if nums[absValue - 1] < 0:
    #             return absValue
    #         nums[absValue-1] *= -1
    #     return -1
