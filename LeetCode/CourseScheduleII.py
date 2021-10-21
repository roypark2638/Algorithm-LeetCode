'''
210. Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
'''


class Solution(object):
    '''
    Same as the previous question and we have to return the ordering of the courses to take
    If we find the cycle, than we return an array with 0
    cycle checks 

    A topological order is an ordering of the nodes in a directed graph where for each directed edges 
    from node A to node B, node A appears before node B in the ordering.

    situation e.g. school class prerequisites, program dependencies, event scheduling, assembly instructions etc..

    Time O(V+E) where V is the vertex and E is the edges
    Note: Topological orderings are not unique

    A directed graph containing a cucle cannot have topological ordering
    Directed Acyclic Graph(DAG) is a only directed graph can have top order.

    Note: Every tree has a toplogical ordering since three don't have a cycle. 
    -> Pick the leaf nodes, and it's like removing leaf node question
    -> Mark the height by adding into dictionary
    '''
    WHITE, GREY, BLACK = 1, 2, 3

    def findOrder(self, numCourses, prerequisites):
        courseMap = {}
        stack = []
        for nextCourse, preCourse in prerequisites:
            if preCourse in courseMap:
                courseMap[preCourse].append(nextCourse)
            else:
                courseMap[preCourse] = [nextCourse]

        color = [Solution.WHITE for _ in range(numCourses)]

        def dfs(currCourse):
            if currCourse not in courseMap:
                color[currCourse] = self.BLACK
                stack.append(currCourse)
                return True

            color[currCourse] = self.GREY
            for child in courseMap[currCourse]:
                if color[child] == self.WHITE:
                    if not dfs(child):
                        return False
                elif color[child] == self.GREY:
                    return False

            color[currCourse] = self.BLACK
            stack.append(currCourse)
            return True

        for currCourse in range(numCourses):
            if color[currCourse] == self.WHITE:
                if not dfs(currCourse):
                    return []

        return stack[::-1]
