'''
Monotonic Array

Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.

Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. Similarly, non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.

Note that empty arrays and arrays of one element are monotonic.

Sample Input
array = [-1,-5,-10,-1100,-1100,-1101,-1102,-9001]

Sample Output
true
'''

'''
- check if the length of array <= 2 then return true
- get first direction by array[1] - array[0]
- loop through the array from range 2
  - check if the direction is meaningful 
  - if direction == 0: then update direction and continue
  - check if direction is broken: then return False
- end of the loop, return true
  
'''
array = [-1,-5,-10,-1100,-1100,-1101,-1102,-9001]
def isMonotonic(array):
  if len(array) <= 2:
    return True

  direction = array[1] - array[0]
  for i in range(2, len(array)):
    if direction == 0:
      direction = array[i] - array[i-1]
      continue
    if breaksDirection(direction, array[i-1], array[i]):
      return False
  return True

def breaksDirection(direction, prev, curr):
  diff = curr - prev
  if direction > 0:
    return diff < 0
  return diff > 0
    

print(isMonotonic(array))