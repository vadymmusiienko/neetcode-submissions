# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = root.val

        def dfs(node):
            if not node:
                return 0

            nonlocal maxSum

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Try splitting here
            maxSum = max(maxSum, node.val + left + right)
            better = node.val + max(left, right)
            # maxSum = max(maxSum, better)

            # Choose either left or right
            return better

        

        dfs(root)
        return maxSum
