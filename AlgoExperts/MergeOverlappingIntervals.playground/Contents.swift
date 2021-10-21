/*
 Write a function that takes in a non-empty array of arbitrary intervals, merges any overlapping intervals, and returns the new intervals in no particular order.
 
 Each interval is an array of two integers, with interval[0] as the start of the interval and interval[1] as the end of the interval.
 
 Note that back-to-back intervals aren't considered to be overlapping. For example, [1,5] and [6,7] aren't overlapping; however, [1,6] and [6,7] are indeed overlapping.
 
 Also Note that the start of any particular interval will always be less than or equal to the end of that interval.
 
 Input
 intervals = [[1,2],[3,5],[4,7],[6,8],[9,10]]
 
 Output
 [[1,2],[3,8],[9,10]]
 */

/*
 Time O(nLogn) ; Space O(n)
 1. sort by start time
 2. create empty mergedIntervals for result
 3. create currentInterval variable
 4. insert first interval into the result array
 5. loop the intervals
    6. get currentIntervalEnd
    7. get nextIntervalStart and End
    8. if overlapping
        9. Yes -> get the max from currentEnd & nextEnd and update existing intervals from the merged result array
        10. No  -> assign nextInterval to currentInterval
            11. append the updated currentInterval to the result array
 */

let intervals: [[Int]] = [[1,2],[3,5],[4,7],[6,8],[9,10]]

func mergeOverlappingIntervals(_ intervals: [[Int]]) -> [[Int]] {
    let sortedIntervals = intervals.sorted(by: { $0[0] < $1[0] })
    
    var mergedIntervals: [[Int]] = []
    var currentInterval = sortedIntervals[0] // [1,2]
    mergedIntervals.append(sortedIntervals[0]) // [[1,2]]
    
    for nextInternal in sortedIntervals { // [1,2]
        let currentIntervalEnd = currentInterval[1] // 2
        let (nextIntervalStart, nextIntervalEnd) = (nextInternal[0], nextInternal[1]) // 1,2
    
        if currentIntervalEnd >= nextIntervalStart {
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
            mergedIntervals[mergedIntervals.count - 1][1] = currentInterval[1]
        } else {
            currentInterval = nextInternal // [1,2]
            mergedIntervals.append(currentInterval)
        }
    }
    
    return mergedIntervals
}

mergeOverlappingIntervals(intervals)
