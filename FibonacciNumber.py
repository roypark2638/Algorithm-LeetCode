'''
509. Fibonacci Number
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


'''
memoize = {0: 0, 1: 1}


def fib(n):
    if n in self.memoize:
        return self.memoize[n]
    else:
        self.memoize[n] = self.fib(n-1) + self.fib(n-2)
        return self.memoize[n]

    # Most Optimal Iterative
    # Time O(n) Space O(1)
    # def fib(self, n):
    #     fibs = [1, 1]
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return 1
    #     for i in range(2, n):
    #         val = fibs[0] + fibs[1]
    #         fibs[0] = fibs[1]
    #         fibs[1] = val
    #     return fibs[-1]

    # Iterative
    # Time O(n) Space O(n)
    # def fib(self, n):
    #     fibs = [1,1]
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return 1
    #     for i in range(2,n):
    #         fibs.append(fibs[i-1] + fibs[i-2])
    #     return fibs[-1]

    # Recursion Bruth Force
    # Time O(2^n) Space O(n)
    # def fib(self, n):
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return 1
    #     return self.fib(n-1) + self.fib(n-2)
