var array = [3,5,-4,8,11,1,-1,6]
let targetSum = 10

/* HashMap
 Time: O(N)
 Space: O(N)
 1. Create an Map
 2. Store first number
 3. targetSum - currentNumber = expectedNumber
 4. if expectedNumber is in the map, return currentNumber and expectedNumber in an array
*/

func twoNumberSum3(_ array: inout [Int], _ targetSum: Int) -> [Int] {
    var numberHashMap = [Int: Bool]()
    
    for number in array {
        let potentialMatch = targetSum - number
        
        if numberHashMap[potentialMatch] == true {
            return [potentialMatch, number]
        } else {
            numberHashMap[number] = true
        }
    }
    
    return []
}

twoNumberSum3(&array, targetSum)
