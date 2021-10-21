'''
24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

'''


class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


# Iterative Time O(n) Space O(1)
# Iterate linked list with jumps in steps of two
# Swap the pair of nodes as we go, before we jump to the next pair. Let's represent the two nodes to be swapped by firstNode and secondNode.
# Swap the two nodes.
# Assign the prevNode's next to the head of the swapped pair.
def swapPairs1(head):
    dummy = ListNode(-1)
    dummy.next = head
    prevNode = dummy

    while head and head.next:
        firstNode = head
        secondNode = head.next

        prevNode.next = secondNode
        firstNode.next = secondNode.next
        secondNode.next = firstNode

        prevNode = firstNode
        head = firstNode.next

    return dummy.next

# Recursive solution Time O(n) Space O(n)
# Start the recursion with head node of the original linked list.
# Every recursion call is responsibile for swapping a pair of nodes. Let's represent the two nodes to be swapped by firstNode and secondNode.
# Next recursion is made by calling the function with head of the next pair of nodes. This call would swap the next two nodes and make further recursive calls if there are nodes left in the linked list.
# Once we get the pointer to the remaining swapped list from the recursion call, we can swap the firstNode and secondNode i.e. the nodes in the current recursive call and then return the pointer to the secondNode since it will be the next head after swapping.


def swapPairs2(head):
    if head is None or head.next is None:
        return

    firstNode = head
    secondNode = head.next

    firstNode.next = swapPairs2(head.next.next)
    secondNode.next = firstNode
    return secondNode
