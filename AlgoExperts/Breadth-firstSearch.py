'''
You're given a Node class that has a name and an array of optional children nodes. When put together, nodes from an acyclic tree-like structure.

Implement the breadthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the Breadth-first Search approach (specifically navigating the tree from left to right), stores all of the nodes' names in the input array, and returns it.

Sample Input

graph =   A
        / | \
       B  C   D
      / \    / \
     E  F   G   H
       / \   \
      I   J   K

Sample Output
["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
'''


# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # Time O(v + e) Space O(v)
    def breadthFirstSearch(self, array):
        queue = [self]
        while queue:
            node = queue.pop(0)
            if node is None:
                continue
            array.append(node.name)
            for child in node.children:
                queue.append(child)
        return array
