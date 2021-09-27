'''
1213. Intersection of Three Sorted Arrays

Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
Example 2:

Input: arr1 = [197,418,523,876,1356], arr2 = [501,880,1593,1710,1870], arr3 = [521,682,1337,1395,1764]
Output: []
'''

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]


# Binary Search
# Time O(nlogn) Space O(logn)
def foo1(arr1, arr2, arr3):
    res = []
    for n in arr1:
        if binarySearch(arr2, n, 0, len(arr2)-1) and binarySearch(arr3, n, 0, len(arr3)-1):
            res.append(n)
    return res


def binarySearch(arr, n, start, end):
    if start > end:
        return False
    mid = (start + end) // 2

    if arr[mid] == n:
        return True
    elif arr[mid] > n:
        return binarySearch(arr, n, start, mid - 1)
    else:
        return binarySearch(arr, n, mid + 1, end)


# Bruth-Force HashMap
# Time O(n) Space O(n)


def foo2(arr1, arr2, arr3):
    res = []
    dic = {}
    createDic(arr1, dic)
    createDic(arr2, dic)
    createDic(arr3, dic)

    for key, value in dic.items():
        if value == 3:
            res.append(key)
    return res


def createDic(arr, dic):
    for n in arr:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1


# Most Optimal
# Three pointers
def foo3(arr1, arr2, arr3):
    res = []
    p1 = p2 = p3 = 0
    while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
        if arr1[p1] == arr2[p2] == arr3[p3]:
            res.append(arr1[p1])
            p1 += 1
            p2 += 1
            p3 += 1
        else:
            max_ = max(arr1[p1], arr2[p2], arr3[p3])
            if arr1[p1] < max_:
                p1 += 1
            elif arr2[p2] < max_:
                p2 += 1
            elif arr3[p3] < max_:
                p3 += 1
    return res


print(foo1(arr1, arr2, arr3))
print(foo2(arr1, arr2, arr3))
print(foo3(arr1, arr2, arr3))
