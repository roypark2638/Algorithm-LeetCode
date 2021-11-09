'''
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
'''


class Solution(object):
    '''
    Bottom Up: Time O(n) Space O(n)
    '''
    # def rob(self, nums):
    #     profits = [0] * (len(nums)+1)
    #     profits[1] = nums[0]
    #     for i in range(2, len(nums)+1):
    #         profits[i] = max(profits[i-2] + nums[i-1], profits[i-1])
    #     return profits[-1]

    '''
    Buttom Up Space Optimized: Time O(n) Space O(1)
    '''

    def rob(self, nums):
        pro1 = 0
        pro2 = nums[0]
        for i in range(2, len(nums)+1):
            temp = max(pro1 + nums[i-1], pro2)
            pro1 = pro2
            pro2 = temp
        return pro2
    '''
    1. Bruth-force recursively: Exponential time O(2^n) Space O(n)
    Use recursive function to find every possible subset of the combination not adjancent values each other. When we are traversing the recursion, we could either include the current value in the nums or not including and pass. When we include current value, we have to remove the next adjacent value to remove the adjancet value. Recurrence relation: leftSum = traverse(nums[0], nums[2:]) and rightSum traverse(0, nums[1:]).
    '''
#     def rob(self, nums):
#         self.maxSum = 0
#         def traverse(nums, curr):
#             if not nums:
#                 return curr
#             left  = traverse(nums[2:], curr + nums[0])
#             right = traverse(nums[1:], curr)

#             self.maxSum = max(self.maxSum, left, right)
#             return curr

#         traverse(nums, 0)
#         return self.maxSum

#     def rob(self, nums):
#         subset = []
#         def traverse(nums, comb):
#             if not nums:
#                 subset.append(comb)
#                 return

#             traverse(nums[2:], comb + [nums[0]])
#             traverse(nums[1:], comb)


#         traverse(nums, [])
#         print(subset)
