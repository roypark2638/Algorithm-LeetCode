'''
Minimum Passes Of Matrix

Write a function that takes in an integer matrix of potentially unequal height and width and returns the minimum number of paases required to convert all negative integers in the matrix to positive integers.

A negative integer in the matrix can only be converted to a positive integer if one or more of its adjacent elements is positive. An adjacent element is an element that is to the left, to the right, above, or below the current element in the matrix. Converting an negative to a positive simply involes multiplying it by -1

Note that the 0 value is neither positive nor negative, meaning that a 0 can't convert an adjacent negative to a positive.

A single pass through the matrix involves converting all the negative integers that can be converted at a particular point in time. For example, consider the following input matrix:

[
    [0, -2, -1],
    [-5, 2, 0],
    [-6, -2, 0]
]

After a first pass, only 3 values can be converted to positives:
[
    [0, 2, -1],
    [5, 2, 0],
    [-6, 2, 0]
]

After a second pass, the remaining negative values can all be converted to positives:
[
    [0, 2, 1],
    [5, 2, 0],
    [6, 2, 0]
]

Note that the input matrix will always contain at least one element. If the negative integers in the input matrix can't all be converted to positives, regardless of how many passes are run, your function should return -1.

Sample Input
matrix = [
    [0, -1, -3, 2, 0],
    [1, -2, -5, -1, -3],
    [3, 0, 0, -4, -1]
]

Sample Output
3
'''

matrix = [
    [0, -1, -3, 2, 0],
    [1, -2, -5, -1, -3],
    [3, 0, 0, -4, -1]
]

# Same Complexity but more optimal space complexity than below solution.


def minimumPassesOfMatrix(matrix):
    passes = getPasses(matrix)
    return passes - 1 if not containNegative(matrix) else -1


def getPasses(matrix):
    queue = getAllPositives(matrix)
    passes = 0

    while len(queue):
        size = len(queue)
        while size > 0:
            currentPosition = queue.pop(0)
            row, col = currentPosition

            positions = getNegativePositions(matrix, row, col)
            for row, col in positions:
                queue.append([row, col])
                matrix[row][col] *= -1
            size -= 1
        passes += 1
    return passes


def getAllPositives(matrix):
    positives = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0:
                positives.append([i, j])
    return positives


def containNegative(matrix):
    for row in matrix:
        for value in row:
            if value < 0:
                return True
    return False


def getNegativePositions(matrix, row, col):
    positions = []

    if row > 0 and matrix[row-1][col] < 0:
        positions.append([row-1, col])

    if col > 0 and matrix[row][col-1] < 0:
        positions.append([row, col-1])

    if row < len(matrix) - 1 and matrix[row+1][col] < 0:
        positions.append([row+1, col])

    if col < len(matrix[0]) - 1 and matrix[row][col+1] < 0:
        positions.append([row, col+1])

    return positions


'''
# Time O(w * h) Space O(w * h)
def minimumPassesOfMatrix(matrix):
    passes = getPasses(matrix)
    return passes - 1 if not containNegative(matrix) else -1


def getPasses(matrix):
    nextQueue = getAllPositives(matrix)
    passes = 0
    while len(nextQueue) > 0:
        currentQueue = nextQueue
        nextQueue = []

        while len(currentQueue) > 0:
            currentPosition = currentQueue.pop(0)
            row, col = currentPosition

            positions = getNegativePositions(matrix, row, col)
            for row, col in positions:
                nextQueue.append([row, col])
                matrix[row][col] *= -1
        passes += 1
    return passes


def getAllPositives(matrix):
    positives = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0:
                positives.append([i, j])
    return positives


def containNegative(matrix):
    for row in matrix:
        for value in row:
            if value < 0:
                return True
    return False


def getNegativePositions(matrix, row, col):
    positions = []

    if row > 0 and matrix[row-1][col] < 0:
        positions.append([row-1, col])

    if col > 0 and matrix[row][col-1] < 0:
        positions.append([row, col-1])

    if row < len(matrix) - 1 and matrix[row+1][col] < 0:
        positions.append([row+1, col])

    if col < len(matrix[0]) - 1 and matrix[row][col+1] < 0:
        positions.append([row, col+1])

    return positions


'''
