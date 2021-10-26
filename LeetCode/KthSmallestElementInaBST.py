'''
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
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
    We know that if we use in-order tree traversal, we know kth element is located at kth traversal position in in-order. Simply traverse the tree in-order and count the number of node to match with given k. We can return the node's value when k is equal to the count.
    '''
#     count = 0
#     ans = TreeNode()
#     def kthSmallest(self, root, k):

#         def dfs(node):
#             if node:
#                 dfs(node.left)
#                 self.count += 1
#                 if self.count == k:
#                     self.ans = node
#                 dfs(node.right)

#         dfs(root)
#         return self.ans.val
    '''
    Iterative DFS: Time O(n) Space O(h)
    '''

    def kthSmallest(self, root, k):
        stack = []
        count = 0
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return -1
            count += 1
            root = stack.pop()
            if count == k:
                return root.val
            root = root.right
        return -1
