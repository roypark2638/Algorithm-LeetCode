'''
Max Subset Sum No Adjacent

Wrtie a function that takes in an array of positive integers and returns the maximum sum of non-adjacent elements in the array.

If the input array is empty, the function should return 0.

Sample Input
array = [75, 105, 120, 75, 90, 135]

Sampel Output
330 // 75 + 120 + 135
'''

array = [75, 105, 120, 75, 90, 135]

# Time O(n) Space O(n)
def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
      return 0
    elif len(array) == 1:
      return array[0]
    res = array[:]
    res[1] = max(array[0], array[1])
    for i in range(2, len(array)):
      res[i] = max(res[i-2] + array[i], res[i - 1])
    return res[-1]

# Optimal solution
# Time O(n) Space O(1)
def maxSubsetSumNoAdjacent2(array):
  if len(array) == 0:
    return 0
  elif len(array) == 1:
    return array[1]
  first = array[0]
  second = max(first, array[1])
  for i in range(2, len(array)):
    curr = max(first + array[i], second)
    first = second
    second = curr
  return second

print(maxSubsetSumNoAdjacent2(array))