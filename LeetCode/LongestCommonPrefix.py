'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
'''
strs = ["flower","flow","flight"]
output:"fl"

flower
create a pointer to hold the common prefix position and initilize with the length of the first word
store the first word of the strs as a variable longestPrefix
iterate the strs and each word and compare the
find the currentCommonPrefixPosition
store the longestPrefix position between of currentCommonPrefixPosition and longestPrefix
return the result

endPoint = len(strs[0])
longestPrefix = strs[0]
for word in strs[1:]:

Time O(n*w) where n is the length of the strs and w is the length of the word
Space O(1)
'''
strs = ["flower", "flow", "flight"]


def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    firstWord = strs[0]
    endPoint = len(firstWord)
    for word in strs[1:]:
        i = 0
        while i < min(len(word), endPoint):
            if firstWord[i] == word[i]:
                i += 1
            else:
                break
        endPoint = min(endPoint, i)
    return firstWord[0:endPoint]


print(longestCommonPrefix(strs))
