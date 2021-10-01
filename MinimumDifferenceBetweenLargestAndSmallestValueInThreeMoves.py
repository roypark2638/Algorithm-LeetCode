'''
1509. Minimum Difference Between Largest and Smallest Value in Three Moves

Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.

Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.

Example 1:

Input: nums = [5,3,2,4]
Output: 0
Explanation: Change the array [5,3,2,4] to [2,2,2,2].
The difference between the maximum and minimum is 2-2 = 0.
Example 2:

Input: nums = [1,5,0,10,14]
Output: 1
Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1]. 
The difference between the maximum and minimum is 1-0 = 1.
'''


'''
- first sort the given nums
- let's say k is the number of moves that we can do
- and for this specific question, the k is 4 for 3 moves(0, 1, 2, 3)
- if the len of nums is <= k(4) then we can return 0
- we have 4 plans
1. nums[-4] - nums[0] -> remove 3 smallest                    
2. nums[-3] - nums[1] -> remove 2 smallest and 1 largest
3. nums[-2] - nums[2] -> remove 1 smallest and 2 largest
4. nums[-1] - nums[3] -> remove 3 largest

e.g.
[1,2,3,4,5,6,7,8]
5 - 1 = 4
6 - 2 = 4
7 - 3 = 4
8 - 4 = 4

[1,3,5,7,9,11,13,15]
9 - 1 = 8
11 - 3 = 8
13 - 5 = 8
15 - 7 = 8

[1,1,1,1,5,6,8,10]
5-1 = 4
6-1 = 5
8-1 = 7
10-1 = 9

[1,1,1,1,1,5,6,7,9,10,15]
7-1 = 6
9-1 = 8
10-1 =9
15-1 =14

Time O(nlogn) Space O(1)
'''
nums = [1, 1, 1, 1, 1, 5, 6, 7, 9, 10, 15]


def minDifference(nums):
    if len(nums) < 5:
        return 0
    nums.sort()
    # res = float("inf")
    # for i in range(4):
    #     res = min(res, nums[len(nums)-4+i] - nums[i])
    return min(b-a for a, b in zip(nums[:4], nums[-4:]))


print(minDifference(nums))
