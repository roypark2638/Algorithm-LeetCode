'''
300. Longest Increasing Subsequence
Medium

9419

193

Add to List

Share
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
'''


class Solution(object):
    '''
    Dynamic Programming
    Tabulation: Time O(n^2) Space O(n)
    Iterate from the end of the nums array and at the each index, solve the subproblem by finding how many subsequence can be made at the each index. Then use the subproblem solution to solve the next subproblem until we finally solve the entire nums array elements and return the longest length.
    '''

    def lengthOfLIS(self, nums):
        longest = 1
        sizes = [1] * len(nums)
        for i in reversed(range(len(nums)-1)):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    sizes[i] = max(sizes[i], 1 + sizes[j])
            longest = max(longest, sizes[i])
        return longest
