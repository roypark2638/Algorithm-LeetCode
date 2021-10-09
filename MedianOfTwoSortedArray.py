'''
4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
'''
nums1 = [1, 2]
nums2 = [3, 4]

# Time O(log(min(n,m)))
# Space O(1)


def findMedianSortedArrays(nums1, nums2):
    # if num1 length is greater than, switch them so that length of nums1 is smaller than nums2.
    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2, nums1)

    x = len(nums1)
    y = len(nums2)

    low = 0
    high = x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        # if partitionX is 0 it means nothing is there on left side. Use -inf for maxLeftX
        # if partitionX is length of input then there is nothing on right side. Use +inf for minRightX
        maxLeftX = float(
            "-inf") if partitionX == 0 else nums1[partitionX-1]
        minRightX = float("inf") if partitionX == x else nums1[partitionX]

        maxLeftY = float(
            "-inf") if partitionY == 0 else nums2[partitionY-1]
        minRightY = float("inf") if partitionY == y else nums2[partitionY]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            # We have partitioned array at correct place
            # Now get max of left elements and min of right elements
            # to get the median in case of even length cominbed array size
            # or get max of left for odd length combined array size.
            if (x+y) % 2 == 0:
                return float(max(maxLeftX, maxLeftY) + min(minRightY, minRightX)) / 2
            else:
                return max(maxLeftX, maxLeftY)
        # we are too far on right side for partitionX. Go on left side.
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:  # We are too far on left side for partitionX. Go on right side.
            low = partitionX + 1


print(findMedianSortedArrays(nums1, nums2))
# Time O(n+m) Space O(n+m)
#     def findMedianSortedArrays(self, nums1, nums2):
#         merged = []
#         self.mergeSortedArray(nums1, nums2, merged)
#         n = len(merged)
#         if len(merged) % 2 == 1:
#             return float(merged[n // 2])
#         else:
#             mid = (n-1) // 2
#             return (float(merged[mid]) + float(merged[mid+1])) / 2

#     def mergeSortedArray(self, nums1, nums2, merged):
#         i = 0
#         j = 0
#         while i < len(nums1) and j < len(nums2):
#             if nums1[i] < nums2[j]:
#                 merged.append(nums1[i])
#                 i +=1
#             else:
#                 merged.append(nums2[j])
#                 j += 1
#         while i < len(nums1):
#             merged.append(nums1[i])
#             i += 1
#         while j < len(nums2):
#             merged.append(nums2[j])
#             j += 1
