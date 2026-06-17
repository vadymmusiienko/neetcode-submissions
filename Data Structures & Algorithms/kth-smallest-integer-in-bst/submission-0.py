# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return root
        
        seen = set([None])
        res = []
        stack = [root]
        while stack:
            node = stack[-1]
            seen.add(node)

            if not node:
                stack.pop()
                continue

            if node.left in seen:
                node = stack.pop()
                stack.append(node.right)
                res.append(node.val)
            else:
                stack.append(node.left)
        
        return res[k-1]