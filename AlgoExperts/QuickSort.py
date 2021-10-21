'''
Quick Sort

'''

array = [8, 5, 2, 9, 5, 6, 3]

# Worst Time O(n^2) when each iteration gives us the longer subarray with max length and shorter subarray with min length
# Best Time O(nlogn) when each iteration divides pivot exactly half
# Average Time O(nlogn)
# Space O(logn) recursion stack, and we need to call next recursion with shorter subarray to achieve this logn space complexity.


def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array


def quickSortHelper(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start+1
    right = end

    while left <= right:
        if array[pivot] < array[left] and array[pivot] > array[right]:
            swap(left, right, array)
            left += 1
            right -= 1
        elif array[pivot] >= array[left]:
            left += 1
        elif array[pivot] <= array[right]:
            right -= 1
    swap(pivot, right, array)
    leftSubarrayIsSmaller = left - 1 - start < end - right

    if leftSubarrayIsSmaller:
        quickSortHelper(array, start, right)
        quickSortHelper(array, right+1, end)
    else:
        quickSortHelper(array, right+1, end)
        quickSortHelper(array, start, right-1)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


print(quickSort(array))
