'''
1351. Count Negative Numbers in a Sorted Matrix

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1

'''
grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]

# 1. Bruth force
# iterate grid and count all the negative numbers and return the count
# Time O(nm) Space O(1)


def foo1(grid):
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] < 0:
                count += len(grid[row]) - col
                break
    return count

# 2. Take advantage of the fact that it's sorted in non-increasing order
# if we find the negative number,
# count += grid[row] - 1 - col


def foo2(grid):
    m, n = len(grid), len(grid[0])
    r, c, count = m-1, 0, 0
    while r >= 0 and c < n:
        if grid[r][c] < 0:
            count += n - c
            r -= 1
        else:
            c += 1
    return count


print(foo1(grid))
print(foo2(grid))
