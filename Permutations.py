'''
46. Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

'''


class Solution(object):
    '''
    We will call a recursion function named constructPerms with nums, current perm, len(nums), and result permutations. When the current permutation's length is equal to the length of the given nums array, we want to append the permutation into the final array. Iterate the nums array in the recursion and append the current number into the current perm and build a new number array with the left side and right side of the numbers from current number, and call the recursion function with the new number array. At each end of the iteration of recursion, we want to make sure to pop the perm so that it doesn't carry previous numbers.
    Time O(n!n) Space O(n!) Building permutation takes n! time and space complexisity. If we think about building a set of permutations where the n is 3, at our first position we have the n number of cases. For next position we take away 1. Now we have n-1: 2 number of cases. Finally we take away 1 more and we have 1 number of cases left. For the time complxisty at each iteration we have copy operation, which take antoher n time complexisty.
    '''

    def permute(self, nums):
        permutations = []
        self.constructPermutations(nums, [], permutations, len(nums))
        return permutations

    def constructPermutations(self, nums, perm, perms, n):
        if len(perm) == n:
            perms.append(list(perm))
            return

        for i in range(len(nums)):
            perm.append(nums[i])
            newNums = nums[:i] + nums[i+1:]
            self.constructPermutations(newNums, perm, perms, n)
            perm.pop()
