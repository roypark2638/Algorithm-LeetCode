'''
Palindrome Check

Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.

A palindrome is defined as a string that's written the same foward and backward. Note that single-character strings are palindromes.

Sample input
string = "abcdcba"

Sample output
true
'''

'''
1. create two pointers, one on the first position and one on the last position in array
left = 0
right = len(string) - 1

while left < right:
  we check if left and right char are the same or not
  if it's not same, return False
  increment left pointer
  decrement right pointer
we didn't return False and we are at the end of the loop, return True

Time O(n)
Space O(1)
'''
string = "abcdcba"

def isPalindrome(string):
  left = 0
  right = len(string) - 1
  while  left < right:
    if string[left] != string[right]:
      return False
    left += 1
    right -= 1
  return True

print(isPalindrome(string))