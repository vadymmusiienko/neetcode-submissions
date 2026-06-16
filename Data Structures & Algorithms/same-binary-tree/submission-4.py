# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            left, right = stack.pop()

            if not left and not right:
                continue
            
            if not left or not right or left.val != right.val:
                return False
            
            stack.append((left.left, right.left))
            stack.append((left.right, right.right))
        
        return True
        