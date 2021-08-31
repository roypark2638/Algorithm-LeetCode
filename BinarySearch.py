'''
Binary Search

Write a function that takes in a sorted array of integers as well as a target integer. The function should use the Binary Search algorithm to determine if the target integer is contained in the array and should return its index if it is, otherwise -1.

Sample input
array = [0,1,21,33,45,45,61,71,72,73]
target = 33

Sample output
3
'''

'''
Use 3 pointers, left, right, mid.
left = 0
right = len(array) - 1
mid = (left + right) //2

1. in a while left <= right, check the value in the middle in the array
  2. if the currentValue < target, then move left = mid + 1
  3. elif the currentValue > target, then move right = mid - 1
  4. else the currentValue == target, return the mid
5. if we don't find the target number, return - 1
'''

array = [0,1,21,33,45,45,61,71,72,73]
target = 33

def binarySearch(array, target):
  left = 0
  right = len(array) - 1

  while left <= right:
    mid = (right + left) // 2 # 9 - 0 / 2 = 4
    currentValue = array[mid]
    if target < currentValue:
      right = mid - 1
    elif target > currentValue:
      left = mid + 1
    else:
      return mid
  return -1
    
print(binarySearch(array, target))