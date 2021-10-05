'''
17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
'''
numberMap = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}
'''
Recursive Backgracking with Hashmap
base case:
i >= len(digits)then return
len(currentString) == len(digits): append the result and return

Iterate len(digits) number of times and iterate current digit of chars to create
newCombinedString
Time O(4^n) Space O(n) where n is the number of the digits
'''


def letterCombinations(self, digits):

    ans = []

    def combineLetters(digits, i, currentString):
        if i >= len(digits):
            return

        if len(currentString) == len(digits):
            ans.append(currentString)
            return

        for char in self.numberMap[digits[i]]:
            newString = currentString + char
            combineLetters(digits, i + 1, newString)

    for i in range(len(digits)):  # O(n) times where n is the length of the digits
        combineLetters(digits, i, "")

    return ans
