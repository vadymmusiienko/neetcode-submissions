# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        left, right = l1, l2

        dummy = curr = ListNode()
        carry = 0
        while left or right:
            # If one list is shorter, treat the other one as zeros
            if not left:
                left_val = 0
            else:
                left_val = left.val
            if not right:
                right_val = 0
            else:
                right_val = right.val
            
            curr_sum = left_val + right_val + carry
            carry = 0 if curr_sum < 10 else 1
            curr_val = curr_sum % 10

            curr.next = ListNode(curr_val, None)
            curr = curr.next

            left = left.next if left else None
            right = right.next if right else None
        
        # Need more nodes
        if carry:
            curr.next = ListNode(1, None)
        
        return dummy.next


        