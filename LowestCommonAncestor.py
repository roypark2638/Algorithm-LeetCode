'''
236. Lowest Common Ancestor of a Binary Tree
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        stack = [(root, None)]
        while stack:
            node, parent = stack.pop()
            if not node:
                continue
            if node is p or node is q:
                stack.append((node.left, node))
                stack.append((node.right, node))

    '''
    1. Recursive Approach
    Traverse the tree in DFS. The moment we encounter either of the nodes p or q, return some boolean flag. The flag helps to determine if we found the requred nodes in any of the paths. The least common ancestor would then be the node for which both the subtree recursions return a True flag. It can also be the node which itself is one of p or q and for which one of the subtree recursions return a True flag.
    
    Algorithm
    1. Start traversing the tree from the root node.
    2. If the current Node is none return None
    3. If the current node itself is one of p or q, return node itself.
    4. Store left and right result into variables
    5. if left and right are both true, than we found the LCA. Return node
    6. Otherwise, return left or right
    
    Time O(n) Space O(h)
    '''
#     def lowestCommonAncestor(self, root, p, q):
#         def dfs(node, p, q):
#             if not node:
#                 return None
#             if node is p or node is q:
#                 return node

#             left = dfs(node.left, p, q)
#             right = dfs(node.right, p ,q)

#             if left and right:
#                 return node
#             return left or right
#         return dfs(root, p, q)
