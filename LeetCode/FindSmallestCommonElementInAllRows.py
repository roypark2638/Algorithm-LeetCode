'''
1198. Find Smallest Common Element in All Rows

Given an m x n matrix mat where every row is sorted in strictly increasing order, return the smallest common element in all rows.

If there is no common element, return -1.

Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5
Example 2:

Input: mat = [[1,2,3],[2,3,4],[2,3,5]]
Output: 2
'''
mat = [[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]


def foo1(mat):
    dic = {}
    rows = len(mat)
    for row in mat:
        createFrequencyTable(row, dic)

    for key, value in dic.items():
        if value == rows:
            return key
    return -1


def createFrequencyTable(row, dic):
    for n in row:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1


def foo2(mat):
    def binarySearch(arr, tar):
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l+r) // 2
            if arr[m] == tar:
                return True
            elif arr[m] > tar:
                r = m - 1
            else:
                l = m + 1
        return False

    if len(mat) == 1:
        return mat[0][0]

    for tar in mat[0]:
        for j in range(1, len(mat)):
            if not binarySearch(mat[j], tar):
                break
        else:
            return tar
    return -1


print(foo1(mat))
print(foo2(mat))
