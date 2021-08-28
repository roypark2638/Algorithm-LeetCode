'''
Class Photos

It's photo day at the local school, and you're the photographer assigned to take class photos.
The class that you'll be photographing has an even number of students, and all these students are wearing red or blue shirts.
In fact, exactly half of the class is wearing red shirts, and the other half is wearing blue shirts.
You're responsible for arranging the students in two rows before taking the photo. Each row should contain the same
number of the students and should adhere to the following guidelines:

    - All students wearing red shirts must be in the same row.
    - All students wearing blue shirts must be in the same row.
    - Each student in the back row must be strictly taller than the student directly in front of them in the front row.

You're given two input array: one containing the heights of all the students with red shirts and another one containg
the heights of all the students with blue shirts. These arrays will always have the same length, and each height will be
a positive integer. Write a function that returns whether or not a class photo that follows the stated guidelines can be taken.

Note: You can assume that each class has at least 2 students.

Sample input
redShirtHeights = [5,8,1,3,4]
blueShirtHeights = [6,9,2,4,5]
'''

redShirtHeights = [5,8,1,3,4]
blueShirtHeights = [6,9,2,4,5]

'''
- find the tallest student and place that color of student group to the back.
blue =[9,6,5,4,2]
red = [8,5,4,3,1]

1. sort the array in descending order
2. find the tallest group and put the tallest group to the back
3. compare each value if every student fits to the rules
'''

def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    if redShirtHeights[0] > blueShirtHeights[0]:
        if compareHeights(blueShirtHeights, redShirtHeights) == False:
            return False
    else:
        if compareHeights(redShirtHeights, blueShirtHeights) == False:
            return False
    return True

def compareHeights(smaller, taller):
    for index in range(len(taller)):
        if taller[index] <= smaller[index]:
            return False

print(classPhotos(redShirtHeights, blueShirtHeights))