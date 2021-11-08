'''
647. Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
'''


class Solution(object):
    '''
    When we are checking the string is palindrom, we have to check two conditions.
    - odd length 
    - even length

    Iterate the given string, increment the count by 1.
    Then we will call this function twice one for expending odd length and another one is for expending even length.
    FindPalindrom function
    - Check if left and right index are in the bounds and the characters in the left and right are equal.
        - Then increment the palindrome count and move the left to the left and right to the right by one
    - return the count
    '''

    def countSubstrings(self, s):
        self.count = 0
        for i in range(len(s)):
            self.count += 1
            self.findPalindrome(i-1, i+1, s)
            self.findPalindrome(i, i+1, s)
        return self.count

    def findPalindrome(self, left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            self.count += 1
            left -= 1
            right += 1
