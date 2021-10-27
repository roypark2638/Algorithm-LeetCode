'''
572. Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    '''
    DFS Recursion: Time O(n * m) Space O(h)
    First use DFS to find where two nodes have same value. Once we found it, not call another recurisve function to check if both of the trees have same strueture.

    If both of the nodes are null, then return True. After that check, now we check if either node has null, then we know the disequality, so return False. Otherwise, as long as the both nodes have the same value, keep traverse both nodes and finally return true if left and right result are all True.
    '''

    def isSubtree(self, root, subRoot):
        def dfs(node, sub):
            if not node:
                return False
            if node.val == sub.val:
                if self.isSameStructure(node, sub):
                    return True
            return dfs(node.left, sub) or dfs(node.right, sub)
        return dfs(root, subRoot)

    def isSameStructure(self, node, sub):
        if not node and not sub:
            return True
        if not node or not sub:
            return False
        if node.val != sub.val:
            return False
        return self.isSameStructure(node.left, sub.left) and self.isSameStructure(node.right, sub.right)

        # if node and sub:
        #     if node.val != sub.val:
        #         return False
        #     left = self.isSameStructure(node.left, sub.left)
        #     right= self.isSameStructure(node.right, sub.right)
        #     return left and right
        # else:
        #     if not node and sub or not sub and node:
        #         return False
        #     return True
