'''
Permutations

Write a function that takes in an array of unique integers and returns an array of all permutations of those integers in no particular order.

If the input array is empty, the function should return an empty array.

Sample input
array = [1, 2, 3]

Sample output
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
'''

'''
recursion

helper(array, perm, perms, index)
if

'''
array = [1, 2, 3]

def getPermutations(array):
    permutations = []
    permutationHelper(0, array, permutations)
    return permutations
    
def permutationHelper(i, array, perms):
    if i == len(array)
