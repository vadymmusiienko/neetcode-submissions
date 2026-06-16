# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # node -> height, isBalanced
        mp = {None: 0}
        stack = [root]
        while stack:
            node = stack[-1]

            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                leftH = mp[node.left]
                rightH = mp[node.right]
                
                if abs(leftH - rightH) > 1:
                    return False

                mp[node] = 1 + max(leftH, rightH)
        
        return True
            
            
            

