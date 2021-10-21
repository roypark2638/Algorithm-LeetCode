'''
12. Integer to Roman

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Example 1:

Input: num = 3
Output: "III"
Example 2:

Input: num = 4
Output: "IV"
Example 3:

Input: num = 9
Output: "IX"
Example 4:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
'''

'''
    - I assume that I can't form the answer with lower roman value first than higher value except those special cases
    - And I have to coordinate to make those special number(4, 9, 40, 90, ...) to be given format.

    1. Approach
    - if 1024 > 1000, then subtract and append the roman
    - 24 - 10
    - 10 - 14
    - 4 - 4

    - roman = "" # store the roman
    - loop until num is equal to 0
        - loop hashMap of array in order where larger number comes first
        - if hashValue < num then subtract and add that key of roman to the result string

    Time O(1) Space O(1)

    '''
num = 58

romanToIntMap = {
    0: ["I", 1],
    1: ["IV", 4],
    2: ["V", 5],
    3: ["IX", 9],
    4: ["X", 10],
    5: ["XL", 40],
    6: ["L", 50],
    7: ["XC", 90],
    8: ["C", 100],
    9: ["CD", 400],
    10: ["D", 500],
    11: ["CM", 900],
    12: ["M", 1000]
}


def intToRoman(num):
    roman = ""
    while num != 0:
        for key, romanMap in reversed(romanToIntMap.items()):
            key, value = romanMap[0], romanMap[1]
            if num >= value:
                roman += key
                num -= value
                break
    return roman


print(intToRoman(num))
