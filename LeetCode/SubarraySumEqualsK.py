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
    1. Bruth Force: Time O(n^2) Space O(1)
    - Use two loops to iterate the array and calculate currentSum.
    - If the currentSum is eqaul to the targetSum, increment the count.
    - Return the count

    2. Memoization of path sum: Time O(n) Space O(n)

    - In order to optimze from the bruth force solution, we will have to think of a clear way to memoize the intermediate result. Namely in the brutal force solution, we did a lot of repeated calculation. For example [1,3,5]: 1, 1+3, 1+3+5, 3, 3+5, 5.
    - This is a classical "space and time tradeoff": we can create a dictionary, cache which saves all the pathSum (from root to current node) and their frequency.
    - Again, we traverse through the tree, at each node, we can get the currPathSum (from root to current node). If within this path, there is a valid solution, then there must be a oldPathSum such that currPathSum - oldPathSum = target
    - We just need to add the frequency of the oldPathSum in the dictionary to the result.

    Time O(n) Space O(n)
    '''


nums = [1, 1, 1]
k = 2


def subarraySum(nums, k):
    count = 0
    cache = {0: 1}
    currPathSum = 0
    for i in range(len(nums)):
        currPathSum += nums[i]
        oldPathSum = currPathSum - k
        count += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
    return count


print(subarraySum(nums, k))
