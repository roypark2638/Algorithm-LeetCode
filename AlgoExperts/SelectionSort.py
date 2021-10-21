'''
Selection Sort

Write a function that takes in an array of integers and returns a sorted version of that array. Use the Selection Sort algorithm to sort the array.

Sample Input
array = [8, 5, 2, 9, 5, 6, 3]

Sameple Output
[2, 3, 5, 5, 6, 8, 9]
'''

array = [8, 5, 2, 9, 5, 6, 3]

# Time O(n^2) | Space O(1)


def selectionSort(array):
    for i in range(len(array)-1):
        smallestIdx = i
        for j in range(i+1, len(array)):
            if array[j] < array[smallestIdx]:
                smallestIdx = j
        array[i], array[smallestIdx] = array[smallestIdx], array[i]

    return array


print(selectionSort(array))
