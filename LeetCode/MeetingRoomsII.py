'''
253. Meeting Rooms II
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
'''
'''{
    0:[0,30]
    1:[15,25]
    2:[20,35]
    }
    inserted = False
    newStart = 15
    newEnd = 25
    runningEnd = 10
    ,

    # Priority Queues
    '''

# 1. Hashmap holds key as the meeting room number
# If a new meeting starts eariler than currentExistingMEeting's end,
# then create a new meeting room. Otherwise, clear the meeting room and append new meeting with current interval
# Time O(wn + nlogn) O(n + w * logn) where n is the length of the intervals and w is the number of min meeting rooms
# Space O(n)
# def minMeetingRooms(self, intervals):
#     intervals.sort(key=lambda x:x[0]) # Time nlogn
#     dic = {}  # Space O(n) where n is the length of the intervals
#     dic[0] = intervals[0]
#     for inter in intervals[1:]: # Time n
#         newStart, newEnd = inter[0], inter[1]
#         inserted = False
#         for i in range(len(dic)): # Time O(w) w is the number of min meeting rooms
#             runningEnd = dic[i][1]
#             if newStart >= runningEnd:
#                 dic[i] = []
#                 dic[i] = inter
#                 inserted = True
#                 break
#         if not inserted:
#             dic[len(dic)] = inter
#     return len(dic)

# 2. Optimal and better solution.
# Checking how many meetings begin before the earliest ended meeting ends
# For example, if 3 meetings have started before the earliest possible meeting end, than we need 3 rooms
# Sorting helps in two things.
# 1. Find what's the earliest meeting ends time
# 2. It allows you to start looking for meetings ends only from next element in the ends array when you find some meeting
# start that is after the current end, because all other meeting ends before the current in the sorted array
# will also be before the current meeting start. So you just have to run 1 time over each array.
# Time O(nlogn) Space O(n) where n is the legnth of the intervals


def minMeetingRooms(self, intervals):
    starts = [interval[0] for interval in intervals]
    ends = [interval[1] for interval in intervals]
    starts.sort()
    ends.sort()

    rooms = 0
    endIntervalIdx = 0
    for i in range(len(starts)):
        if starts[i] < ends[endIntervalIdx]:
            rooms += 1
        else:
            endIntervalIdx += 1
    return rooms
