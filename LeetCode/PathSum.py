'''
112. Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    '''
    Time O(n) Space O(n) where n is the number of the nodes
    Space O(n) is for the worst case when the tree is completely unbalanced.
    Best case would be Space O(logn) when the tree is balanced.
    Iterative solution
    - Use depth first search on the binary search
    - Traverse the tree with the stack
    - if it's not leaf, then add up the currentSum
    - if it's leaf, then subtract the currentSum
    - if current node is leaf than compare target to the current sum
    '''

    def hasPathSum(self, root, targetSum):
        stack = [(root, 0)]
        while stack:
            node, curr = stack.pop()
            if node is None:
                continue
            if node.left is None and node.right is None:
                if node.val + curr == targetSum:
                    return True
            stack.append((node.left, curr+node.val))
            stack.append((node.right, curr+node.val))
        return False
    '''
    Time O(n) Space O(n) where n is the number of the nodes
    Space O(n) is for the worst case when the tree is completely unbalanced.
    Best case would be Space O(logn) when the tree is balanced.
    Depth First Search starting from the root
    add up the sum and once reached the leaf node, compare if the sum is equal to the targetSum
    return true if it is
    
    How do we know if there is one single true, then we want to stop
    '''
    # def hasPathSum(self, root, targetSum):
    #     def helper(node, targetSum, current):
    #         if node is None:
    #             return False
    #         elif node.left is None and node.right is None:
    #             if targetSum == current+node.val:
    #                 return True
    #             else:
    #                 return False
    #         if helper(node.left, targetSum, current+node.val) or helper(node.right, targetSum, current+node.val):
    #             return True
    #     return helper(root, targetSum, 0)
#         def helper(node, targetSum, current):
#             if node is None:
#                 if targetSum == current:
#                     return True
#                 else:
#                     return False

#             if helper(node.left, targetSum, current+node.val) or helper(node.right, targetSum, current+node.val):
#                 return True
#         return helper(root, targetSum, 0)
