'''
366. Find Leaves of Binary Tree

Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.

Example 1:

Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
Example 2:

Input: root = [1]
Output: [[1]]
'''
'''
DFS and Hashmap

Key point here is to find and mark the height of each node
Use DFS to traverse the node and keep track of the currentHeight

When we reach the base case, calculate currentHeight and store as follow
hashmap{currentHeight: [node.val]}

'''


def findLeaves(self, root):
    heightMap = {}

    def dfs(node):
        if node is None:
            return -1
        currentHeight = max(dfs(node.left), dfs(node.right)) + 1
        if currentHeight in heightMap:
            heightMap[currentHeight].append(node.val)
        else:
            heightMap[currentHeight] = [node.val]

        return currentHeight
    dfs(root)
    return heightMap.values()
