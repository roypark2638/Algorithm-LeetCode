'''
1047. Remove All Adjacent Duplicates In String
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
'''


class Solution(object):
    '''
    - All lowercase English letters
    - Remove all the adjacent characters

    We use a stack to find the non-duplicate characters.
    Iterate the characters in the given string and store each char one by one and check if current character is equal to the last element in the stack. If true pop the last element. At the end of the loop, return the stack.
    Time O(n) Space O(n)
    '''

    def removeDuplicates(self, s):
        stack = []
        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
