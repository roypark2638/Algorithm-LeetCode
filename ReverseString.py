'''
344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters s. 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

'''

s1 = ["h", "e", "l", "l", "o"]
s2 = ["h", "e", "l", "l", "o"]

# Recursion Time O(n) Space O(n)


def foo1(s):
    helper(s, 0, len(s)-1)
    return s


def helper(s, l, r):
    if l < r:
        s[l], s[r] = s[r], s[l]
        helper(s, l+1, r-1)


# Two pointers Time O(n) Space O(1)
def foo2(s):
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        r -= 1
        l += 1
    return s


print(foo1(s1))
print(foo2(s2))
