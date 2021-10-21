'''
Write a function that takes in a potentially invalid BST and returns a boolean representing whether the BST is valid.

Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node its right; and its children nodes are either valid BST nodes themselves or None / null.

A BST is valid if and only if all of tis nodes are valid BST nodes.

'''

# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
  return validateBstHelper(tree, float("-inf"), float("inf"))

def validateBstHelper(tree, minValue, maxValue):
  if tree is None:
    return True

  if tree.value < minValue or tree.value >= maxValue:
    return False

  isLeftValid = validateBstHelper(tree.left, minValue, tree.value)
  isRightValid = validateBstHelper(tree.right, tree.value, maxValue)
  return isLeftValid and isRightValid

