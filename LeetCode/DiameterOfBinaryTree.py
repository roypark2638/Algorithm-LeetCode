'''
543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.


Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1

Constraints:

The number of nodes in the tree is in the range [1, 104].
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
    Diameter of a tree is a length of the longest apth between any two nodes in a tree. This path may or may not pass through the root node.

    Longest path must be between two left nodes. We know that in a tree, nodes are only connected with their parent node and 2 children. Therefore we know that the longest path in the tree would consist of a node, its longest left branch, and its longest right branch. So, our algorithm to solve this problem will find the node where the sum of its longest left and right branches is maximized. 

    - Use a recursion function dfs to calculate the maximum diameter. Initialize diameter globally and base case is where node is null, return 0. Get left path and rigth path recursively, and current maximum diameter = max(diamter, leftPath + rightPath). And return max(leftPath, rightPath) + 1 -> just like calculating the maximum depth of the tree.
    Time O(n) Space O(h)
    '''
    diameter = 0

    def diameterOfBinaryTree(self, root):
        def longestPath(node):
            if not node:
                return 0
            leftPath = longestPath(node.left)
            rightPath = longestPath(node.right)

            self.diameter = max(self.diameter, leftPath + rightPath)
            return max(leftPath, rightPath) + 1
        longestPath(root)
        return self.diameter
