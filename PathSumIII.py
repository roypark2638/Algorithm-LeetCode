'''
437. Path Sum III

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    '''
    Memoization solution Time O(n) Space O(n)
    High level walkthrough
    1. In order to optimize the solution, we can reduce the repeated calculation. 
    For example, 1->3->5: 1, 1+3, 1+3+5, 3, 3+5, 5
    2. This is classical space and time tradeoff. Create a hasahmap to store pathSum and their frequency
    3. Traverse the tree and check if each iteration has a valid subtree sums up to the target sum. Then
    there are must be a oldPathSum such that currPathSum - oldPathSum = target
    4. add the frequency of the oldPathSum to the result
    5. During DFS break down, we need to -1 in cache[currPathSum] because this path is not available later traverse
    '''
    counter = 0

    def pathSum(self, root, targetSum):
        cache = {0: 1}
        self.dfs(root, targetSum, cache, 0)
        return self.counter

    def dfs(self, node, targetSum, cache, currPathSum):
        if not node:
            return

        currPathSum += node.val
        oldPathSum = currPathSum - targetSum
        self.counter += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1

        self.dfs(node.left, targetSum, cache, currPathSum)
        self.dfs(node.right, targetSum, cache, currPathSum)
        cache[currPathSum] -= 1

    '''
    Bruth Force Solution Time O(nlogn) ~ O(n^2)
    High level walkthrough
    1. create global variable, count
    2. 1st DFS layer
    3. 2nd DFS layer
    4. return
    '''
#     counter = 0
#     def pathSum(self, root, targetSum):
#         self.dfs(root,targetSum)
#         return self.counter

#     def dfs(self, node, targetSum):
#         if not node:
#             return

#         self.test(node, targetSum, 0)
#         self.dfs(node.left, targetSum)
#         self.dfs(node.right, targetSum)

#     def test(self, node, targetSum, currPathSum):
#         if not node:
#             return

#         currPathSum += node.val
#         if currPathSum == targetSum:
#             self.counter += 1
#         self.test(node.left, targetSum, currPathSum)
#         self.test(node.right, targetSum, currPathSum)
