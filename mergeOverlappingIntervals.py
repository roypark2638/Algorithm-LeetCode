'''
Write a function that takes in a non-empty array of arbitrary intervals, merges any overlapping intervals, and returns the new intervals in no particular order.

Each interval interval is an array of two integers, with interval[0] as the start of the interval and interval[1] as the end of the interval.

Note that back-to-back intervals aren't considered to be overlapping. For example, [1, 5] and [6, 7] aren't overlapping; however, [1, 6] and [6, 7] are indeed overlapping.

Also note that the start of any particular interval will always be less than or equal to the end of that interval.

Sample Input
intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]

Sample Output
[[1, 2], [3, 8], [9, 10]]
'''
'''
- Sort the array based on the startInterval in intervals array
- Create a mergedIntervals to store the result and append the first intervals from the sorted intervals
- Iterate range from 1 to end of the array
  - get the currentStartInterval and previousEndInterval values
  - if currentStart is less than or equal to the previousEndInterval
    - True, Update the mergedIntervals's last interval's endInterval to max value of sortedInterval end or mergedIntervals end
    - False, append the sortedIntervals to mergedIntervals
- return mergedIntervals as the result
'''
intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
def mergeOverlappingIntervals(intervals):
  sortedIntervals = sorted(intervals, key=lambda x: x[0])
  mergedIntervals = []
  mergedIntervals.append(sortedIntervals[0])

  for i in range(1, len(sortedIntervals)):
    currentStart = sortedIntervals[i][0]
    previousEnd = mergedIntervals[-1][1]

    if currentStart <= previousEnd:
      mergedIntervals[-1][1] = max(sortedIntervals[i][1], mergedIntervals[-1][1])
    else:
      mergedIntervals.append(sortedIntervals[i])
  return mergedIntervals


print(mergeOverlappingIntervals(intervals))