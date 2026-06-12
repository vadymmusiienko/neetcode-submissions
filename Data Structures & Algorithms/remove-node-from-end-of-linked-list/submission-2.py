# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        if not head.next:
            return None

        # Find len of the list
        length = 0
        prev, curr = None, head
        while curr:
            length += 1
            prev = curr
            curr = curr.next
        
        # Node from the start (0-indexed)
        idx = length - n

        if idx < 0:
            return None
        if idx == 0:
            res = head.next
            head.next = None
            return res
        
        remove = head
        prev = None
        for _ in range(idx):
            prev = remove
            remove = remove.next
        
        prev.next = remove.next
        remove.next = None

        return head


        

        
        