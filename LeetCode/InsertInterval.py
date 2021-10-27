'''
57. Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
Example 3:

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]
Example 4:

Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]
Example 5:

Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105

'''


class Solution(object):
    '''
    Sort: Time O(nlog) Space O(n)
    Append the new interval into the given intervals array. Then sort the array by the starting time. Iterate the array and merge the overlapping intervals.
    '''
#     def insert(self, intervals, newInterval):
#         intervals.append(newInterval)
#         intervals.sort(key=lambda x:x[0])

#         merged = []
#         for i in range(len(intervals)):
#             if not merged:
#                 merged.append(intervals[i])
#             else:
#                 if merged[-1][1] >= intervals[i][0]:
#                     merged[-1][1] = max(merged[-1][1], intervals[i][1])
#                 else:
#                     merged.append(intervals[i])
#         return merged

    '''
    Greedy algorithm: Time O(n) Space O(n)
    Create a new array merged and append intervals where the start time is less the new interval. 
    If it merged array has at least one interval and the interval is overlapped with new interval, then merge with new interval. Otherwise, simply append new interval into the merged array. 
    Now, our merged array is needed to append the left over intervals and also check if the intervals are needed to be merged. Previously our initial loop to insert intervals before the new interval doesn't need to check if it's needed to merge because given intervals doesn't have overlapped intervals.
    '''
    # When intervals is empty
    # When inserting point is at the last index

    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        merged = []
        i = 0
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        if merged and merged[-1][1] >= newInterval[0]:
            merged[-1][1] = max(merged[-1][1], newInterval[1])
        else:
            merged.append(newInterval)

        for j in range(i, len(intervals)):
            if merged[-1][1] >= intervals[j][0]:
                merged[-1][1] = max(merged[-1][1], intervals[j][1])
            else:
                merged.append(intervals[j])
        return merged
