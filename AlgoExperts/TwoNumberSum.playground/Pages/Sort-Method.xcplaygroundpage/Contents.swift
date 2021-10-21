var array = [3,5,-4,8,11,1,-1,6]
let targetSum = 10

/* Sort the array
 Time: O(nLog(n))
 Space: O(1)
 1. Sort the array
 [-4,-1,1,3,5,6,8,11]
 2. Set two pointers at left and right
 3. Sum up two numbers and if it's matched with targetSum, return two numbers in an array
    - If currentSum is greater than targetSum, move the right pointer to the left
    - If currentSum is less than targetSum, move the left pointer to the right
 */

func twoNumberSum2(_ array: inout [Int], _ targetSum: Int) -> [Int] {
    array.sort()
    var left = 0
    var right = array.count - 1
    
    while left < right {
        let currentSum = array[left] + array[right]
        
        if currentSum == targetSum {
            return [array[left], array[right]]
        }
        else if currentSum < targetSum {
            left += 1
        }
        else {
            right -= 1
        }
    }
    
    return []
}

twoNumberSum2(&array, targetSum)
