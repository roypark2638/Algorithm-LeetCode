'''
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''


class Solution(object):
    '''
    return the k most frequent elements.
    [1,1,1,3,3,5,5,5,5], k = 2
    [1,5]
    [1,1,1,3,3,5,5,5,5], k = 3
    [1,3,5]
    [1,1,1,3,3,5,5,5,5], k = 4
    - Can I assume the input valid, for example, k is less than equal to the number of unique elements in the nums array?
    - Will ever k would equal to 0?
    [1,1,1,3,3,5,5,5,5], k = 0
    - What it be multiple answers? for example, and the answer is no. It's guaranteed that the answer is unique
    '''

    '''
    Heap(Priority Queue) and hashmap: Time O(nlogn) Space O(n)
    
    We want to create a frequency table of each number into hashmap. The key value is unique and store the key into an array, uniqueNums and use this array to create and populate a 2D array holding tuple of (uniqueNumCount, key). Now, call heapify function on this newly created 2D tuple array. This computation will give us the minimum count at the first array position. Now, pop out the n-k number of elements from the heap, which we are removing the smallest count. And we return the leftover unique number in the heap as an array.
    '''
#     def topKFrequent(self, nums, k):
#         d = {}
#         for num in nums:
#             d[num] = d.get(num, 0) + 1
#         uniqueNums = d.keys()
#         pq = []
#         for num in uniqueNums:
#             uniqueNumCount = d[num]
#             pq.append((uniqueNumCount, num))
#         heapq.heapify(pq)

#         res = []
#         # res = heapq.nlargest(k, pq)
#         for i in range(len(d) - k):
#             heapq.heappop(pq)
#         return [b for a, b in pq]
    '''
    Same as above approach but slightly better performance: Time O(nlogk) Space O(n)
    '''
#     def topKFrequent(self, nums, k):
#         count = {}
#         for num in nums:
#             count[num] = count.get(num, 0) + 1

#         res = heapq.nlargest(k, count.keys(), key=count.get)
#         return res

    '''
    Bucket Sort: Tiem O(n) Space O(n)
    
    Since the maximum number of the nums is unbounded, we want to make the bucket index with the count and values as an array. For example, 
    i(count) [0,1,2,3,4,5,6]
    value    [-,[1],[2],[3],-,-]
    Now, we want to find k number of the most frequenct elements. Iterate the array from the bucket from the behind since the highest frequent elements located at the last, and append the elements to the final result array. Once the length of the result array is equal to the k, then return the result array.
    '''

    def topKFrequent(self, nums, k):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        bucket = [[] for _ in range(len(nums)+1)]
        for num, count in dic.items():
            bucket[count].append(num)
        res = []

        for arr in bucket[::-1]:
            for n in arr:
                res.append(n)
                if len(res) == k:
                    return res
