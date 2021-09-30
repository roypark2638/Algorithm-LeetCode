'''
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
'''
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]


# Iterative DFS with queue structure
# This method directly mutate grid to mark for visiting
# If mutation is not allowed, create a new matrix to check the visiting
# Time O(n*m) Space O(n*m)

def numIslands(grid):
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):

            if grid[row][col] == "1":
                count += 1
                traverseNegihbors(grid, row, col)
    return count


def traverseNegihbors(grid, row, col):
    queue = [(row, col)]
    while queue:
        r, c = queue.pop()
        if grid[r][c] != "1":
            continue
        grid[r][c] = "#"

        unvisitedNeighbors = getNeighbors(grid, r, c)
        for neighbor in unvisitedNeighbors:
            queue.append(neighbor)


def getNeighbors(grid, row, col):
    neighbors = []

    if row > 0:
        neighbors.append([row-1, col])

    if col > 0:
        neighbors.append([row, col-1])

    if row < len(grid) - 1:
        neighbors.append([row+1, col])

    if col < len(grid[0]) - 1:
        neighbors.append([row, col+1])

    return neighbors


print(numIslands(grid))
