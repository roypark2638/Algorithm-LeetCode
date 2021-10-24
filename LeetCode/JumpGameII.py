'''
45. Jump Game II

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.


Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000


'''


class Solution(object):
    '''
    Recursive Bruth Froce: Time O(n!) Space O(n). At each index i we have n-1 choices and we recursively explore each of them till end. So we require O(n*(n-1)*(n-2)... 1) = O(n!)

    We start at index 0 and are required to reach index n-1 (where n = len(nums)). We can't always do the maximum jump at each index. This can be easily vertified by looking at the example test cases.
    So, at each position, we can use a jump size of anywhere in the range [1, nums[pos]]. The final answer will be the minimum jumps required. We can recursively solve this problem as -
    - If we reach the index n-1 return 0, signifying that we need 0 more jumps.
    - Else recurse for each jump size possible from the current index and return the answer in which we require the minimum number of jumps
    '''
    # def jump(self, nums, pos = 0):
    #     if pos == len(nums)- 1:
    #         return 0
    #     minJump = float('inf')
    #     for i in range(1, nums[pos]+1):
    #         minJump = min(minJump, 1 + self.jump(nums, pos + i))
    #     return minJump
    '''
    Recursive Memoization: Time O(n^2) Space O(n)
    We can see that for a given position, we are repeatedly calculating the same answer over and over again. The jumps required to reach for a given index on the path remains fixed and can be stored in memo dictionary to avoid re-calculations.
    '''
    # def jump(self, nums):
    #     memo={}
    #     def dfs(nums, pos):
    #         if pos in memo:
    #             return memo[pos]
    #         if pos >= len(nums)-1:
    #             return 0
    #         minJump = float('inf')
    #         for i in range(1, nums[pos]+1):
    #             minJump = min(minJump, 1 + dfs(nums, pos+i))
    #         memo[pos] = minJump
    #         return memo[pos]
    #     return dfs(nums, 0)

    '''
    Greedy BFS: Time O(n) Space O(1)
    We can iterate over all indices maintaining the furthest reachable position from current index, maxReachable and currently furthest reached position, lastJumpedPos. Everytime we will try to update lastJumpedPos to futheest possible reachable index, maxReachable.
    
    Updating the lastJumpedPos separately from maxReachable allows us to maintain track of minimum jumps required. Each time astJumpedPos is updated, jumps will also be updated and store the minimum jumps required to reach lastJumpedPos (On the contrary, updating jumps with maxReachable won't give the optimal (minimum possible) value of jumps required).
    
    We will just return it as soon as lastJumpedPos reaches(or exceeds) last index.
    
    1. maxReachable = max(maxReachable, i+nums[i]): updating the range of next level. Similar to queue.push(node) step of BFS but here we are only greedily storing the max reachable index on next level.
    2. i == lastJumpPos: When it becomes true, current level iteration has been completed.
    3. lastJumpedPos = maxReachable: Set range til which we need to iterate the next level.
    4. jumps+=1: Move on to the next level.
    5. return jumps: The final answer will be numer of levels in BFS traversal.
    '''

    def jump(self, nums):
        i = jumps = maxReachable = lastJumpedPos = 0
        # loop till last jump hasn't taken us till the end
        while lastJumpedPos < len(nums)-1:
            # Furthest index reachable on the next level from current level
            maxReachable = max(maxReachable, nums[i] + i)
            if i == lastJumpedPos:  # current level has been iterated and maxReachable position on next level has been finalised
                lastJumpedPos = maxReachable
                jumps += 1  # jumps only gets updated after we iterate all possible jumps from previous level. This ensures jumps will only store minimum jump required to reach lastJumpedPos
            i += 1
        return jumps
