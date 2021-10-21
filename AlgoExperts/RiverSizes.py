'''
River Sizes

You're given a two-dimensional array(a matrix) of potentially unequal height and width containing only 0s and 1s. Each 0 represents land, and each 1 represents part of a river. A river consists of any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent). The number of adjacent 1s forming a river determine its size.

Note that a river can twist. In other words, it doesn't have to be a straight vertical line or a straight hortizontal line; it can be L-shaped, for example.

Write a function that returns an array of the sizes of all rivers represented in the input matrix. The sizes don't need to be in any particular order.

Sample Input
matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 0]
]

Sample Output
[1, 2, 2, 2, 5] // The numbers could be ordered differently.
'''

matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 0]
]
'''
- create an array to hold the result sizes
- copy the matrix and assign initial value of False to mark if we visited or not
- use two for loops
- if visited, then continue, otherwise call traverseNode function

- use BFS and queue to traverse the adjacent nodes
- set the current position'visitied True
- getUnvisitedNeighbors and append those neighbors to the queue

- if currentRiverSize > 0, then append that into the result sizes array.

- return the sizes
'''


'''
- create an array to hold the result sizes
- copy the matrix and assign initial value of False to mark if we visited or not
- use two for loops
- if visited, then continue, otherwise call traverseNode function

- use BFS and queue to traverse the adjacent nodes
- set the current position'visitied True
- getUnvisitedNeighbors and append those neighbors to the queue

- if currentRiverSize > 0, then append that into the result sizes array.

- return the sizes
'''


def riverSizes(matrix):
    sizes = []
    isVisited = [[False for row in matrix[0]] for col in matrix]
    for col in range(len(matrix)):
        for row in range(len(matrix[0])):
            if isVisited[col][row] == True:
                continue
            traverseNode(col, row, matrix, isVisited, sizes)
    return sizes


def traverseNode(col, row, matrix, isVisited, sizes):
    currentRiverSize = 0
    nodesToExplore = [[col, row]]
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop(0)
        col = currentNode[0]
        row = currentNode[1]
        if isVisited[col][row]:
            continue
        isVisited[col][row] = True
        if matrix[col][row] == 0:
            continue
        currentRiverSize += 1
        unvisitedNeighbors = getUnvisitedNeighbors(col, row, isVisited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)

    if currentRiverSize > 0:
        sizes.append(currentRiverSize)


def getUnvisitedNeighbors(col, row, isVisited):
    neighbors = []

    if col > 0 and isVisited[col-1][row] == False:
        neighbors.append([col-1, row])
    if row > 0 and isVisited[col][row-1] == False:
        neighbors.append([col, row-1])
    if col < len(isVisited) - 1 and isVisited[col+1][row] == False:
        neighbors.append([col+1, row])
    if row < len(isVisited[0]) - 1 and isVisited[col][row+1] == False:
        neighbors.append([col, row+1])
    return neighbors


print(riverSizes(matrix))
