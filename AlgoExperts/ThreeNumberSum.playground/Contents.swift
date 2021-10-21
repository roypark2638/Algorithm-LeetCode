/*
 Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.
 
 If no three numbers sum up to the target sum, the function should return an empty array.

 Input:
 array = [12,3,1,2,-6,5,-8,6]
 
 output:
 [[-8,2,6], [-8,3,5], [-6,1,5]]
 */

var array = [12,3,1,2,-6,5,-8,6]
var targetSum = 0
/*
 
 1. sort given array
 [-8,-6,1,2,3,5,6,12]
 2. create an empty triplets array
 
 3. for pivot in 0..<array.count-2
    4. create two pointers, left and right. Left = pivot + 1, right array.count - 1
    5. while left < right,
        6. sum up 3 numbers
        - if currentSum == targetSum, store three numbers into triplets
        - if currentSum < targetSum, left += 1
        - if currentSum > targetSum, right -= 1
 7. return triplets
 
 Time O(n^2)
 Space O(n)
 */

func threeNumberSum(array: inout [Int], targetSum: Int) -> [[Int]] {
    var triplets: [[Int]] = []
    array.sort()
    
    for pivot in 0..<array.count - 2 {
        var left = pivot + 1
        var right = array.count - 1
        
        while left < right {
            let currentSum = array[pivot] + array[left] + array[right]
            if currentSum == targetSum {
                triplets.append([array[pivot], array[left], array[right]])
                left += 1
                right -= 1
            }
            else if currentSum < targetSum {
                left += 1
            } else {
                right -= 1
            }
        }
    }
    return triplets
}

threeNumberSum(array: &array, targetSum: targetSum)
