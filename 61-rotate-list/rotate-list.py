# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head

        # First, find the length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Make the list circular
        tail.next = head

        # Find the new tail: (length - k % length - 1)th node
        k = k % length
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        # New head is next of new tail
        new_head = new_tail.next
        new_tail.next = None  # Break the circle

        return new_head
