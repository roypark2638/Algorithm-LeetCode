'''
359. Logger Rate Limiter

Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the Logger class:

Logger() Initializes the logger object.
bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.
Input
["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
Output
[null, true, true, false, false, false, true]

Explanation
Logger logger = new Logger();
logger.shouldPrintMessage(1, "foo");  // return true, next allowed timestamp for "foo" is 1 + 10 = 11
logger.shouldPrintMessage(2, "bar");  // return true, next allowed timestamp for "bar" is 2 + 10 = 12
logger.shouldPrintMessage(3, "foo");  // 3 < 11, return false
logger.shouldPrintMessage(8, "bar");  // 8 < 12, return false
logger.shouldPrintMessage(10, "foo"); // 10 < 11, return false
logger.shouldPrintMessage(11, "foo"); // 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21
'''


# Use two hashmap and it can manage the memory usage
# latest is last time that cacheNew is created(and first log inserted at the same time). We don't insert message into cacheOld.
# - All of the messages in cacheOld have older timestamp than latest.
# - All of the messages in cacheNew have newer timestamp than latest, but older timestamp than latest + 10.
# We compare the current timestamp with latest,
# - If timestamp >= lastest + 20, then all messages in both cacheNew and cacheOld have older timestamp than timestamp - 10, we can clean them all.
# - If timestamp >= latest + 10, then all messages in cacheOld have older timestamp than timestamp - 10, we can clean messages in cacheOld.
# - Otherwise, we need to check if either cacheNew or cacheOld contains the message.
def __init__(self):
    self.newerMessages = {}
    self.oldMessages = {}
    self.timeLastSeen = 0


def shouldPrintMessage(self, timestamp, message):
    if timestamp >= self.timeLastSeen + 20:
        self.newerMessages.clear()
        self.oldMessages.clear()
        self.timeLastSeen = timestamp
    elif timestamp >= self.timeLastSeen + 10:
        self.oldMessages = self.newerMessages
        self.newerMessages = {}
        self.timeLastSeen = timestamp

    if message in self.newerMessages:
        return False
    if message in self.oldMessages and timestamp < self.oldMessages[message] + 10:
        return False
    self.newerMessages[message] = timestamp
    return True


# Simpler, one hashmap
# Time O(1) Space O(n)
# Disadvantage is that memory usage never stop growing.

#     def __init__(self):
#         self.timestampMap = {}

#     def shouldPrintMessage(self, timestamp, message):
#         if message not in self.timestampMap or timestamp >= self.timestampMap[message]:
#             self.timestampMap[message] = timestamp + 10
#             return True
#         return False
