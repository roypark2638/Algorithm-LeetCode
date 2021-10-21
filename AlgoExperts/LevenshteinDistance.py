'''
Levenshtein Distance

Write a function that takes in two strings and returns the minimum number of edit operations that need to be performed on the first string to obtain the second string.

There are three edit operations: insertion of a character, deletion of a character, and substitution of a character for another.

Sample Input
str1 = "abc"
str2 = "yabd"

Sample Output
2
'''

str1 = "abc"
str2 = "yabd"

# Time O(nm) Space O(nm)


def levenshteinDistance2(str1, str2):
    edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for col in range(1, len(str2) + 1):
        edits[col][0] = col
    for col in range(1, len(str2) + 1):
        for row in range(1, len(str1) + 1):
            if str1[row-1] == str2[col-1]:
                edits[col][row] = edits[col-1][row-1]
            else:
                edits[col][row] = 1 + \
                    min(edits[col-1][row-1], edits[col-1]
                        [row], edits[col][row-1])
    return edits[-1][-1]


# Optimal Solution
# Time O(nm) Space O(min(n,m)) where n is the length of the str1 and m is the length of the str2
def levenshteinDistance(str1, str2):
    # Find out the smaller strings to set as a row
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2
    # Init the first row to be like [0, 1, 2, 3, ...]
    evenEditRow = [x for x in range(len(small) + 1)]
    oddEditRow = [None for _ in range(len(small) + 1)]
    for colIdx in range(1, len(big) + 1):
        if colIdx % 2 == 1:
            currentEditRow = oddEditRow
            previousEditRow = evenEditRow
        else:
            currentEditRow = evenEditRow
            previousEditRow = oddEditRow
        # init the first col to be like [0], [1], [2], [3], ...
        currentEditRow[0] = colIdx
        for rowIdx in range(1, len(small) + 1):
            if small[rowIdx-1] == big[colIdx-1]:
                currentEditRow[rowIdx] = previousEditRow[rowIdx-1]
            else:
                currentEditRow[rowIdx] = 1 + min(
                    previousEditRow[rowIdx-1], previousEditRow[rowIdx], currentEditRow[rowIdx-1])
    return evenEditRow[-1] if len(big) % 2 == 0 else oddEditRow[-1]


print(levenshteinDistance2(str1, str2))
