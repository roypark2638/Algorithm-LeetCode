var array = [3,5,-4,8,11,1,-1,6]
let targetSum = 10
    
/* Brute-force
 Time: O(N^2)
 Space: O(1)
 1. Outer Loop for N times
 2. Inner loop for N-1 times
 3. add them together compared to targetSum
 4. if it's true, store into array and return
*/

func twoNumberSum1(_ array: inout [Int], _ targetSum: Int) -> [Int] {
    for i in 0..<array.count - 1 {
        let firstNumber = array[i]
        for j in i+1..<array.count {
            let secondNumber = array[j]
            let currentSum = firstNumber + secondNumber
            
            if currentSum == targetSum {
                return [firstNumber, secondNumber]
            }
        }
    }
    return []
}

twoNumberSum1(&array, targetSum)
