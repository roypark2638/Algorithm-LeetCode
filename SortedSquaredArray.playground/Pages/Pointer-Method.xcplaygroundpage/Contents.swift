// https://www.algoexpert.io/questions/Sorted%20Squared%20Array

/*
 Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order.
 
 Input
 [1,2,3,5,6,8,9]
 Output
 [1,4,9,25,36,64,81]
 */

/*
 Time O(N)
 Space O(N)
 
 1. create array with the same length of the given array
 2. create pointers for left, right and index
 3. loop while left <= right
    * fill the array from the back with larger number
    * move the pointer and index accordingly
 */

let array = [-5,-3,-1,4]

func sortedSquaredArray2(_ array: [Int]) -> [Int] {
    var sortedSquares = Array(repeating: 0, count: array.count)
    
    var left = 0
    var right = array.count - 1
    var index = array.count - 1
    
    while left <= right {
        let leftValue = array[left]
        let rightValue = array[right]
        
        if abs(leftValue) > abs(rightValue) {
            sortedSquares[index] = leftValue * leftValue
            left += 1
        } else {
            sortedSquares[index] = rightValue * rightValue
            right -= 1
        }
        index -= 1
    }
    
    return sortedSquares
}

sortedSquaredArray2(array)
