'''
654. Maximum Binary Tree

You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the subarray prefix to the left of the maximum value.
Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.

Input: nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]
Explanation: The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.
'''
nums = [3, 2, 1, 6, 0, 5]

'''
    No duplicates, if there is a duplicate, we can use the first occured value since the array is not sorted but ask to the interviewer for the confirmation of their thoughts
    - Find index of the maximum value in nums array
    - Create a new node to insert with the max value from the array
    - Slice the nums into leftSubarray and rightSubarray

    The first largest number is the root node where we start
    [3,2,1,6,0,5]
           *
    
    [3,2,1,6,0,5]
           *
    [0,5] right
       *
    [0] left
     *
    [3,2,1] left
     *
    [2,1] right
     *
    [1] right
     *
    '''


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructMaximumBinaryTree(nums):
    def dfs(nums):
        maxIdx = nums.index(max(nums))
        node = TreeNode(nums[maxIdx])

        if len(nums[:maxIdx]) > 0:
            node.left = dfs(nums[:maxIdx])
        if len(nums[maxIdx+1:]) > 0:
            node.right = dfs(nums[maxIdx+1:])
        return node
    return dfs(nums)


def inorder(node):
    if node:
        inorder(node.left)
        print(node.val)
        inorder(node.right)


print(constructMaximumBinaryTree(nums))
root = constructMaximumBinaryTree(nums)
print(inorder(root))
