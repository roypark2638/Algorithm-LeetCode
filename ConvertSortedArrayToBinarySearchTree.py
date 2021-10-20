'''
108. Convert Sorted Array to Binary Search Tree
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    '''
    Recursive BST construction: Time O(n) Space O(logn)
    - Call a helper function with the nums array, start, and end index.
    - Use a binary search to pick the mid value and construct left and right subtrees
    '''

    def sortedArrayToBST(self, nums):
        return self.constructBST(nums, 0, len(nums)-1)

    def constructBST(self, nums, left, right):
        if left > right:
            return None
        mid = left + (right - left)//2
        node = TreeNode(nums[mid])
        node.left = self.constructBST(nums, left, mid - 1)
        node.right = self.constructBST(nums, mid + 1, right)
        return node
