'''
39. Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
Example 4:

Input: candidates = [1], target = 1
Output: [[1]]
Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
'''


class Solution(object):
    '''
    Backtracking: Time O(n^(t/m - 1)) Space O(t/m) where n is the number of elements in the array, t is the target, and m is the minimum value among candidates. The execution of the backtracking is unfolded as a DFS traversal in a n-ary tree. The worst case will be n-ary tree's minimum times of tree height.

    Typical backtracking, note that the candidates can be repeated unlimited amount of times. So when we are passing the start in the recursion, we want to make sure the start is from the i because we are including the current value until it's greater than or equal to the target.
    '''

    def combinationSum(self, candidates, target):
        res = []

        def backtracking(start, combo, currSum):
            if target == currSum:
                res.append(combo)
                return
            if target < currSum:
                return
            for i in range(start, len(candidates)):
                backtracking(i, combo + [candidates[i]],
                             currSum + candidates[i])
        backtracking(0, [], 0)
        return res
#     def combinationSum(self, candidates, target):
#         res = []
#         def backtracking(runningTarget, combo, start):
#             if runningTarget < 0:
#                 return
#             if runningTarget == 0:
#                 res.append(list(combo))
#                 return

#             for i in range(start, len(candidates)):
#                 num = candidates[i]
#                 combo.append(num)
#                 # print(runningTarget, num)
#                 backtracking(runningTarget-num, combo, i)
#                 combo.pop()

#         backtracking(target, [], 0)
#         return res
