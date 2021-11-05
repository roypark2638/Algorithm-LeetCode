'''
Rod Cutting from CTCI

Given a rod of length n indches and a table of prices pi for i = 1,2,...,n, determine the maximum revenue forn obtainable by cutting up the rod and selling the pieces.
'''

prices = [1, 5, 8, 9]
n = 4

'''
Tabulation: Time O(n^2) Space O(n)

We want to solve smaller subproblems to solve next bigger subproblem. We know when the rod length is equal to zero, the profit is zero, which is our base case. We want to build every subproblem i = 0,1,...,n to find optimal solution at this position i. For example, when i = 2, we have two ways to compare to get the maximum profit, (1 rod + 1 rod) or (2 rod). When i = 3, we have three ways, (1 rod + 1 rod + 1 rod), (2 rod, 1 rod), (3 rod) and so on. Thus, we can store the previous maximum profit into an array to look up to find current optimal solution at index i. Since we have multiple ways to cut the rods, we have all the possible previous cutting ways to get the current maximum profit. We need to use two for loops, outer loop i iterates from index 1 to n+1 and inner loop iterats from index 1 to i+1. Find the inner loop's maximum profit by comparing the all the possible previous cutting ways, maxProfit = max(maxProfit, prices[j] + profits[i-j]). When we finish each inner loop, we want to update the profits[i] with the maxProfit that we found.
'''


def cutRodTabu(prices, n):
    profits = [0] * (n+1)
    for i in range(1, n+1):
        maxProfit = float('-inf')
        for j in range(1, i+1):
            maxProfit = max(maxProfit, prices[j-1] + profits[i-j])
        profits[i] = maxProfit
    return profits[-1]


print(cutRodTabu(prices, n))

'''
Memoization: Time O(n^2) Space O(n)
'''


def cutRodMemo(prices, n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    maxProfit = float('-inf')
    for i in range(1, n+1):
        maxProfit = max(maxProfit, prices[i-1] + cutRodMemo(prices, n-i, memo))
    memo[n] = maxProfit
    return maxProfit


print(cutRodMemo(prices, n))
