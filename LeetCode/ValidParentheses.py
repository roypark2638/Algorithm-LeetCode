'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
'''
'''
Can I assume that we only have valid input, that is 3 different type of parentheses?
So this one order is matter.
For example,
([{()}]) -> true

({(})) -> False

(){}[]()

I will use stack data structure to keep track the end parantheses.
So, because stack is first in last out, we know what paranthese has to come in order.

Edge case is that can we have a possibly like this case?
(() -> Yes, then we will return true if the stack is empty

- Create an empty stack and hashmaps for parens
- Iterate each value of given s
    if paren is open, then append the value to the stack
    else: pop the stack, if value is None or not matching with the open and end parans, return False
- return true if stack.empty else
Time O(n) Space O(n)
'''


def isValid(self, s):
    parens = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    stack = []
    for paren in s:
        if paren in parens:
            stack.append(paren)
        else:
            if stack:
                openParen = stack.pop()
                if parens[openParen] != paren:
                    return False
            else:
                return False
    return False if len(stack) > 0 else True
