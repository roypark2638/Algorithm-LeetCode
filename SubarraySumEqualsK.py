'''
560. Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''


class Solution(object):
    '''
    Hashmap

    initial variable
    - count, sumCount{}, runningSum

    init sumCount[0] = 1 the reason is

    - Keep track of the runningSum and we will check whether
    runningSum - target exist in our frequency of sumCount hashmap
    If that diff exists in the hashmap, then we will add the number of occurance to our count variable.
    - Keep building sumCount frequency hashmap.
    return count
    Time O(n) Space O(n)
    '''

    def subarraySum(self, nums, k):
        count = 0
        sumCount = {}
        runningSum = 0
        sumCount[0] = 1
        for i in range(len(nums)):
            runningSum += nums[i]
            if runningSum-k in sumCount:
                count += sumCount[runningSum-k]
            if runningSum in sumCount:
                sumCount[runningSum] += 1
            else:
                sumCount[runningSum] = 1
        return count
