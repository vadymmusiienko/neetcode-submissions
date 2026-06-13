# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(curr_root):
            if not curr_root:
                return curr_root
            
            tmp = curr_root.left
            curr_root.left = curr_root.right
            curr_root.right = tmp

            self.invertTree(curr_root.left)
            self.invertTree(curr_root.right)
        
        invert(root)
        return root
        