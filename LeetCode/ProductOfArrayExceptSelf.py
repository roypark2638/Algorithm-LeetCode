'''
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''


class Solution(object):
    '''
    1. Use two arrays left and right to hold the product values
    [1,2,3,4]
    [1,1,2,6]
    [24,12,4,1]
    [24,12,8,6]

    2. Use one array
    [1,2,3,4]
    [1,1,2,6]
    running = 1
    [24,12,8,6]

    Time O(n) Space O(1) in which without counting the space for output
    '''

    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        running = 1
        for i in range(len(nums)):
            res[i] = running
            running *= nums[i]

        running = 1
        for i in reversed(range(len(nums))):
            res[i] *= running
            running *= nums[i]
        return res
