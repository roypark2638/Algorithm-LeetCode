'''
105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    '''
    DFS Recursion

    Preorder indicates the root of node in order and Inorder indicates each node's left subtree and right subtree. Use recursion with base case checking if the length of the inorder and preorder is 0, then return None, which means that the current child node is empty and also check if preorder length is equal to the one, then return the first index value in the preorder TreeNode. Now, pop the first value in the preorder and create a new node with that value and find the coordinate index from the inorder array. Now assign the new node left and right value by calling the recursion function and slice the inorder array to be subtree of left and right. Fianlly return the made root to combine them as a tree structure.
    '''

    def buildTree(self, preorder, inorder):
        def constructTree(preorder, inorder):
            if not len(inorder):
                return None
            if len(preorder) == 1:
                return TreeNode(preorder[0])
            value = preorder.pop(0)
            root = TreeNode(value)
            idx = inorder.index(value)
            root.left = constructTree(preorder, inorder[:idx])
            root.right = constructTree(preorder, inorder[idx+1:])
            return root
        return constructTree(preorder, inorder)

#    def buildTree(self, preorder, inorder):
#         def constructTree(preorder, inorder):
#             if not len(inorder) or not len(preorder):
#                 return None
#             if len(preorder) == 1:
#                 return TreeNode(preorder[0])

#             root = TreeNode(preorder[0])
#             idx = inorder.index(preorder[0])
#             root.left = constructTree(preorder[1:idx+1], inorder[:idx])
#             root.right = constructTree(preorder[idx+1:], inorder[idx+1:])
#             return root
#         return constructTree(preorder, inorder)

#     def buildTree(self, preorder, inorder):
#         def constructTree(inStart, inEnd, preStart, preEnd):
#             if inStart == inEnd or preStart == preEnd:
#                 return TreeNode(preorder[0])
#             if inStart > inEnd or preStart > preEnd:
#                 return None

#             root = TreeNode(preorder[preStart])
#             inorderRootIndex = inorder.index(preorder[preStart])
#             root.left = constructTree(inStart, inorderRootIndex -1, preStart+1, inorderRootIndex-1)
#             root.right = constructTree(inorderRootIndex + 1, inEnd, preStart+1, inorderRootIndex+1)
#             return root

#         return constructTree(preorder, inorder, 0, len(inorder)-1)
