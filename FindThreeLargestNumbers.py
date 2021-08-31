'''
Find Three Largest Numbers

Write a function that takes in an array of at least three integers and, without sorting the input array, returns a sorted array of the three largest integers in the input array.

The function should return duplicate integers if necessary; for example, it should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].

Sample Input:
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

Sample Output:
[18, 141, 541]
'''

'''
threeLargestNumbers = [array[0], array[1], array[2]]
threeLargestNumbers.sort()
[1,17,141]

For each array value, compare the value from the larest to smallest.
for index in range(3...<len(array)):
  currentValue = array[index]
  if threeLargestNumbers[2] > currentValue:
    threeLargestNumbers[0] = threeLargestNumbers[1]
    threeLargestNumbers[1] = threeLargestNumbers[2]
    threeLargestNumbers[2] = currentValue
  elif threeLargestNumbers[1] > currentValue:
    threeLargestNumbers[0] = threeLargestNumbers[1]
    threeLargestNumbers[1] = currentValue
  elif threeLargestNumbers[0] > currentValue:
    threeLargestNumbers[0] = currentValue

Time: O(n)
Space: O(1)
'''

array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

def findThreeLargestNumbers(array):
  threeLargestNumbers = [array[0], array[1], array[2]]
  threeLargestNumbers.sort()

  for index in range(3, len(array)):
    swapValues(threeLargestNumbers, array[index])
  return threeLargestNumbers

def swapValues(result, currentValue):
  if result[2] < currentValue:
    result[0] = result[1]
    result[1] = result[2]
    result[2] = currentValue
  elif result[1] < currentValue:
    result[0] = result[1]
    result[1] = currentValue
  elif result[2] < currentValue:
    result[0] = currentValue

print(findThreeLargestNumbers(array))