/* https://www.algoexpert.io/questions/Non-Constructible%20Change
 Given an array of positive integers representing the values of coins in your possession, write a function that returns the minimum amount of change (the minimum sum of money) that you cannot create. The given coins can have any positive integer value and aren't necessarily unique (i.e., you can have multiple coins of the same value).
 
 For example, if you're given coins = [1,2,5], the minimum amount of change that you can't create is 4. If you're given no coins, the minimum amount of change that you can't create is 1.
 
 Inout
 coins = [5,7,1,1,2,3,22]
 Output
 20
 */

/*
 1. sort the array
 [1,1,2,3,5,7,22]
 
 2. loop through all the coins and if the coin > currentChange + 1 then we cannot the next coin so return currentChange + 1. Otherwise, set currentChange += coin
 
 */
var coins: [Int] = [5,7,1,1,2,3,22]

func nonConstructibleChange(_ coins: inout [Int]) -> Int {
    coins.sort()
    var currentChange = 0
    
    for coin in coins {
        if coin > currentChange + 1 {
            return currentChange + 1
        }
        
        currentChange += coin
    }
    return currentChange + 1
}

nonConstructibleChange(&coins)
