'''
64. Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
'''


class Solution(object):
    '''
    Approach 3 Mutate the grid in place
    Time O(nm) space O(1)
    '''

    def minPathSum(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cost = grid[i][j]
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = cost + grid[i][j-1]
                elif j == 0:
                    grid[i][j] = cost + grid[i-1][j]
                else:
                    grid[i][j] = cost + min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
    '''
    Approach 2 Tabulation.
    - Create a nxm matrix to hold the each state's minimum cost
    - Iterate the matrix and check the condition for when (1) row and col is equal to 0 (2) row is equal to 0 (3) col is equal to 0 (4) else.
    cost(i,j) = grid[i][j] + min(cost(i+1,j), cost(i,j+1))
    '''
#     def minPathSum(self, grid):
#         costs = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
#         for i in range(len(costs)):
#             for j in range(len(costs[0])):
#                 cost = grid[i][j]
#                 if i == 0 and j == 0:
#                     costs[i][j] =cost
#                 elif i == 0:
#                     costs[i][j] = costs[i][j-1] + cost
#                 elif j == 0:
#                     costs[i][j] = costs[i-1][j] + cost
#                 else:
#                     costs[i][j] = min(costs[i-1][j], costs[i][j-1]) + cost
#         return costs[-1][-1]

    '''
    Approach 1.
    Bruth Force and momization
    
    The Bruth Force approach involves recursion. For each element, we consider two paths, rightwards and downwards and find the minimum sum out of those two. It specifies whether we need to take a right step or downward step to minimize the sum.
    
    cost(i,j) = grid[i][j] + min(cost(i+1,j), cost(i,j+1))
    '''
    # def minPathSum(self, grid):
    #     m, n = len(grid), len(grid[0])
    #     memo = {}
    #     def dfs(i, j):
    #         if (i, j) in memo:
    #             return memo[(i, j)]
    #         if i >= m or j >= n:
    #             return float('inf')
    #         if i == m-1 and j== n-1:
    #             return grid[i][j]
    #         memo[(i, j)] = min(dfs(i+1, j), dfs(i,j+1)) + grid[i][j]
    #         return memo[(i, j)]
    #     return dfs(0,0)
