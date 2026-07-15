# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        # NOTE: root is always to the 'left' of dummy
        # '#' means new level
        res = []
        stack = [root]
        while stack:
            node = stack.pop()

            if not node:
                res.append('N')
            else:
                res.append(str(node.val))
                stack.append(node.right)
                stack.append(node.left)

        print(res)
        return ",".join(res)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        vals = data.split(",")
        i = 0
        def dfs():
            nonlocal i
            if vals[i] == 'N':
                i += 1
                return None
            
            node = TreeNode(int(vals[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()

            return node

        
        return dfs()
