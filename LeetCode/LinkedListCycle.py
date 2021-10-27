'''
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    '''
    Iterative Floyd's algorithm: Time O(n) Space O(1)
    Create slwo and fast pointers, where slow pointer increment the position by 1 and fast pointer increment the position by 2. If both pointers are not null and pointing to the same node, then we know that we found a cycle by the floyd's algorithm.
    '''

    def hasCycle(self, head):
        if not head:
            return False
        fast = head.next
        slow = head
        while fast != slow:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

    '''
    Recurisve Floyd's algorithm: Time O(n) Space O(n)
    '''
    # def hasCycle(self, head):
    #     def cycle(slow, fast):
    #         if not slow or not fast:
    #             return False
    #         fast = fast.next
    #         if not fast:
    #             return False
    #         if slow == fast:
    #             return True
    #         return cycle(slow.next, fast.next)
    #     return cycle(head, head)

    '''
    Hashmap: Time O(n) Space O(n)
    Traverse the linked list and append each node into the hashmap. During the traversal, if we find a same node by checking the hashmap, then we found a cycle. 
    '''

    def hasCycle(self, head):
        if not head:
            return False
        hashmap = {}
        temp = head
        while temp != None:
            if temp in hashmap:
                return True
            hashmap[temp] = True
            temp = temp.next
        return False
