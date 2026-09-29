# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        """
        Merge k sorted linked lists into one sorted linked list using a min-heap.

        Approach:
        1. Initialize a min-heap with the head of each non-empty linked list.
        2. Repeatedly extract the smallest node from the heap.
        3. Append it to the result list and push its next node (if exists) into the heap.
        4. Continue until the heap is empty.

        We need a tie-breaker in the heap since ListNode objects are not directly
        comparable. We use a tuple (value, index, node) where index is a unique
        counter to avoid comparing ListNode objects directly.
        """
        if not lists:
            return None

        # Min-heap: (node_value, tie_breaker_counter, node)
        heap = []
        counter = 0
        for node in lists:
            if node is not None:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1

        if not heap:
            return None

        # Dummy node to simplify list construction
        dummy = ListNode(0)
        current = dummy

        while heap:
            val, _, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next is not None:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1

        return dummy.next