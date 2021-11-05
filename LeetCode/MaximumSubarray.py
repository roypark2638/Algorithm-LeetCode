'''
Divide and Conquer from CLRS

The greatest sum over all subarrays must be in these three options
- A[low .. mid]
- A[mid+1 .. high]
- crossing the midpoint

We can find maximum subarrays on the A[low .. mid] and A[mid+1 .. high] recursively because these two subproblems are smaller instances of the problem of finding a maximum subarray. Now, find maximum subarray in crossing mid point and take a subarray with the largest sum of the three.

Find maximum subarray corssing the midpoint
: This problem is not a smaller instance of our original problem because it has the added restriction that the subarray it chooses must cross the midpoint. Any subarray crossing the midpoint is titself made of two subarrays A[i .. mid] and A[mid+1 .. high]. Therefore, we just need to find maximum subarrays of the form A[i .. mid] and A[mid+1 .. j] and then combine them.

Analysing Running Time
: the recursive call for finding maximum subarrays in A[low .. mid] and A[mid+1 .. high] takes 2T(n/2) and finding crossing subarray takes O(n) time. 2T(n/2) + O(n) = O(nlogn)
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
