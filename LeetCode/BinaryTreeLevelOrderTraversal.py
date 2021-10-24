'''
102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    '''
    Recursive DFS: Time O(n) Space O(h)
    Create a global hashmap to store the each level's node and create dfs helper function passing node and height. If current node is null then return for our base case. We used preorder traverse, which we simply store the node value with respect to the current height. After storing the value and we traverse left and right subtrees with height + 1.
    '''
    # def levelOrder(self, root):
    #     res = {}
    #     def dfs(node, height):
    #         if not node:
    #             return
    #         if height in res:
    #             res[height].append(node.val)
    #         else:
    #             res[height] = [node.val]
    #         dfs(node.left, height + 1)
    #         dfs(node.right, height + 1)
    #     dfs(root, 0)
    #     return res.values()

    '''
    Iterative Traverse: Time O(n) Space O(h)
    * Ask if returning order matters
    On leetcode doesn't accept different orders, so make sure to append it to the stack right node first and then left node.
    
    '''

    def levelOrder(self, root):
        stack = [(root, 0)]
        res = {}
        while stack:
            node, height = stack.pop()
            if not node:
                continue
            if height in res:
                res[height].append(node.val)
            else:
                res[height] = [node.val]
            stack.append((node.right, height + 1))
            stack.append((node.left, height + 1))
        return res.values()
