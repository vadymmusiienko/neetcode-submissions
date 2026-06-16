# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        good_nodes = 0
        stack = [(root, float("-inf"))]
        while stack:
            node, cur_max = stack.pop()

            # Good node
            if node.val >= cur_max:
                good_nodes += 1
            
            # Update the stack
            if node.left:
                stack.append((node.left, max(cur_max, node.val)))
            if node.right:
                stack.append((node.right, max(cur_max, node.val)))
        
        return good_nodes

