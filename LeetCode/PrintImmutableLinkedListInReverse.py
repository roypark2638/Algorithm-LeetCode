'''
1265. Print Immutable Linked List in Reverse

You are given an immutable linked list, print out all values of each node in reverse with the help of the following interface:

ImmutableListNode: An interface of immutable linked list, you are given the head of the list.
You need to use the following functions to access the linked list (you can't access the ImmutableListNode directly):

ImmutableListNode.printValue(): Print value of the current node.
ImmutableListNode.getNext(): Return the next node.
The input is only given to initialize the linked list internally. You must solve this problem without modifying the linked list. In other words, you must operate the linked list using only the mentioned APIs.


Example 1:

Input: head = [1,2,3,4]
Output: [4,3,2,1]
'''

# Recursion
# Time O(n) Space O(n)


def foo1(head):
    if head:
        foo1(head.getNext())
        head.printValue()


# Divide and Conquer
# Time O(nlogn) Space O(logn)
def foo2(head):
    def getSize(head):
        size = 0
        temp = head
        while temp != None:
            size += 1
            temp = temp.getNext()
        return size

    def helper(head, n):
        if n > 1:
            half = head
            for _ in range(n//2):
                half = half.getNext()
            helper(half, n-n//2)
            helper(head, n//2)
        elif n != 0:
            head.printValue()

    size = getSize(head)
    helper(head, size)


# Print from the back two pointers
# Time O(n^2) Space O(1)
def foo3(head):
    lastPrint = None
    while head != lastPrint:
        curr = head
        while curr.getNext() != lastPrint:
            curr = curr.getNext()

        curr.printValue()
        lastPrint = curr
