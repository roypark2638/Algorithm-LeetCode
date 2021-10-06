'''
853. Car Fleet
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation: 
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.
Example 2:

Input: target = 10, position = [3], speed = [3]
Output: 1
'''
'''
    - Create a data array of tuple to hole position and speed with the same index position
    - Sort that array based on the position in descending order beacuse the cars are not allowed to pass a car in front. So we will start looking at the car positioned at the closest to the target.
    - If the arrival time to the target conflict with the previous car, than it's combined as one fleet. So if it's not conflict, then we will count the number of fleet. In order to do that, keep track of the previousFinishTime. If previousFinsihTime is smaller than currentFinishTime than update the previousFinishTime and increment fleet. It means that a car behind couldn't catup the car in front, so it's arrived saparately.

    '''

target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]


def carFleet(target, position, speed):
    cars = [(pos, vel) for pos, vel in zip(position, speed)]
    cars.sort(reverse=True, key=lambda x: x[0])

    fleet = 0
    prev = 0

    for pos, vel in cars:
        destination = target - pos
        finishTime = float(destination) / vel

        if prev < finishTime:
            prev = finishTime
            fleet += 1
    return fleet


print(carFleet(target, position, speed))
