'''
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
'''
'''
Approach 1: Longest Common Substring -> fails e.g. s=bcdgfdcb
Approach 2: Brute Force, Time O(n^3) Space O(1)
Approach 3: Dynamic Programming Time O(n^2) Space O(1)

Approach 3.
Check two conditions 
1. s[i-1] and s[i+1]
2. s[i] and s[i+1]
If it's palindrom, then expand both left and right to find the longest palindrome
'''
s = "babad"


def longestPalindrome(s):
    start, end = 0, 0

    def updatePointersOfPalindrom(start, end, left, right, i):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if end - start < right-left:
                start, end = left, right
            left -= 1
            right += 1
        return (start, end)
    for i in range(len(s)):
        left, right = i-1, i+1
        start, end = updatePointersOfPalindrom(start, end, left, right, i)
        left, right = i, i+1
        start, end = updatePointersOfPalindrom(start, end, left, right, i)
    return s[start: end+1]


print(longestPalindrome(s))
