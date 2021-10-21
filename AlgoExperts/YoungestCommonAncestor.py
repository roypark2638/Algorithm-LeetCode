'''
You're given three inputs, all of whicty pointing to their youngest ancestor. The first input is the top ancestor in an ancestral tree (i.e., the only instance that has no ancestor--its ancestor property points to None / null), and the other two inputs are descendants in the ancestral tree.

Write a function that returns the youngest common ancestor to the two descendatns.

Note that a descendant is considered its own ancestor. So in the simple ancestral tree below, the youngest common ancestor to nodes A and B is node A.

// The youngest common ancestor to nodes A and B is node A.

    A
   /
  B

Sample Input
topAncestor = node A
descdendantOne = node E
descendantTwo = Node I

        A
      /   \ 
     B     C
    / \   / \
   D  E  F   G
  / \
 H   I

 Sample Output
 node B
'''

# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


'''
- Given two descendants have different level in the tree
- In order to find the common ancestor, we need to make those two nodes at the same level
- Calculate both of depth in the tree to move lower decendant's level to higher decendant's level
- Match the levels by moving lower decendant to upwards
- Now, two decendants are at the same level.
- Move both of decendatns until they are the same
- Return the common ancestor.
'''

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDepth(topAncestor, descendantOne)
	depthTwo = getDepth(topAncestor, descendantTwo)
	if depthOne > depthTwo:
		return equalizeLevelAndGetCommonAncestor(descendantTwo, descendantOne, depthOne - depthTwo )
	else:

		return equalizeLevelAndGetCommonAncestor(descendantOne, descendantTwo, depthTwo - depthOne)
		
		
def getDepth(top, node):
	depth = 0
	while node != top:
		depth += 1
		node = node.ancestor
	return depth
	
def equalizeLevelAndGetCommonAncestor(high, low, diff):
	for _ in range(diff):
		low = low.ancestor
	while high != low:
		high = high.ancestor
		low = low.ancestor
	return low






