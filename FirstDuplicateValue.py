'''
First Duplicate Value

Given an array of integers between 1 and n, inclusive, where n is the length of the array, write a function that returns the first integer that appears more than once (when the array is read from left to right).

In other words, out of all the integers that might occur more than once in the input array, your function should return the one whose first duplicate value has the minimum index.

If no integer appears more than once, your function should return -1.

Note that you're allowed to mutate the input array.

Sample Input
array = [2, 1, 5, 2, 3, 3, 4]

sample Output
2
'''

'''
1. Bruth Force
Time O(n^2) | Space O(1)

2. HashMap
Time O(n) | Space O(n)
- Create a hashmap to store the value that we found and mark with a boolean value.
- Iterate the array and check if the value exist in the hashmap.

3. Array Munipulation
Time O(n) | Space (1)
Since the given prompty indicates that an array of integers between 1 and n, inclusive, where n is the length of the array and we can mutate the given array, we can use this method.
- Iterate array and create seenIndex by abs(value) - 1 to mark the found value on that index.
- If the array value from seenIndex is nagative, return that abs(value)
- Otherwise, make that value negative and keep iterates until the end of the array.
'''

array = [2, 1, 5, 2, 3, 3, 4]

def firstDuplicateValue2(array):
  seen = {}
  for n in array:
    if n in seen:
      return n
    seen[n] = True
  return -1

def firstDuplicateValue3(array):
  for n in array:
    seenIndex = abs(n) - 1
    if array[seenIndex] <= 0:
      return abs(n)
    array[seenIndex] *= -1
  return -1



print(firstDuplicateValue3(array))
