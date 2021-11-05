'''
Divide and Conquer from CLRS
'''

A = [1, 5, -3, -5, 10, 1, 5, -7]


def findMaximumSubarray(A):
    print(findMaximumSubarrayDivideAndConquer(A, 0, len(A)-1))


def findMaximumSubarrayDivideAndConquer(A, low, high):
    if low >= high:
        return (low, high, A[low])

    mid = low + (high - low) // 2

    (leftLow, leftHigh, leftSum) = findMaximumSubarrayDivideAndConquer(A, low, mid)
    (rightLow, rightHigh, rightSum) = findMaximumSubarrayDivideAndConquer(
        A, mid + 1, high)
    (crossLow, crossHigh, crossSum) = findMaxCrossingSubarray(A, low, mid, high)

    if leftSum >= rightSum and leftSum >= crossSum:
        return (leftLow, leftHigh, leftSum)
    elif rightSum >= leftSum and rightSum >= crossSum:
        return (rightLow, rightHigh, rightSum)
    else:
        return (crossLow, crossHigh, crossSum)


def findMaxCrossingSubarray(A, low, mid, high):
    leftMaxSum = float('-inf')
    curSum = 0
    left = mid

    for i in reversed(range(low, mid+1)):
        curSum += A[i]
        if curSum > leftMaxSum:
            leftMaxSum = curSum
            left = i
    right = mid+1
    curSum = 0
    rightMaxSum = float('-inf')

    for i in range(mid+1, high):
        curSum += A[i]
        if curSum > rightMaxSum:
            rightMaxSum = curSum
            right = i

    return (left, right, leftMaxSum + rightMaxSum)


findMaximumSubarray(A)
