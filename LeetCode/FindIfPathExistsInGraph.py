'''
1971. Find if Path Exists in Graph

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex start to vertex end.

Given edges and the integers n, start, and end, return true if there is a valid path from start to end, or false otherwise.

 

Example 1:


Input: n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
Example 2:


Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], start = 0, end = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
 

Constraints:

1 <= n <= 2 * 105
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= start, end <= n - 1
There are no duplicate edges.
There are no self edges.

'''


class Solution(object):
    '''
    Graph Traversal, DFS and BFS

    Use either DFS or BFS to find a path from given start to end vertax. Since the graph is an unriected, we have to mark visited vertax to avoid infinite cycling.

    - Create a visited array initially false values with the number of vertaxies and adjacency list from the given edge list.
    - Call a DFS function with arguments, visited, adjacency list, start, and end.
    - Use stack to store initially start vertax and loop while the stack is not empty.
    - Pop the stack value into a node and continue if node is null or node is already visited.
    - Mark the current node visitied value to True
    - Return True only if the currnet node is equal to the end node, which means that we found a path
    - Otherwise, iterate the current node's neighbors and append it to the stack
    - After traversing all possible path from the start, if the path doesn't exist, return False

    Time O(e) Space O(v+e)
    '''

    def validPath(self, n, edges, start, end):
        # create a visited array
        visited = [False] * n

        # create and generate adjacency list with edge list
        adList = {}
        for v1, v2 in edges:
            if v1 in adList:
                adList[v1].append(v2)
            else:
                adList[v1] = [v2]
            if v2 in adList:
                adList[v2].append(v1)
            else:
                adList[v2] = [v1]
        # call DFS or BFS function to find if a path exists from start to end vertax
        return self.dfsHasPathFrom(start, end, adList, visited)

    def dfsHasPathFrom(self, start, end, adList, visited):
        stack = [start]
        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True

            if node == end:
                return True
            for neighbor in adList[node]:
                stack.append(neighbor)

        return False

    def bfsHasPathFrom(self, start, end, adList, visited):
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if visited[node]:
                continue
            visited[node] = True
            if end == node:
                return True
            for nei in adList[node]:
                queue.append(nei)
        return False
