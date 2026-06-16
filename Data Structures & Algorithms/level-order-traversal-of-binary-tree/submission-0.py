from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        res = []
        while queue:
            level = []
            outstanding = deque()
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node and node.left:
                    outstanding.append(node.left)
                if node and node.right:
                    outstanding.append(node.right)

            res.append(level)
            queue = outstanding
        
        return res
