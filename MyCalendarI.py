'''
729. My Calendar I

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
'''

'''
1. Binary Search Tree structure
- Find the correct index of the interval
- Make sure that the left and right intervals don't intersect
Time O(logn) Space O(h)
'''


class Node():
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left, self.right = None, None


class MyCalendar(object):
    def __init__(self):
        self.root = None

    def bookHelper(self, node, start, end):
        if node.end <= start:
            if node.right is None:
                node.right = Node(start, end)
                return True
            else:
                return self.bookHelper(node.right, start, end)
        elif node.start >= end:
            if node.left is None:
                node.left = Node(start, end)
                return True
            else:
                return self.bookHelper(node.left, start, end)
        return False

    def book(self, start, end):
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.bookHelper(self.root, start, end)


# class MyCalendar(object):
#     #class Node(object):
#         # def __init__(self, val = (0, 0), prev = None, next = None):
#         #     self.val = val
#         #     self.prev = prev
#         #     self.next = next

#     '''
#     Is new start time is always smaller than previous start time?

#      case 1: appending to the beginning
#      case 2: appending to the middle
#      case 3: appending to the end

#     '''
#     def __init__(self):
#         # self.head = Node()
#         self.schedule = []

#     # def book(self, start, end):
# #         if not self.schedule:
# #             self.schedule.append([start, end])
# #             return True

# #         for i in range(len(self.schedule)):
# #             currStart = self.schedule[i][0]
# #             currEnd = self.schedule[i][1]
# #             flag = False

# #             if i == 0 and end <= currStart:
# #                 # append to the beginning
# #                 self.schedule.append([start, end])
# #                 flag = True

# #             elif i > 0 and i < len(self.schedule) and self.schedule[i-1][1] <= start and end <= currStart:
# #                 # append to the middle

# #                 self.schedule.append([start, end])
# #                 flag = True
# #             elif i == len(self.schedule) - 1 and self.schedule[-1][1] <= start:
# #                 self.schedule.append([start, end])
# #                 flag = True


# #             if flag:
# #                 self.schedule.sort()
# #                 return True
# #         return False


# # Your MyCalendar object will be instantiated and called as such:
# # obj = MyCalendar()
# # param_1 = obj.book(start,end)
