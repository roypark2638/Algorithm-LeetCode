'''
Array of Products

Write a function that takes in a non-empty array of integers and returns an array of the same length, where each element in the output array is equal to the product of every other number in the input array.

In other words, the value at output[i] is equal to the product of every number in the input array other than input[i].

Note that you're expected to solve this problem without using division.

Sample Input
array = [5, 1, 4, 2]

Sample Output
[8, 40, 10, 20]
'''

'''
- Create a new array with value 1 on each position
- Use for-in loop to store a current leftRunningProduct value into the new array products
- Use another for-in loop to multiple the current products[i] with a current rightRunningProduct value into products array.
- Return products array result.
'''

array = [5, 1, 4, 2]
def arrayOfProducts(array):
  products = [1 for _ in range(len(array))]

  leftRunning = 1
  for i in range(len(array)):
    products[i] = leftRunning
    leftRunning *= array[i]

  rightRunning = 1
  for i in reversed(range(len(array))):
    products[i] *= rightRunning
    rightRunning *= array[i]
  return products

print(arrayOfProducts(array))
