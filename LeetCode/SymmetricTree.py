'''
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    '''
    Recursive: Time O(n) Space O(logn)
    '''
    # def isSymmetric(self, root):
    #     def dfs(one, two):
    #         if not one and not two:
    #             return True
    #         if not one or not two:
    #             return False
    #         if one.val != two.val:
    #             return False
    #         return dfs(one.right, two.left) and dfs(one.left, two.right)
    #     if not root:
    #         return True
    #     return dfs(root.left, root.right)

    '''
    Iterative: Time O(n) Space O(logn)
    '''

    def isSymmetric(self, root):
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            one, two = stack.pop()
            if not one and two or not two and one:
                return False
            if not one and not two:
                continue
            if one.val != two.val:
                return False
            stack.append((one.left, two.right))
            stack.append((one.right, two.left))
        return True
