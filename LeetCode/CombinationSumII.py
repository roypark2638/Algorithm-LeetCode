'''
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''


class Solution(object):
    '''
    Backtracking: Time O(2^n * n) Space O(n)
    - Sort the given candidates array and call a recursion function with a start index, path, and current sum.
    - If current sum is equal to the target, append the path to the final result array.
    - Iterate from the start index to the length of the given array candidates.
        - Calcultae the new current sum if it's greater than target, we can simply return since it's sorted array, we know that the all the later values are going to be greater.
        - Checking duplicates is check if the iteration i index is greater than start index and candidates[i] is eqaul to the the previous value, candidates[i-1]. If yes, we know we had this exact combination, so we can simply continue to the next iteration.
        - Call the recursion function with i+1 and new path and new current sum.
    '''

    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        def dfs(start, path, currSum):
            if currSum == target:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                newCurrSum = currSum + candidates[i]
                if newCurrSum > target:
                    break
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                dfs(i+1, path+[candidates[i]], newCurrSum)
        dfs(0, [], 0)
        return res
