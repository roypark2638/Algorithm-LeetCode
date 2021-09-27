'''
Remove Kth Node From End

Write a function that takes in the head of a Singly Linked List and an integer k and removes the kth node from the end of the list.

The removal should be done in place, meaning that the original data structure should be mutated (no new structure should be created).

Furthermore, the input head of the linked list should remain the head of the linked list after the removal is done, even if the head is the node that's supposed to be removed. In other words, if the head is the node that's supposed to be removed, your function should simply mutate its value and next pointer.

Note that your function doesn't need to return anything.

You can assume that the input Linked List will always have at least two nodes and, more specifically, at least k nodes.

Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None if it's the tail of the list.

Sample Input
head = 0->1->2->3->4->5->6->7->8->9
k = 4

Sample Output
head = 0->1->2->3->4->5->7->8->9
'''

# Create 2 pointers, first and second.
# Move second pointer to kth times
# And move both of pointers until second is None
# Now remove the node where first pointer is pointing to
# Time O(n) Space O(1)


def removeKthNodeFromEnd(head, k):
    first = head
    second = head
    for _ in range(k):
        second = second.next

    prev = None
    while second != None:
        prev = first
        first = second
        second = second.next

    if prev == None:
        head.value = head.next.value
        head.next = head.next.next
    else:
        prev.next = first.next
        first.next = None
