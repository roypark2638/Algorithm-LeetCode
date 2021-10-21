'''
Remove Islands

You're given a two-dimensional array (a matrix) of potentiall unequal height and width containing only 0s and 1s. The matrix represents a two-toned image, where each 1 represents black and each 0 represents white. An island is defined as any number of 1s t hat are horizontally or vertically adjacent (but not diagonally adjacent) and that don't touch the border of the image. In other words, a group of horizontally or vertically adjacent 1s isn't an island if any of those 1s are in the first row, last row, first column, or last column of the input matrix.

Note that an island can twist. In other words, it doesn't have to be a striaght vertical line or a straight horizontal line; it can be L-shaped, for example.

You can think of islands as patches of black that don't touch the border of the two-toned image.

Wrtie a function that returns a modified version of the input matrix, where all of the islands are removed.
You remove an island by replacing it with 0s.

Naturally, you're allowed to mutate the input matrix.

Sample Input
matrix=
[
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

Sample Output
[
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1]
]
'''
matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

'''
- Iterate the edges of the matrix and mark all of the connected 1s by changing the value to 2
- Iterate the entire matrix and change left 1s to the 0 and 2s to the 1
- return matrix
'''
# Time O(nm) Space O(nm)


def removeIslands(matrix):
    markIslands(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
            elif matrix[i][j] == 2:
                matrix[i][j] = 1
    return matrix


def markIslands(matrix):
    endRow = len(matrix)
    endCol = len(matrix[0])

    for col in range(endCol):
        if matrix[0][col] == 1:
            traverseNodes(matrix, 0, col)
    for row in range(1, endRow):
        if matrix[row][endCol-1] == 1:
            traverseNodes(matrix, row, endCol-1)
    for col in reversed(range(0, endCol-1)):
        if matrix[endRow-1][col] == 1:
            traverseNodes(matrix, endRow-1, col)
    for row in reversed(range(1, endRow-1)):
        if matrix[row][0] == 1:
            traverseNodes(matrix, row, 0)


def traverseNodes(matrix, row, col):
    nodeToExplore = [[row, col]]
    while len(nodeToExplore):
        currentNode = nodeToExplore.pop(0)
        row = currentNode[0]
        col = currentNode[1]
        if matrix[row][col] == 1:
            matrix[row][col] = 2
        neighbors = getNeighbors(matrix, row, col)
        for neighbor in neighbors:
            nodeToExplore.append(neighbor)


def getNeighbors(matrix, row, col):
    neighbors = []

    if col > 0 and matrix[row][col-1] == 1:
        neighbors.append([row, col-1])
    if row > 0 and matrix[row-1][col] == 1:
        neighbors.append([row-1, col])
    if col < len(matrix[0]) - 1 and matrix[row][col+1] == 1:
        neighbors.append([row, col+1])
    if row < len(matrix) - 1 and matrix[row+1][col] == 1:
        neighbors.append([row+1, col])
    return neighbors


print(removeIslands(matrix))
