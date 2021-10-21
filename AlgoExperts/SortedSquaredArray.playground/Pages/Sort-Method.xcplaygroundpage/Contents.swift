// https://www.algoexpert.io/questions/Sorted%20Squared%20Array

/*
 Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order.
 
 Input
 [1,2,3,5,6,8,9]
 Output
 [1,4,9,25,36,64,81]
 */

/*
 Time O(nLog(n))
 Space O(n)
 
 1. create an array with same length of the given array
 2. loop the array and square the value and append it to the new array
 3. sort the new array and return it

 */

let array = [-5,-3,-1,4]
func sortedSquaredArray(_ array: [Int]) -> [Int] {
    var sortedSquares = Array(repeating: 0, count: array.count)
    
    for index in array.indices {
        let value = array[index]
        sortedSquares[index] = value * value
    }
    
    sortedSquares.sort()
    return sortedSquares
}

sortedSquaredArray(array)
