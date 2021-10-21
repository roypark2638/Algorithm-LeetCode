'''
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0
'''
'''
    - is it only lower characters?
    - upper characters? or special chracters?

    Hashmap {char:i}
    - iterate string
    - if char exist in the map
        - update max(currentStartIndex, hashmap[char] + 1)
    - update the hashmap with char and i
    - calculate longestLength

    Time O(n) Space O(n) where n is the length of the given string.
    }
    '''


def lengthOfLongestSubstring(self, s):
    longestLen = 0
    currentStartIndex = 0

    charTable = {}

    for i, char in enumerate(s):
        if char in charTable:
            currentStartIndex = max(charTable[char] + 1, currentStartIndex)
        charTable[char] = i
        longestLen = max(longestLen, i - currentStartIndex + 1)

    return longestLen
