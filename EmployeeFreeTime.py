'''
759. Employee Free Time
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
'''
'''
    Basic Idea
    1. Sort the intervals by starting time
    2. Merge the busy overlapping time
    3. Find diff of merged[i-1].end and merge[i].start
    '''
schedule = [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]


class Solution(object):

    def employeeFreeTime(self, schedule):
        # Flatten the schedule
        ints = []
        for i in schedule:
            [ints.append(x) for x in i]

        # Sort the flattened intervals
        ints.sort(key=lambda x: x.start)

        # Merge the busy overlapping intervals
        merged = []
        for i in ints:
            if not merged or merged[-1].end < i.start:
                merged.append(i)
            else:
                merged[-1].end = max(merged[-1].end, i.end)

        # Find the free time by diff of merged values
        free = []
        for i in range(1, len(merged)):
            free.append(Interval(merged[i-1].end, merged[i].start))

        return free


a = Solution()
print(a.employeeFreeTime(schedule))
