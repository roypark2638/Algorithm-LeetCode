'''
221. Maximal Square
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
'''


class Solution(object):
    '''
    Space optimized
    In order to calculate the current box size, we need a 1-D array with a variable to hold a previous value.
    Time O(nm) space O(n)
    '''

    def maximalSquare(self, matrix):
        dp = [0 for i in range(len(matrix[0])+1)]
        maxLength, prev = 0, 0
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                temp = dp[j]
                if matrix[i-1][j-1] == "1":
                    dp[j] = min(dp[j-1], dp[j], prev) + 1
                    maxLength = max(dp[j], maxLength)
                else:
                    dp[j] = 0
                prev = temp
        return maxLength*maxLength

    '''
    Tabulation 
    Get the minimum value from the surrounding values(top, topleft, left) and add one to the current dp table and keep track of the maximum length of the box.
    '''
    # def maximalSquare(self, matrix):
    #     dp = [[0 for row in range(len(matrix[0])+1)] for col in range(len(matrix)+1)]
    #     maxLength = 0
    #     for i in range(1, len(matrix)+1):
    #         for j in range(1, len(matrix[0])+1):
    #             if matrix[i-1][j-1] == "1":
    #                 dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
    #                 maxLength = max(dp[i][j], maxLength)
    #     return maxLength*maxLength

    '''
    Bruth force
    Time O((nm)^2) Space O(nm)
    '''
#     def maximalSquare(self, matrix):
#         maxSquare = 0
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j] == "1":
#                     maxSquare = max(maxSquare, self.findSquareSize(matrix, i, j))
#         return maxSquare


#     def findSquareSize(self, matrix, i, j):
#         row, col = 2, 2
#         squareSize = 1
#         isSquare = True
#         while isSquare and i+ row <= len(matrix) and j+col <= len(matrix[0]):
#             for r in range(i, i+row):
#                 for c in range(j, j+col):
#                     if matrix[r][c] != "1":
#                         isSquare = False
#                         return (row-1)*(col-1)
#             squareSize = row * col
#             row += 1
#             col += 1
#         return squareSize
