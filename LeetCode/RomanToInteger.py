'''
13. Roman to Integer

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
Given a roman numeral, convert it to an integer.
Example 1:

Input: s = "III"
Output: 3
Example 2:

Input: s = "IV"
Output: 4
Example 3:

Input: s = "IX"
Output: 9
'''
s = "III"

'''
    - I X C can only be placed once before those roman?
    - Can the s value is always valid, which that always higher number comes first except those given exception?
    - What's teh constraints for s?


    - Hashmap romanToInt
    - Store all the symbol and value + specical cases that smller comes eariler than larger
    - Iterate s and add up the totals
    - Check if roman is "I", "X", or "C" and it's not the last index,
        - grab 2 char if it's in the hashmap
            - yes, then add that number and increment index
            - no, just grab one char and add
        - increment index

    - Time O(1) Space O(1) because s is constant 15 and space is also finite constant numbers

    e.g.
    ["III"] 3
    ["LXLIVIV"]
    roman = I
    combined = IV
    total = 98
    i = 7
    len(s) = 7
    '''
romanToIntMap = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000
}


def romanToInt(s):
    # i = 0
    # total = 0
    # while i < len(s):
    #     roman = s[i]
    #     if i < len(s) - 1 and s[i:i+2] in romanToIntMap:
    #         total += romanToIntMap[s[i:i+2]]
    #         i += 2
    #     else:
    #         total += romanToIntMap[roman]
    #         i += 1
    # return total

    tot = 0
    i = 0
    while i < len(s):
        if i < len(s)-1 and romanToIntMap[s[i]] < romanToIntMap[s[i+1]]:
            tot += romanToIntMap[s[i+1]] - romanToIntMap[s[i]]
            i += 2
        else:
            tot += romanToIntMap[s[i]]
            i += 1
    return tot


print(romanToInt(s))
