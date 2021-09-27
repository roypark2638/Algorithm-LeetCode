'''
1337. The K Weakest Rows in a Matrix

You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are [2,0,3,1,4].
'''

mat = [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1]
]
k = 3

# Linear Search and Sorting


# Time O(nm) + O(mlogm) where m is the length of the row
# Time O(m * (n + logm)) Space O(m)
# Sum up all 1s and store in a tuple.
# Sort the tuple and return the result
def foo1(mat, k):
    strengths = []

    for i, row in enumerate(mat):
        strength = 0
        for value in row:
            if value == 1:
                strength += 1
            else:
                break
        strengths.append((strength, i))

    # Sort all the strengths. This will sort firstly by strength and secondly by index.
    strengths.sort()

    indices = []
    for i in range(k):
        indices.append(strengths[i][1])
    return indices


# Binary Search and Sorting/ Map
# Time O(nm) + O(mlogm)
# Time O(m * (n + logm)) Space O(m)
# Find the number of 1s with binary search and same process from the above
def foo2(mat, k):
    def binarySearch(arr):
        l, r = 0, len(arr)
        while l < r:
            m = (l+r) // 2
            if arr[m] == 0:
                r = m
            elif arr[m] == 1:
                l = m + 1
        return l

    strengths = []
    for i, row in enumerate(mat):
        strengths.append((binarySearch(row), i))
    strengths.sort()
    res = []
    for i in range(k):
        res.append(strengths[i][1])
    return res


print(foo1(mat, k))
print(foo2(mat, k))
