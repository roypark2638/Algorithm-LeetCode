'''
1315. Sum of Nodes with Even-Valued Grandparent

Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

A grandparent of a node is the parent of its parent if it exists.

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
'''

# DFS Iterative and add grandchild value


def foo1(root):
    def sumGrandchild(n):
        tot = 0
        if n.left:
            tot += n.left.val
        if n.right:
            tot += n.right.val
        return tot

    stack = [root]
    res = 0
    while stack:
        node = stack.pop()

        if node.left and node.val % 2 == 0:
            res += sumGrandchild(node.left)

        if node.right and node.val % 2 == 0:
            res += sumGrandchild(node.right)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return res

# DFS iterative, check parent and add currNode value


def foo2(root):
    if root is None:
        return 0
    res = 0
    stack = [(root, None)]
    while stack:
        node, parent = stack.pop()
        if parent is not None and parent.val % 2 == 0:
            if node.left:
                res += node.left.val
            if node.right:
                res += node.right.val

        if node.left:
            stack.append((node.left, node))

        if node.right:
            stack.append((node.right, node))

    return res

# DFS recurisve


def foo3(root):

    def dfs(node, parent, grand):
        if node:
            nonlocal ans
            if parent and grand and grand.val % 2 == 0:
                ans += node.val
            dfs(node.left, node, parent)
            dfs(node.right, node, parent)

    ans = 0
    dfs(root, None, None)
    return ans
