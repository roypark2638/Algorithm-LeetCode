'''
6. ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
'''
'''
    - If numRow is less than equal to 1, return original string
    - Increment the pointer to find the correct position to append
    - First and last row has one jump, in other words, it has one element to append
    - The other rows in between first and last have two elements to append
    - Increment value can be calculated by (numRows - 1) * 2
    - Increment value in between first and last can be calculated by (increment + currentPosition - (2 * currentRow)) -> and make sure to check the bounds

    '''
s = "PAYPALISHIRING"
numRows = 4


def convert(s, numRows):
    if numRows <= 1:
        return s
    res = ""

    for row in range(numRows):
        increment = (numRows-1) * 2
        for i in range(row, len(s), increment):
            res += s[i]
            if row > 0 and row < numRows - 1 and increment + i - 2 * row < len(s):
                res += s[increment+i-2*row]
    return res


print(convert(s, numRows))
