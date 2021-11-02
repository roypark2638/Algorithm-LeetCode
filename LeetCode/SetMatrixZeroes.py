'''
73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''


class Solution(object):
    '''
    2. Space Optimized Solution: Time O(nm) Space O(1)

    Use first row cell and first colume cell as an indicator and two additional variables to flag firstRow and firstCol if we need to change the first cell to zeros.
    - Iterate the matrix and mark the indicator(first cells) and those two variable, firstRow and firstCol.
    - Iterate from 1 to the length of the matrix row and check the first column of each row has zero value, then iterate from 1 to the length of the matrix column and convert matrix value to 0
    - We want to perform similarly from right above step but switch row and column.
    - check if firstCol and firstRow flag is on, then change the first cell value to zero. 
    '''

    def setZeroes(self, matrix):
        R = len(matrix)
        C = len(matrix[0])
        firstRow = False
        firstCol = False
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    if i == 0:
                        firstRow = True
                    if j == 0:
                        firstCol = True
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, R):
            if matrix[i][0] == 0:
                for j in range(1, C):
                    matrix[i][j] = 0

        for j in range(1, C):
            if matrix[0][j] == 0:
                for i in range(1, R):
                    matrix[i][j] = 0
        if firstCol:
            for i in range(R):
                matrix[i][0] = 0
        if firstRow:
            for j in range(C):
                matrix[0][j] = 0
        return matrix

    '''
    1. Additional Memory
    Store the indices of the initial 0s to convert the row and column to zero while not effecting converted 0s. Then convert the entire row and column of the each 0s position from the created indices array.
    
    It's important to iterate the matrix from the top to bottom in order to reduce time complexity.
    - Create indices array to hold 0s
    - Iterate the indices array and call a function named, traverseNeighbors by passing matrix, i, and j indices
        - Store i and j into a stack
        - convert the current position value to 0
        - store the neighbors only if it's in the boundry the value is not 0
    
    Time O(nm) Space O(n+m)
    '''
#     def setZeroes(self, matrix):
#         # create an indices array and store the indices where matrix value is equal to 0
#         indices = []
#         for row in range(len(matrix)):
#             for col in range(len(matrix[row])):
#                 if matrix[row][col] == 0:
#                     indices.append((row, col))

#         for i, j in indices:
#             self.findNeighbors(matrix, i, j)
#         return matrix

#     def findNeighbors(self, matrix, row, col):
#         i, j = row, col
#         while i > 0:
#             matrix[i-1][j] = 0
#             i -= 1

#         i, j = row, col
#         while j > 0:
#             matrix[i][j-1] = 0
#             j -= 1

#         i, j = row, col
#         while i < len(matrix) -1:
#             matrix[i+1][j] = 0
#             i += 1

#         i, j = row, col
#         while j < len(matrix[0]) -1:
#             matrix[i][j+1] = 0
#             j += 1

    '''
    Same solution as approach 1 but cleaner way to write the code.
    '''
#     def setZeroes(self, matrix):
#         R = len(matrix)
#         C = len(matrix[0])
#         rows = set()
#         cols = set()
#         for row in range(R):
#             for col in range(C):
#                 if matrix[row][col] == 0:
#                     rows.add(row)
#                     cols.add(col)
#         for row in range(R):
#             for col in range(C):
#                 if row in rows or col in cols:
#                     matrix[row][col] = 0
#         return matrix
