'''
416. Partition Equal Subset Sum

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
'''
'''
    - calcualte total sum
    - Recursively check whether there exists a subset with target sum
    - base case -> sum == 0 : True
    - n == 0 or sum < 0: False
    - recursion(nums, index +1, sum-nums[index]) || recursion(nums, index+1, sum)
    Time O(n * m) Space O(n) where n is the length of the nums and m is the length of the subTotal
    '''


def canPartition(self, nums):
    total = 0
    for num in nums:
        total += num

    if total % 2 == 1:
        return False
    subTotal = total // 2

    def dfs(i, subTotal, memo={}):
        if subTotal in memo:
            return memo[subTotal]
        if subTotal == 0:
            return True
        if i == len(nums)-1 or subTotal < 0:
            return False
        memo[subTotal] = dfs(i+1, subTotal - nums[i],
                             memo) or dfs(i+1, subTotal, memo)
        return memo[subTotal]
    return dfs(0, subTotal)
