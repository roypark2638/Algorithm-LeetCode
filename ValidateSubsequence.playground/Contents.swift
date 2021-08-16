// https://www.algoexpert.io/questions/Validate%20Subsequence

let array = [5,1,22,25,6,-1,8,10]
let sequence = [1,6,-1,10]

/*
 loop the array
 1. set sequence index = 0 and final index = sequence.count
 2. increment index
    * if sequence == array -> increment both
    * if sequence != array -> increment array only
 3. if sequence index == sequence.count -> true
 
 Time O(N)
 Space O(1)
 */

func isValidSubsequence(_ array: [Int], _ sequence: [Int]) -> Bool {
    var sequenceIndex = 0
    
    for num in array {
        if sequence[sequenceIndex] == num {
            
            sequenceIndex += 1
            if sequenceIndex == sequence.count {
                return true
            }
        }
    }

    return false
}

isValidSubsequence(array, sequence)
