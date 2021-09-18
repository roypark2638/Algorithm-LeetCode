'''
Min Height BST

Write a function that takes in a non-empty sorted array of distinct integers, constructs a BST from the integers, and returns the root of the BST.

The function should minimize the height of the BST.

You've been provided with a BST class that you'll have to use to construct the BST.

Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null.

A BST is valid if and only if all of its nodes are valid BST nodes.

Note that the BST class already has an insert method which you can use if you want.

Sample Input
array = [1, 2, 5, 7, 10, 13, 14, 15, 22]

Sample Output

            10
           /  \
          2    14
         / \   / \
        1  5  13  15
            \       \
              7      22
'''

# Time O(nlogn) -> logn is from the insert method
# Space O(n)
# def minHeightBst(array):
#     return constructMinHeightBst(array, None, 0, len(array) - 1)

# def constructMinHeightBst(array, bst, start, end):
# 	if start > end:
# 		return
# 	mid = (start + end) // 2
# 	if bst is None:
# 		bst = BST(array[mid])
# 	else:
# 		bst.insert(array[mid])
# 	constructMinHeightBst(array, bst, start, mid - 1)
# 	constructMinHeightBst(array, bst, mid + 1, end)
# 	return bst

# Still passing the bst as an argument and manually insert the bst without using insert method.
# Time O(n) 
# Space O(n)
# def minHeightBst(array):
#     return constructMinHeightBst(array, None, 0, len(array) - 1)

# def constructMinHeightBst(array, bst, start, end):
# 	if start > end:
# 		return
# 	mid = (start + end) // 2
# 	newBstNode = BST(array[mid])
# 	if bst is None:
# 		bst = newBstNode
# 	else:
# 		if array[mid] < bst.value:
# 			bst.left = newBstNode
# 			bst = bst.left
# 		else:
# 			bst.right = newBstNode
# 			bst = bst.right
# 	constructMinHeightBst(array, bst, start, mid - 1)
# 	constructMinHeightBst(array, bst, mid + 1, end)
# 	return bst


# Cleaner and optimal way.
# Instead of passing the bst to the recursive function,
# connect the bst tree while constructing the tree.
# Time O(n)
# Space O(n)
def minHeightBst(array):
    return constructMinHeightBst(array, 0, len(array) - 1)

def constructMinHeightBst(array, start, end):
	if start > end:
		return None
	mid = (start + end) // 2
	bst = BST(array[mid])
	bst.left = constructMinHeightBst(array, start, mid - 1)
	bst.right = constructMinHeightBst(array, mid + 1, end)
	return bst

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
