'''
114. Flatten Binary Tree to Linked List
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
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
    Morris Traversal Time O(n) Space O(1)
    It requires modifying the tree's structure. 

    Morris Traversal takes advantage of the basic nature of ordered traversals to iterate through and unwind the tree. In a pre-order traversal of a binary tree, each vertex is processed in (node, left, right) order. This means that the entire left subtree could be placed between the node and its right subtree.

    First, we need to locate the last right node in the left subtree while keeping track of the current node. So, whenever we find a left subtree, we can dispatch a runner(leftTail) to find its last node, then stitch together both ends of the left subtree into the righ path of curr, taking heed to sever the left connection at curr.

    Once that's done, we can continue to move curr to the right, looking for the next left subtree. When curr can no longer move right, the tree will be successfully flattened.
    '''
    # def flatten(self, root):
    #     curr = root
    #     while curr:
    #         if curr.left:
    #             leftTail = curr.left
    #             while leftTail.right:
    #                 leftTail = leftTail.right
    #             leftTail.right = curr.right
    #             curr.right = curr.left
    #             curr.left = None
    #         curr = curr.right

    '''
    Recursion DFS.
    Create a dummy prev and create a new binary tree
    '''
#     prev = None
#     def flatten(self, root):
#         if not root:
#             return None
#         self.flatten(root.right)
#         self.flatten(root.left)

#         root.right = self.prev
#         root.left = None
#         self.prev = root

    '''
    DFS Iterative solution
    Use a new dummy TreeNode, last to reconstruct a linkedlist from the tree
    '''

    def flatten(self, root):
        last = TreeNode(-1)
        stack = [root]
        while stack:
            node = stack.pop()
            last.right = node
            last.left = None
            if node and node.right:
                stack.append(node.right)
            if node and node.left:
                stack.append(node.left)
            last = node
