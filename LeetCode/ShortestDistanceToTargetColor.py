'''
1182. Shortest Distance to Target Color

You are given an array colors, in which there are three colors: 1, 2 and 3.

You are also given some queries. Each query consists of two integers i and c, return the shortest distance between the given index i and the target color c. If there is no solution return -1.

Example 1:

Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
Output: [3,0,3]
Explanation: 
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).
'''
'''
    ? is the index always valid?

    1. Burth-Force
    - Iterate queries enumerate(i, color)
        - call getShortestDistance function to iterate leftSubarray and rightSubarray to calculate shortest distance to the color, if there is no color than return -1, or return the shortest distance index
    - append the shortest distance index


    2. Hashmap with Binary Search
    - Create hashMap {color: [index]}
    - Iterate queries and get the shortest distance
        - Find the color and call binary search to find the index where can insert number
        - Calculate the shortestDistance on current, left, and right
    '''
colors = [1, 1, 2, 1, 3, 2, 2, 3, 3]
queries = [[1, 3], [2, 2], [6, 1]]

# Binary Search Function to return either the matching index or near index


def binarySearch(targetNum, arr, l, r):
    while l < r:
        mid = (l+r) // 2
        if targetNum > arr[mid]:
            l = mid + 1
        elif targetNum < arr[mid]:
            r = mid - 1
        else:
            return mid
    return l

# Create hashmap {color: [index]}


def createColorMap(colorMap, colors):
    for i, color in enumerate(colors):
        if color not in colorMap:
            colorMap[color] = [i]
        else:
            colorMap[color].append(i)


def getShortestDistance(colorMap, num, color):
    if color not in colorMap:
        return -1
    arr = colorMap[color]

    # Search i where the element can be inserted
    i = binarySearch(num, arr, 0, len(arr) - 1)

    # Calculate the shortestDistance on current, left, and right
    shortestDistance = abs(arr[i]-num)
    if i > 0:
        shortestDistance = min(shortestDistance, abs(arr[i-1]-num))
    if i < len(arr) - 1:
        shortestDistance = min(shortestDistance, abs(arr[i+1]-num))

    return shortestDistance


def shortestDistanceColor(colors, queries):
    colorMap = {}
    createColorMap(colorMap, colors)
    res = []
    for targetNum, targetColor in queries:
        res.append(getShortestDistance(
            colorMap, targetNum, targetColor))
    return res


print(shortestDistanceColor(colors, queries))
