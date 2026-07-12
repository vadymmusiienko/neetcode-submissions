# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not lists[0]:
            return None

        # heap with (node value, node idx)
        heap = [(lists[i].val, i) for i in range(len(lists))]
        heapq.heapify(heap)

        dummy = curr = ListNode()
        while heap:
            val, idx = heapq.heappop(heap)
            next_node = lists[idx].next
            lists[idx] = next_node
            if next_node:
                heapq.heappush(heap, (next_node.val, idx))

            new_node = ListNode(val=val)
            curr.next = new_node
            curr = new_node

        return dummy.next
        