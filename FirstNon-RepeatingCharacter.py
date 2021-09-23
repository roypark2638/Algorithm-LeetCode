'''
First Non-Repeating Character

Write a function that takes in a string of lowercase English-alphabet letters and returns the index of the string's first non-repeating character.

The first non-repeating character is the first character in a string that occurs only once.

If the input string doesn't have any non-repeating characters, your function should return -1.

Sample Input
string = "abcdcaf"

Sample Output
1
'''
'''

'''
string = "abcdcaf"

# Time O(n), Space O(1)
# Space is constant because lowercase English-alphabet letters are constant


def firstNonRepeatingCharacter(string):
    charFrequency = {}
    for char in string:
        if char in charFrequency:
            charFrequency[char] += 1
        else:
            charFrequency[char] = 1

    for i in range(len(string)):
        if charFrequency[string[i]] == 1:
            return i
    return -1


print(firstNonRepeatingCharacter(string))
