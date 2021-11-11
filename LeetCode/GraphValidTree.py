'''
261. Graph Valid Tree

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.


Example 1:


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false

Constraints:

1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.
'''


class Solution(object):
    '''
    Breath-first search

    We want to use bfs to validate tree structure from the given undirected edges list. First we can check whether the graph has a cycle by checking if length of the edge list is not equal to the n-1 where n.

    We consider two ways to represent the graph either adjacency list or adjacency matrix. Since this graph is close to be a sparse graph, where the number of edges are much less than |V^2| we would like to use the adjacency list. Therefore, first step is to convert the edges list to the adjacency list.

    We want to check if any part of vertex is disconnected and visited vertex. So we create seen hashset for this task with our first vertex in it

    Use Queue data structure for looping and enumerate the neighbors got from the adjacency list and if the neighbor not exist in the seen hashset, then we add the neighbor into seen hashset and queue, this way we don't visit the same vertex repeated. 

    Finally return whether length of the seen hashset is equal to the n

    creating adjacency list takes Time O(v+e) and space O(v+e)
    looping the queue takes time O(v) by making sure we are not enquing the visited vertex and dequing take constant time.
    seen hashset takes O(v) space 
    where v is the length of the vertexis and e is the length of the edges in the graph
    '''

    def validTree(self, n, edges):
        # check if it has a cycle in the graph or a self loop
        if len(edges) != n - 1:
            return False
        # create adjacency list based on the given edges
        adlist = {i: [] for i in range(n)}
        for a, b in edges:
            adlist[a] += [b]
            adlist[b] += [a]
        # create seen hashset to check visit status and check any disconnected graph
        seen = {0}
        queue = deque([0])
        while queue:
            vertex = queue.popleft()
            for neighbor in adlist[vertex]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        return len(seen) == n
