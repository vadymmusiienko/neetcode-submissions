# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left, right = l1, l2

        dummy = curr = ListNode()
        carry = 0
        while left or right or carry:
            # If one list is shorter, treat the other one as zeros
            left_val = left.val if left else 0
            right_val = right.val if right else 0
            
            curr_sum = left_val + right_val + carry
            carry = curr_sum // 10
            curr_val = curr_sum % 10
            curr.next = ListNode(curr_val, None)

            curr = curr.next
            left = left.next if left else None
            right = right.next if right else None
        
        return dummy.next


        