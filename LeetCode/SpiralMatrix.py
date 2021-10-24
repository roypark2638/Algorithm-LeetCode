'''
54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.


Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

'''


class Solution(object):
    '''
    startRow, endRow, startCol, endCol
    Iterate firstly start row of each colume, secondly end colume and each row, thirdly check if the current row is same as the one we traverse firstly, if yes break, if not then iterate. forthly same bound check and then iterate if it's meet with the condition.

    Move pointers by 1 and iterate above logic while startRow < endRow and startCol < endCol

    Time O(nm) Space O(nm)
    '''

    def spiralOrder(self, matrix):
        res = []
        startRow, startCol = 0, 0,
        endRow, endCol = len(matrix), len(matrix[0])

        while startRow < endRow and startCol < endCol:
            for col in range(startCol, endCol):
                res.append(matrix[startRow][col])
            for row in range(startRow+1, endRow):
                res.append(matrix[row][endCol-1])
            for col in reversed(range(startCol, endCol-1)):
                if startRow == endRow-1:
                    break
                res.append(matrix[endRow-1][col])
            for row in reversed(range(startRow+1, endRow-1)):
                if startCol == endCol-1:
                    break
                res.append(matrix[row][startCol])
            startRow += 1
            startCol += 1
            endRow -= 1
            endCol -= 1
        return res
