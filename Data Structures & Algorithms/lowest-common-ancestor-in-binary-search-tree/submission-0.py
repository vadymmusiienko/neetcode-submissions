# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while True:
            root_v = root.val
            p_v = p.val
            q_v = q.val

            if (p_v <= root_v and root_v <= q_v) or (q_v <= root_v and root_v <= p_v):
                return root
            
            if p_v <= root_v and q_v <= root_v:
                root = root.left
            
            if p_v >= root_v and q_v >= root_v:
                root = root.right
        
        