'''
Disk Stacking

You're given a non-empty array of arrays where each subarray holds three integers and represents a disk. These integers denote each disk's width, depth, and height, respectively. Your goal is to stack up the idsks and to maximize the total height of the stack. A disk must have a strictly smaller width, depth, and height than any other disk below it.

Write a function that returns an array of the disks in the final stack, starting with the top disk and ending with the bottom disk. Note that you can't rotate disks; in other words, the integers in each subarray must represent [width, depth, height] at all times.

You can assume that there will only be one stack with the greatest total height.

Sample Input
disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]

Sample Output
[[2, 1, 2], [3, 2, 3], [4, 4, 5]]
'''

disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]


def diskStacking(disks):
    disks.sort(key=lambda disk: disk[2])
    heights = [disk[2] for disk in disks]
    sequences = [None for disk in disks]
    maxHeightIdx = 0
    for i in range(1, len(disks)):
        currentDisk = disks[i]
        for j in range(i):
            otherDisk = disks[j]
            if isStackable(currentDisk, otherDisk):
                if heights[i] < heights[j] + currentDisk[2]:
                    heights[i] = heights[j] + currentDisk[2]
                    sequences[i] = j
        if heights[i] > heights[maxHeightIdx]:
            maxHeightIdx = i
    return buildSequence(disks, sequences, maxHeightIdx)


def isStackable(c, o):
    return c[0] > o[0] and c[1] > o[1] and c[2] > o[2]


def buildSequence(disks, sequences, currIdx):
    sequence = []
    while currIdx != None:
        sequence.append(disks[currIdx])
        currIdx = sequences[currIdx]
    return list(reversed(sequence))


print(diskStacking(disks))
