'''
62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
Example 3:

Input: m = 7, n = 3
Output: 28
Example 4:

Input: m = 3, n = 3
Output: 6
 

Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 109.
'''


class Solution(object):
    '''
    Bruth-Force, Recursive: Time O(2^nm) Space O(nm) - TLE
    We want to create a unique path count as global vairable to keep track in the recursion.
    The base case is when we reach the n and m to the finish position, we increment our unique path count.
    if n is greater than the finisi row index or m is greater than the finish col index, then re simply return null value
    otherwise, we call the recursion one incrementing n and another one incrementing m
    '''
    # count = 0
    # def uniquePaths(self, m, n):
    #     def countUniquePaths(row, col):
    #         if row == m and col == n:
    #             self.count += 1
    #         if row > m or col > n:
    #             return
    #         else:
    #             countUniquePaths(row+1, col)
    #             countUniquePaths(row, col+1)
    #     countUniquePaths(1, 1)
    #     return self.count
    # count = 0
    '''
    Dynamic Programming
    Top-down: Time O(nm) Space O(nm)
    We want to count up the number of path on each (row, col) position and store the value into a hashmap to avoid recomputation.
    '''

    def uniquePaths(self, m, n):
        memo = {}

        def countUniquePaths(row, col):
            if (row, col) in memo:
                return memo[(row, col)]
            if row == m and col == n:
                return 1
            if row > m or col > n:
                return 0
            count = 0
            count += countUniquePaths(row+1, col) + \
                countUniquePaths(row, col+1)
            memo[(row, col)] = count
            return count

        return countUniquePaths(1, 1)
    '''
    Bottom-up(Iterative): Time O(nm) Space O(nm)
    We want to solve the subproblems from the smallest and build way up to solve bigger and finally the original problem. Since we have two ways that we can move either bottom or right, we can find the current position's number of paths by adding the number of bottom paths and the number of right paths. Initially, we want to fill out our dp table with 1s, since every path has at least one path. Now, iterate the grid starting index from 1(0-indexed, position at 2x2) to fill up the table and return the last element in the grid
    '''
#     def uniquePaths(self, m, n):
#         dp = [[1 for i in range(n)] for j in range(m)]
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
#         return dp[-1][-1]
