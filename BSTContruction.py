'''
BST Contruction

Wrtie a BST class for a Binary Search Tree. The class should support:
  - Inserting values with the insert method.
  - Removing values with the remove method; this method should only remove the first instance of a given value.
  - Searching for values with the contains method.

Note that you can't remove values from a single-node tree. In other words, calling the remove method on a single-node tree should simply not do anything.

Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the ST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null.

'''

# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        curNode = self
		while True:
			if value < curNode.value:
				if curNode.left is None:
					curNode.left = BST(value)
					break
				else:
					curNode = curNode.left
			else:
				if curNode.right is None:
					curNode.right = BST(value)
					break
				else:
					curNode = curNode.right
        return self

    def contains(self, value):
        curNode = self
		while curNode is not None:
			if value < curNode.value:
				curNode = curNode.left
			elif value > curNode.value:
				curNode = curNode.right
			else:
				return True
		return False

    def remove(self, value, parentNode = None):
        curNode = self
		while curNode is not None:
			if value < curNode.value:
				parentNode = curNode
				curNode = curNode.left
			elif value > curNode.value:
				parentNode = curNode
				curNode = curNode.right
			else:
				if curNode.left is not None and curNode.right is not None:
					curNode.value = curNode.right.getMinValue()
					curNode.right.remove(curNode.value, curNode)
				elif parentNode is None:
					if curNode.left is not None:
						curNode.value = curNode.left.value
						curNode.right = curNode.left.right
						curNode.left = curNode.left.left
					elif curNode.right is not None:
						curNode.value = curNode.right.value
						curNode.left = curNode.right.left
						curNode.right = curNode.right.right
					else:
						pass
				elif parentNode.left == curNode:
					parentNode.left = curNode.left if curNode.left is not None else curNode.right
				elif parentNode.right == curNode:
					parentNode.right = curNode.right if curNode.right is not None else curNode.left
				break
					
        return self

	def getMinValue(self):
		curNode = self
		while curNode.left is not None:
			curNode = curNode.left
		return curNode.value
	
	
	
	
	