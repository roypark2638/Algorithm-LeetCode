'''
Smallest Difference

Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first array in the first position.

Note that the absolute difference of two integers is the distance between them on the real number line. For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.

You can assume that there will only be one pair of numbers with the smallest difference.
'''
arrayOne = [-1,5,10,20,28,3]
arrayTwo = [26,134,135,15,17]

'''
1. sort each array
[-1,3,5,10,20,28]
[15,17,26,134,135]

- use two pointers to compare the difference
- keep track of smallest and current differences
- loop while any of them doesn't exceed their array index
'''
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    smallest = float("inf")
    current = float("inf")
    resultPair = []
    a = 0
    b = 0
    while a < len(arrayOne) and b < len(arrayTwo):
        first = arrayOne[a]
        second = arrayTwo[b]
        if first < second:
            current = second - first
            a += 1
        elif second < first:
            current = first - second
            b += 1
        else:
            return [first, second]
        if smallest > current:
            smallest = current
            resultPair = [first, second]
    return resultPair
    

print(smallestDifference(arrayOne, arrayTwo))