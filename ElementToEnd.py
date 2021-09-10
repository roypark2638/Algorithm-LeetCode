'''
Element To End

You're given an array of integers and an integer. Write a function that moves all instances of that integer in the array to the end of the array and returns the array.

The function should perform this in place (i.e, it should mutate the input array) and doesn't need to maintain the order of the other integers.

Sample Input
array = [2,1,2,2,2,3,4,2]
toMove = 2

Sample Output
[1,3,4,2,2,2,2,2]
'''

'''
create two pointers left and right
find the target number index from the left
find the non-target number index from the right
and swap them until left is less than right
'''

array = [2,1,2,2,2,3,4,2]
toMove = 2
def moveElementToEnd(array, toMove):
    left = 0
    right = len(array) - 1

    while left < right:
        while left < right and array[left] != toMove:
            left += 1
        while left < right and array[right] == toMove:
            right -= 1
        temp = array[left]
        array[left] = array[right]
        array[right] = temp
        
    return array

print(moveElementToEnd(array, toMove))

