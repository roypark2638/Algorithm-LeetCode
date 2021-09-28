'''
832. Flipping an Image

Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].

Example 1:

Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
'''
'''
1. reverse each row
image = [
    [0, 1, 1],
    [1, 0, 1],
    [0, 0, 0]
]
2. invert 0 to 1 and 1 to 0
output = [
    [1, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]

1. bruth force and two pointers
- swap the value at each row(reverse row)
- invert 0 to 1 and 1 to 0

Time O(nm) Space O(1)
'''

image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]


def flipAndInvertImage(image):
    def reverseRow(arr):
        l, r = 0, len(arr) - 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    for row in image:
        reverseRow(row)

    for row in range(len(image)):
        for col in range(len(image[row])):
            curr = image[row][col]
            if curr == 0:
                image[row][col] = 1
            else:
                image[row][col] = 0
    return image


print(flipAndInvertImage(image))
