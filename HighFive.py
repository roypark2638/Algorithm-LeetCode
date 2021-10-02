'''
1086. High Five
Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from a student with IDi, calculate each student's top five average.

Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj and their top five average. Sort result by IDj in increasing order.

A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division.

Example 1:

Input: items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The student with ID = 1 got scores 91, 92, 60, 65, 87, and 100. Their top five average is (100 + 92 + 91 + 87 + 65) / 5 = 87.
The student with ID = 2 got scores 93, 97, 77, 100, and 76. Their top five average is (100 + 97 + 93 + 77 + 76) / 5 = 88.6, but with integer division their average converts to 88.
'''
'''
    - Does it for sure each students have more than 5 scores?
    - If it's less than 5 scores, can I assume to calculate the average given number of scores?
    - What would be the return type? can it be floating point number or integer value?
    
    1. Hashmap with Array
    - create hashmap to store id as a key and scores as value of an array.
    - sort each array of the scores in descending order and get top 5 scores to calculate average score
    - store result in an array with id and average score and sort them in increasing order and return
    
    Time O(nlogn) Space O(n)
    '''
items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [
    2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]


def highFive(items):
    records = {}

    for i, score in items:
        if i in records:
            records[i].append(score)
        else:
            records[i] = [score]

    res = []
    for key, arr in records.items():
        arr.sort(reverse=True)
        average = sum(arr[:5])/5
        res.append([key, average])

    return res


print(highFive(items))
