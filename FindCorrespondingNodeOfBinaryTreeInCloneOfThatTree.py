'''
1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

Follow up: Solve the problem if repeated values on the tree are allowed.

Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.

'''


class Solution(object):
    '''
    - is the target must exist in the original?
    - can there be duplicate values?

    - Find and store the target node from original
    - and find the node from cloned
    '''
# BFS Iterative using queue

    def getTargetCopy(self, original, cloned, target):
        queue = deque([(original, cloned)])
        while queue:
            ori, cl = queue.popleft()
            if ori is None:
                continue
            if ori is target:
                return cl
            queue.append((ori.left, cl.left))
            queue.append((ori.right, cl.right))

# DFS Recurisve
#     def getTargetCopy(self, original, cloned, target):
#         def getTargetNode(original, cloned):
#             if original is not None:
#                 getTargetNode(original.left, cloned.left)
#                 if original == target:
#                     self.ans = cloned
#                 getTargetNode(original.right, cloned.right)

#         getTargetNode(original, cloned)

#         return self.ans

# DFS Iterative
#     def getTargetCopy(self, original, cloned, target):
#         stack = [(original, cloned)]
#         while stack:
#             node, cl = stack.pop()
#             if node is None:
#                 continue
#             stack.append((node.left, cl.left))
#             if node == target:
#                 return cl
#             stack.append((node.right, cl.right))
