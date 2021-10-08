'''
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    # Recursive Time O(n) Space O(n)
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    # Recursive Time O(n) Space O(n)
    # def mergeTwoLists(self, l1, l2):
    #     def mergeHelper(l1, l2, pre):
    #         if l1 is None or l2 is None:
    #             pre.next = l1 if l1 is not None else l2
    #             return
    #         if l1.val < l2.val:
    #             pre.next = l1
    #             mergeHelper(l1.next, l2, pre.next)
    #         else:
    #             pre.next = l2
    #             mergeHelper(l1, l2.next, pre.next)
    #     dummy = ListNode()
    #     mergeHelper(l1, l2, dummy)
    #     return dummy.next

# Iterative Time O(n) Space O(1)
#     def mergeTwoLists(self, l1, l2):
#         dummyNode = ListNode()
#         mergedList = dummyNode
#         while l1 != None and l2 != None:
#             if l1.val < l2.val:
#                 mergedList.next = ListNode(l1.val)
#                 l1 = l1.next
#             else:
#                 mergedList.next = ListNode(l2.val)
#                 l2 = l2.next
#             mergedList = mergedList.next

#         mergedList.next = l1 if l1 is not None else l2

#         return dummyNode.next
