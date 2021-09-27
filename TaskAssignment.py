'''
Task Assignment

You're given an integer k representing a number of workers and an array of positive integers representing durations of tasks that must be completed by the workers. Specifically, each worker must complete two unique tasks adn can only work on one task at a time. The number of t asks will always be equal to 2k such that each worker always has exactly two tasks to complete. All tasks are independent of one another and can be completed in any order. Workers will complete their assigned tasks in parallel, and the time taken to complete all tasks will be equal to the time taken to complete the longest pair of tasks (see the sample output for an explanation).

Write a function thaat returns the optimal assignment of tasks to each worker such taht the tasks are completed as fast as possible.
Your function should return a list of pairs, where each pair stores the indices of the tasks that should be completed by one worker. The pairs should be in the following format: [task1, task2], where the order of task1 and task2 doesn't matter. Your function can return the pairs in any order. If multiple optimal assignments exist, any correct answer will be accepted.

Note: You'll always be given at least one worker (i.e., k will always be greater than 0).

Sample Input
k = 3
tasks = [1, 3, 5, 3, 1, 4]

Sample Output
[
    [0, 2],
    [4, 5],
    [1, 3],
]
'''
'''
- Create a dictionary with an array holding indicies
- Sort the given tasks
- Iterate k times
    - Get indices from left and right of sortedTasks
    - Pop the index of the indices 
    - Store the one and two index to the result
'''
k = 3
tasks = [1, 3, 5, 3, 1, 4]

# Time O(nlogn) Space O(n)


def taskAssignment(k, tasks):
    sortedTasks = sorted(tasks)
    pairedTasks = []
    tasksToIndices = getTasksToIndices(tasks)
    for i in range(k):
        taskOne = sortedTasks[i]
        taskTwo = sortedTasks[len(tasks)-1-i]

        taskOneIndices = tasksToIndices[taskOne]
        taskTwoIndices = tasksToIndices[taskTwo]

        taskOneIdx = taskOneIndices.pop()
        taskTwoIdx = taskTwoIndices.pop()

        pairedTasks.append([taskOneIdx, taskTwoIdx])
    return pairedTasks


def getTasksToIndices(tasks):
    tasksToIndices = {}
    for i, task in enumerate(tasks):
        if task in tasksToIndices:
            tasksToIndices[task].append(i)
        else:
            tasksToIndices[task] = [i]
    return tasksToIndices


print(taskAssignment(k, tasks))
