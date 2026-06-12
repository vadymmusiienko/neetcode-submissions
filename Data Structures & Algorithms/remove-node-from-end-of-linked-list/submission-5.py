# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(0, head) # Points at head
        slow = dummy
        fast = head

        # Move fast to n-th node
        for _ in range(n):
            fast = fast.next
        
        # Move together until end
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Slow.next is the node we want to remove
        slow.next = slow.next.next

        return dummy.next
        