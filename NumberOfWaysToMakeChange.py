'''
Number Of Ways To Make Change

Given an array of distinct positive integers representing coin denominations and a single non-negative interger n representing a target amount of money, write a function that returns the number of ways to make change for that target amount using the given coin denominations.

Note that an unlimited amount of coins is at your disposal.

Sample Input
n = 6
denoms = [1, 5]

Sample Output
2
'''
'''
- Dynamic Programming
- create an array with nth number of 0s with array[0] = 1
- each array position represents the number of ways to make the change
- find out how many ways we can make with each denom
- if denom <= ways[amount]: then ways[amount] += ways[amount - demon]
'''

n = 10
denoms = [1, 5, 10 ,25]
def numberOfWaysToMakeChange(n, denoms):
  ways = [0 for amount in range(n+1)]
  ways[0] = 1
  for denom in denoms:
    for amount in range(denom, n+1):
      if amount >= denom:
        ways[amount] += ways[amount - denom]
  return ways[-1]  

print(numberOfWaysToMakeChange(n, denoms))
