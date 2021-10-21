'''
617. Merge Two Binary Trees

You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Example 1:


Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
Example 2:

Input: root1 = [1], root2 = [1,2]
Output: [2,2]

Constraints:

The number of nodes in both trees is in the range [0, 2000].
-104 <= Node.val <= 104
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    '''
    Clarify questions
    - Are both of the root node have integer values
    - Can I assuem that the sum of the integer values are in the max boundary?
    - Can I mutate the given root1 to make the new binary tree?

    Recursive
    If both of the current nodes are not null, then we sum up the node values into root1 node. Then assign the return node of recursion call traversing left subtrees result to the root1.left. And assign the return node of recursion call traversing right subtrees result to the root1.right. If either of the nodes have null value, simply return root1 or root2.
    Time O(n) Space O(n)
    '''

    def mergeTrees(self, root1, root2):
        if root1 and root2:
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)
            root1.val += root2.val
            return root1
        else:
            return root1 or root2

    '''
    Recursive but we are makign a entirely new binary tree to return value without modifying the original given trees
    '''
    # def mergeTrees(self, root1, root2):
    #     if root1 and root2:
    #         newTreeNode = TreeNode(root1.val + root2.val)
    #         newTreeNode.left = self.mergeTrees(root1.left, root2.left)
    #         newTreeNode.right = self.mergeTrees(root1.right, root2.right)
    #         return newTreeNode
    #     else:
    #         return root1 or root2

    '''
    Iterative
    We again traverse the two trees, but this time we make use of a stack to do so instead of making use of recursion. Each entry in the stack stores data in the form[node1, node2]. Here, node1 and node2 are the nodes of the first tree and the second tree respectively.
    
    We start off by pushing the root nodes of both the trees onto the stack. Then, at every step, we remove a node pair from the top of the stack. For every node pair removed, we add the values corresponding to the two nodes and update the value of the corresponding node in the first tree. Then, if the left child of the first tree exists, we push the left child(pair) of both the trees onto the stack. If the left child of the first tree doesn't exist, we append the left child(subtree) of the second to the current node of the first tree. We do the same for the right child pair as well.
    
    If at any step both the current nodes are null, we continue with popping the next nodes from the stack.
    '''
#     def mergeTrees(self, root1, root2):
#         if not root1:
#             return root2
#         if not root2:
#             return root1
#         stack = [(root1, root2)]
#         while stack:
#             t1, t2 = stack.pop()
#             if not t1 or not t2:
#                 continue

#             if t1 and t2:
#                 t1.val += t2.val
#             stack.append((t1.left, t2.left))
#             stack.append((t1.right, t2.right))
#             if not t1.left:
#                 t1.left = t2.left
#             if not t1.right:
#                 t1.right = t2.right

#         return root1
