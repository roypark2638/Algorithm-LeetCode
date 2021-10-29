'''
133. Clone Graph
Medium

4012

1971

Add to List

Share
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
Example 4:


Input: adjList = [[2],[1]]
Output: [[2],[1]]
 

Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution(object):
    '''
    Recursive DFS Hashmap deep clone: Time O(n) Space O(n) where n is v + e
    We want to copy every node and connect the nodes in an undirected way. We use recursive function to clone each node and first we check if the current node is in the hashmap, means that we already made a clone and visited, then just return that node from the hashmap. Otherwise, we create a new copy node from the original node and store that node into our hashmap. Now iterate the all the neighbors from the orignal current node and append it to the copied node's neighbors properties. And finally we return the copy of the node at the end.
    '''
#     def cloneGraph(self, node):
#         oldToNew = {}
#         def clone(node):
#             if not node:
#                 return
#             if node in oldToNew:
#                 return oldToNew[node]

#             copy = Node(node.val)
#             oldToNew[node] = copy

#             for neighbor in node.neighbors:
#                 copy.neighbors.append(clone(neighbor))
#             return copy
#         return clone(node)

    '''
    BFS Hashmap: Time O(n) Space O(n) where n is v + e
    
    '''

    def cloneGraph(self, node):
        if not node:
            return node
        queue = deque([node])
        oldToNew = {}
        oldToNew[node] = Node(node.val, [])
        while queue:
            n = queue.popleft()
            for nei in n.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val, [])
                    queue.append(nei)
                oldToNew[n].neighbors.append(oldToNew[nei])

        return oldToNew[node]
