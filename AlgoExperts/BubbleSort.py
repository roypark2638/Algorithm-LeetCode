'''
Bubble Sort

Write a function that taks in an array of integers and returns a sorted version of that array. Use the Bubble Sort algorithm to sort the array.

Sample Input
array = [8, 5, 2, 9, 5, 6, 3]

Sample Output
[2, 3, 5, 5, 6, 8, 9]
'''

array = [8, 5, 2, 9, 5, 6, 3]

'''
i, j pointer move together until j < len(array) - i
Check if there is a change happended each loop, if not then break and return
'''


def bubbleSort(array):
    for i in range(len(array) - 1):
        changed = False
        for j in range(1, len(array) - i):
            if array[j-1] > array[j]:
                changed = True
                array[j-1], array[j] = array[j], array[j-1]
            if not changed:
                break
    return array


print(bubbleSort(array))
