'''
1302. Deepest Leaves Sum

Given the root of a binary tree, return the sum of values of its deepest leaves.
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
'''


root = [1, 2, 3, 4, 5, null, 6, 7, null, null, null, null, 8]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    # Use DFS inorder traversal, stack and iteratively
    # Time O(v+e) Space O(d)
    #     def deepestLeavesSum(self, root):
    #         depth = deepestSum = 0
    #         stack = [(root, 0)]
    #         while stack:
    #             node, currDepth = stack.pop()
    #             if node.left is None and node.right is None: # if it's leave node
    #                 if currDepth > depth:
    #                     depth = currDepth
    #                     deepestSum = node.val
    #                 elif currDepth == depth:
    #                     deepestSum += node.val

    #             else:
    #                 if node.left:
    #                     stack.append((node.left, currDepth + 1))
    #                 if node.right:
    #                     stack.append((node.right, currDepth + 1))
    #         return deepestSum

    # BFS, queue and iteratively
    def deepestLeavesSum(self, root):
        deepsetSum = depth = 0
        queue = deque([(root, 0)])
        while queue:
            node, currDepth = queue.popleft()

            if node.left is None and node.right is None:
                if currDepth > depth:
                    depth = currDepth
                    deepestSum = node.val
                elif currDepth == depth:
                    deepestSum += node.val

            else:
                if node.left:
                    queue.append((node.left, currDepth+1))
                if node.right:
                    queue.append((node.right, currDepth+1))
        return deepestSum
