'''
797. All Paths From Source to Target
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
'''

'''
directed acyclic graph (DAG)
Essentially, we want to implement a recursive function called backtrack(currNode, path) which continues the exploration, given the current node and the path traversed so far.

Within the recursive function, we first define its base case, i.e. the moment we should terminate the recursion. Obviously, we should stop the exploration when we encounter our target node. So the condition of the base case is currNode == target.

As the body of our recursive function, we should enumerate through all the neighbor nodes of the current node.

For each iteration, we first mark the choice by appending the neighbor node to the path. Then we recursively invoke our backtrack() function to explore deeper. At the end of the iteration, we should reverse the choice by popping out the neighbor node from the path, so that we could start all over for the next neighbor node.

Once we define our backtrack() function, it suffices to add the initial node (i.e. node with index 0) to the path, to kick off our backtracking exploration.

Time O(2^n * n)
Space O(2^n * n)
'''
graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]


def allPathsSourceTarget(graph):
    ans = []
    target = len(graph) - 1

    def backtrack(currNode, path):
        if currNode == target:
            ans.append(list(path))
            return

        for nextNode in graph[currNode]:
            path.append(nextNode)
            backtrack(nextNode, path)
            path.pop()

    path = [0]
    backtrack(0, path)
    return ans


print(allPathsSourceTarget(graph))
