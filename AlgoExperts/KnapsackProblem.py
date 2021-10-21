'''
Knapsack Problem

You're given an array of arrays where each subarray holds two integer values and represents an item; the first integer is the item's value, and the second integer is the item's weight. You're also given an integer representing the maximum capacity of a knapsack that you have.

Your goal is to fit items in your knapsack without having the sum of their weights exceed the knapsack's capacity, all the while maximizing thier combined value. Note that you only have one of each item at your disposal.

Return the maximized combined value of the items that you should pick as well as an array of the indices of each item picekd.

items = [[1,2],[4,3],[5,6],[6,7]]
capacity = 10

output
[10, [1,3]]
'''

'''
Dyanmic programming
Time O(nm) Space O(nm) where n is the length of the items and m is the length of the capacity
- Create a matrix (m+1) x (n+1) to evaluate the current maximum capacity
- Iterate the matrix and if currentItemWeight is less than equal to the currentCapacity,
    - Then append matrix[i][j] into either maximum of currentItemValue + matrix[i-1][currentCapacity-currentItemWeight] or right above value
    - else: append above value
- Create and return a sequence of the indices that creating the currentMaximumCapacity.
'''


def knapsackProblem(items, capacity):
    matrix = [[0 for _ in range(capacity+1)] for _ in range(len(items)+1)]

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            currentItemWeight = items[i-1][1]
            currentItemValue = items[i-1][0]

            if currentItemWeight <= j:
                matrix[i][j] = max(currentItemValue + matrix[i-1],
                                   [j-currentItemWeight], matrix[i-1][j])
            else:
                matrix[i][j] = matrix[i-1][j]
    return [matrix[-1][-1], getIndices(matrix, items)]


def getIndices(matrix, items):
    row = len(matrix) - 1
    col = len(matrix[row]) - 1
    indices = []
    while row > 0 and col > 0:
        # append and move the current item index
        if matrix[row-1][col] == matrix[row][col]:
            row -= 1
        else:
            row -= 1
            indices.append(row)
            col -= items[row][1]
    return indices
