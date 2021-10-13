'''
113. Path Sum II
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
'''


class Solution(object):
    '''
    Time O(n^2) Space O(n) where n is the number of the nodes
    Worst case time complexity is when the tree is the complete tree,
    where has n/2 leaf nodes. Every leaf node, we will perform O(n) copy
    operation. Therefore, it's O(n^2) time.

    Recursive DFS Approach
    base case
    - if node is None:
        return 
    path.append(node.val) and add up currentSum
    - if leaf node and found the matching sum
        append the path to the result array
    - else:
        recursion(node.left, targetSum, path, currentSum)
        recursion(node.right, targetSum, path, currentSum)
    Here is a place after visiting the leaf node or right node
    pop last element from the path

    '''

    def pathSum(self, root, targetSum):
        res = []

        def dfs(node, target, path, current):
            if not node:
                return
            path.append(node.val)
            current += node.val
            if not node.left and not node.right and current == target:
                res.append(list(path))
            else:
                dfs(node.left, target, path, current)
                dfs(node.right, target, path, current)
            path.pop()
        dfs(root, targetSum, [], 0)
        return res
