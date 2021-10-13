'''
322. Coin Change
ou are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
'''


'''
Recurisve Bruth-Force Approach 
Time O(n^m) Space O(m) where n is the number of coins and m is the length of the amount
'''


def coinChangeBruthForce(coins, amount):
    def dfs(coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        minCount = float('inf')
        for coin in coins:
            count = dfs(coins, amount - coin)
            if count == -1:
                continue
            minCount = min(minCount, count + 1)
        return -1 if minCount == float('inf') else minCount
    return dfs(coins, amount)


'''
Recursive Memoization Approach
Time O(n*m) Space O(m) where n is the number of coins and m is the length of the amount
'''


def coinChangeMemo(coins, amount):
    memo = {}

    def dfs(coins, amount):
        if amount in memo:
            return memo[amount]
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        minCount = float('inf')
        for coin in coins:
            count = dfs(coins, amount - coin)
            if count == -1:
                continue
            minCount = min(minCount, count+1)

        memo[amount] = minCount if minCount != float('inf') else -1
        return memo[amount]
    return dfs(coins, amount)


'''
Iterative Tabulation Approach
Time O(n*m) Space O(m)
'''


def coinChangeTabulation(coins, amount):
    ways = [float('inf')] * (amount+1)
    ways[0] = 0
    for coin in coins:
        for i in range(1, len(ways)):
            if i >= coin:
                ways[i] = min(ways[i-coin]+1, ways[i])
    return -1 if ways[-1] == float('inf') else ways[-1]
