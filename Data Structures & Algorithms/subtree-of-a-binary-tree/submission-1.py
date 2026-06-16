# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSubtreeHelper(node):
            stack = [(node, subRoot)]
            while stack:
                left, right = stack.pop()

                if not left and not right:
                    continue
                
                if not left or not right or left.val != right.val:
                    return False
                
                stack.append((left.left, right.left))
                stack.append((left.right, right.right))
                
            return True

        stack = [root] 
        while stack:
            node = stack.pop()

            if node.val == subRoot.val and isSubtreeHelper(node):
                return True
            
            if node and node.left:
                stack.append(node.left)
            if node and node.right:
                stack.append(node.right)
        
        return False