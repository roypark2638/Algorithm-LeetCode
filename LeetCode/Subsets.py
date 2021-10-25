'''
78. Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''


class Solution(object):
    '''
    We create a for loop in our subsets fucntion to iterate the given array to n+1( n= len(array)). We call backtracking function in inside of this loop and the iteration index k, will acts as finding a valid solution, if len(path) == k, append to the final result. So we will find all subsets of every length k(0,1,2,...,n).

    The base case is when length of the current path is equal to k, then append the result to the final array. In recursion body, iterate the given array and in the loop, we append a current valid to the path to try a new partial solution. Then call a recursion function. Then, we remove the last element from the path.

    This is a common backtracking templete pattern. first we check if the current candidate is a valid solution. If yes, append to the result array and return. Now enumerate the given array to get next candidate. We append the next candidate to the current candidate to create a new partial solution. Call a backtracking function then we also remove last element(backtrack)
    '''

    def subsets(self, nums):
        res = []

        def backtracking(first=0, path=[]):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(first, len(nums)):
                # create a new paritial solution candidate
                path.append(nums[i])
                # explore futher with the new candidate
                backtracking(i+1, path)
                # backtrack
                path.pop()

        for k in range(len(nums)+1):
            backtracking()
        return res
