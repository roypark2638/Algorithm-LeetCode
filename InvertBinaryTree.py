'''
Invert Binary Tree

Wrtie a function that takes in a Binary Tree and inverts it. In other words, the function should swap every left node in the tree for its corresponding right node.

Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input

tree =      1
           /  \
          2     3
         / \   / \
        4  5  6   7
      /  \
     8    9

Sample Output
             1
           /  \
          3     2
         / \   / \
        7  6  5   4
                 / \
                9   8 

'''

# Breath First Search (Iterative solution)
# Time O(n) Space O(n)
def invertBinaryTree(tree):
	queue = [tree]
  while queue:
    curr = queue.pop(0)
    if curr is None:
      continue
    swap(curr)
    queue.append(curr.left)
    queue.append(curr.right)

# Recursive Solution
# Time O(n) where n is the number of the nodes in the tree
# Space O(d) where d is the depth of the tree
def invertBinaryTree2(tree):
  if tree is None:
    return
  swap(tree)
  invertBinaryTree2(tree.left)
  invertBinaryTree2(tree.right)

  
def swap(tree):
	tree.left, tree.right = tree.right, tree.left

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

