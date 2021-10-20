'''
279. Perfect Squares
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 

Constraints:

1 <= n <= 104
'''


class Solution(object):
    '''
    Tabulation

    Algorithm
    - Create an array dp of one or multiple dimentions to hold the values of intermediate sub-solutions, as well as the final solution which is usually the last element in the array. Note that, we createa fictional element dp[0]=0 to simplify the logic, which helps in the case that the remainder (n-k) happends to be a square number.

    - As an additional preparion step, we pre-calculate a list of square numbers (i.e. squareNums) that is less than the given number n.

    - As the main step, we then loop from the number 1 to n, to calculate the solution for each number i(i.e. numSquares(i)). At each iteration, we keep the result of numSquares(i) in dp[i], while resuing the previous results stored in the array.

    - At the end of the loop, we then return the last element in the array as the result of the solution.
    '''

    def numSquares(self, n):
        squareNums = [i**2 for i in range(1, int(math.sqrt(n)+1))]
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for square in squareNums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square]+1)
        return dp[-1]
    '''
    Recursive Solution
    '''
#     def numSquares(self, n, memo = {}):
#         if n in memo:
#             return memo[n]
#         if n < 0:
#             return float('inf')
#         if n == 0 :
#             return 0
#         height = float('inf')
#         sq = 1
#         while n >= pow(sq, 2):
#             height = min(self.numSquares(n- pow(sq, 2)) + 1, height)

#             sq += 1
#         memo[n] = height
#         return memo[n]
