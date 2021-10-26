'''
90. Subsets II
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
'''


class Solution(object):
    #     def subsetsWithDup(self, nums):
    #         res = []
    #         nums.sort()
    #         def backtracking(first = 0, path = []):
    #             if k == len(path):
    #                 newset = path[:]
    #                 if newset not in res:
    #                     res.append(newset)
    #                 return

    #             for i in range(first, len(nums)):
    #                 path.append(nums[i])
    #                 backtracking(i+1, path)
    #                 path.pop()

    #         for k in range(len(nums)+1):
    #             backtracking()
    #         return res

    def subsetsWithDup(self, nums):
        res = []
        nums.sort()

        def dfs(nums, path):
            res.append(path[:])
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[i+1:], path + [nums[i]])

        dfs(nums, [])
        return res
