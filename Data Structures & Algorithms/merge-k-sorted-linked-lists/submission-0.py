# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Put the first node of every non-empty list into the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while heap:
            # Get smallest node
            val, i, node = heapq.heappop(heap)

            # Add it to result
            current.next = node
            current = current.next

            # Put next node from the same list into heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next