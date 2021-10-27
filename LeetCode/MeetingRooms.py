'''
252. Meeting Rooms

Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106
'''


class Solution(object):
    def canAttendMeetings(self, intervals):
        '''
        Sort intervals by meeting starting time in the intervals
        Time O(nlogn) Space O(1)
        Create a variable pre to store the previous meeting ending time in order to detect overlap, initially assign -inf value. Enumerate the intervals and if pre(previoud meeting ending time) is greater than the start(current meeting starting time), which means that we detect the time overlap, so return False. otherwise, assign the pre to the current ending time and keep iterate the intervals.
        '''
        # intervals.sort(key=lambda x:x[0])
        # pre = float('-inf')
        # for start, end in intervals:
        #     if pre > start:
        #         return False
        #     pre = end
        # return True

        '''
        Bruth-force: Time O(n^2) Space O(1)
        Store the ith meeting interval into a variable, pre and jth meeting interval into a variable, curr. If the pre meeting starting is greater than the curr meeting starting time, we swap them in order to have eariler meeting in a pre variable. Now, if pre meeting ending time is greater than the curr meeting starting time, we know there exists a conflict, so return False.
        '''
        for i in range(len(intervals)-1):
            for j in range(i+1, len(intervals)):
                pre, curr = intervals[i], intervals[j]
                if pre[0] > curr[0]:
                    pre, curr = curr, pre
                if pre[1] > curr[0]:
                    return False
        return True
