'''
1570. Dot Product of Two Sparse Vectors

Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

Example 1:

Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
Example 2:

Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
Example 3:

Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6
'''

# Spare Vector is a vector that has mostly zero values, while a dense vector is a vector where most of the elements are non-zero. It's ineifficient to store a sparese vector as a one-dimentioanl array. Instead, we can store the non-zero values and their corresponding indices in a dictionary, with the index being the key.

# 1. Non-efficient array approach
# class SparseVector:
#     def __init__(self, nums):
#         self.array = nums


#     # Return the dotProduct of two sparse vectors
#     def dotProduct(self, vec):
#         total = 0
#         for n1, n2 in zip(self.array, vec.array):
#             total += n1 * n2
#         return total


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)


# 2. Hash Set
class SparseVector:
    def __init__(self, nums):
        self.nonzeros = {}
        for i, value in enumerate(nums):
            if value != 0:
                self.nonzeros[i] = value

    # Return the dotProduct of two sparse vectors

    def dotProduct(self, vec):
        total = 0
        for i, value in self.nonzeros.items():
            if i in vec.nonzeros:
                total += value * vec.nonzeros[i]

        return total
