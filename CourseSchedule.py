'''
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

'''


class Solution(object):
    '''
    The problem could be modeled as yet another graph traversal problem, where each course can be represented as a vertex in a graph and the dependancy between the courses can be modeled as a directed edge between two vertex. The problem to determine if one could build a valid schedule of courses that satisfies all the dependancies would be equaivalent to determin if the corresponding graph is DAG i.e. there is no cycle existed in the graph.

    Backtracking is a general algorithm to solve a constraint satisfaction problems, which incrementally builds cadidnates to a solution, and abandon the candidate (i.e. backtrack) as soon as it determines the candidate would noe lead to a valid solution.

    Algorithm 3 steps.

    step 1) We build a graph structure with the given list of course dependencies. Here we adopt the adjacency list data structure, which can be implemented as hashmap or dictionary. Each entry in the adjacency list represents a node which consists of a node index and a list of neighbors nodes that follow from the node.

    step 2) We then enumerate each node (course) in the constructed graph, to check if we could form a dependency cycle starting from the node.

    step 3) we perform the cycle check via backtracking, where we breadcrumb our path (i.e. mark the nodes we visited) to detect if we come across a previously visited node (hence a cycle detected). We also remove the breadcrumbs for each iteration
    '''
#     def canFinish(self, numCourses, prerequisites):
#         courseAdjacencyList = {}

#         # construct a graph structure and adopt the adjacency list data structure
#         for courses in prerequisites:
#             prevCourse, nextCourse = courses[0], courses[1]
#             if prevCourse in courseAdjacencyList:
#                 courseAdjacencyList[prevCourse].append(nextCourse)
#             else:
#                 courseAdjacencyList[prevCourse] = [nextCourse]

#         path = [False for _ in range(numCourses)]
#         for currCourse in courseAdjacencyList.keys():
#             cycleExist = self.detectCycle(currCourse, path, courseAdjacencyList)
#             if cycleExist:
#                 return False
#         return True

#     def detectCycle(self, currCourse, path, courseAdjacencyList):
#         if currCourse not in courseAdjacencyList:
#             return False
#         if path[currCourse]:
#             return True

#         path[currCourse] = True
#         ret = False
#         neighbors = courseAdjacencyList[currCourse]
#         for child in neighbors:
#             ret = self.detectCycle(child, path, courseAdjacencyList)
#             if ret: break

#         # after backtracking, remove the breadcrumb(i.e. visited mark)
#         path[currCourse] = False
#         return ret

    # Postorder DFS Algorithm
    # Time O() where E is the number of edges
    # E+V for creating graph structure and adjacency list
    def canFinish(self, numCourses, prerequisites):
        # create graph structure and adjacency list
        courseMap = {}
        for prevCourse, nextCourse in prerequisites:
            if prevCourse in courseMap:
                courseMap[prevCourse].append(nextCourse)
            else:
                courseMap[prevCourse] = [nextCourse]

        # create two data structure to hold path for breakcrumbs to check acycle
        # visitied for marking visited node
        path = [False] * numCourses
        visited = [False] * numCourses

        for currCourse in courseMap.keys():
            cycleExist = self.cycleCheck(currCourse, path, visited, courseMap)
            if cycleExist:
                return False

        return True

    def cycleCheck(self, currCourse, path, visited, courseMap):
        if visited[currCourse] or currCourse not in courseMap:
            return False
        if path[currCourse]:
            return True

        # mark the path, means that this course in a process of stack or backtracking
        path[currCourse] = True
        res = False
        children = courseMap[currCourse]
        for child in children:
            res = self.cycleCheck(child, path, visited, courseMap)
            if res:
                break
        # mark visitied in order not to call this node again
        visited[currCourse] = True
        path[currCourse] = False
        return res
