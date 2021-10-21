'''
938. Range Sum of BST

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
'''

# Time O(N) Space O(N)
# DFS Iterative


def rangeSumBST(root, low, high):
    total = 0
    stack = [root]
    while stack:
        node = stack.pop()

        if node.val >= low and node.val <= high:
            total += node.val

        if node.left and node.val >= low:
            stack.append(node.left)
        if node.right and node.val <= high:
            stack.append(node.right)

    return total
