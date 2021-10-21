'''
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''

'''
The water afrea will always be limited by the height of the shorter line. Futher, the father the line, the more will be the water area obtained.

- Use two pointers, one at the beginning and one at the end
- Calculate the water area and keep track of the most water area
- Move shorter height line toward other end by one step

'''
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]


def maxArea(height):
    mostWater = 0
    left, right = 0, len(height)-1
    while left < right:
        currWater = min(height[left], height[right]) * (right-left)
        mostWater = max(mostWater, currWater)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return mostWater

# Bruth-Force
# def maxArea(self, height):
#     mostWater = 0
#     n = len(height)
#     for i in range(n-1):
#         for j in range(i, n):
#             water = min(height[i], height[j]) * (j-i)
#             if water > mostWater:
#                 mostWater = water
#     return mostWater


print(maxArea(height))
