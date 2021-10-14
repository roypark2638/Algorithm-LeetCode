'''
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    '''
    We have to check from the leaf node if it's valid or not to get the optimal time complexity. otherwise we will get n^2 complexity compared to O(n)

    Traverse DFS manner and once we reach to the leaf node check if it's valid
    while traversing the DFS, keep track of the max and min bounds

    '''
#     def isValidBST(self, root):
#         def helper(node, minBound, maxBound):
#             if node is None:
#                 return True
#             if node.val <= minBound or node.val >= maxBound:
#                 return False
#             left = helper(node.left, minBound, node.val)
#             right = helper(node.right, node.val, maxBound)

#             if left and right:
#                 return True
#             # return True


#         return helper(root, float('-inf'), float('inf'))

    '''
    Iterative inorder traversal
    '''

    def isValidBST(self, root):
        stack, prev = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True
