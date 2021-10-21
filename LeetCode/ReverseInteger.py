'''
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
'''

'''
- Keep track of the symbol as -1 or 1 to multiple at the end
- x value needs to be converted positive if it's negative
- Iterate until x == 0 and extract last digit for the each iteration and multiply by 10
- Check the bounds of integers of 2**31

Time O(n) where n is the number of x
Space O(1)
'''
x = 1353


def reverse(x):
    symbol = 1
    if x < 0:
        symbol = -1
        x *= -1
    res = 0
    while x:
        res = res * 10 + x % 10
        x /= 10

    return 0 if res > 2**31 else res * symbol


print(reverse(x))
