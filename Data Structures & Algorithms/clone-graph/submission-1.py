"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # Empty graph
        if not node:
            return None

        # Recursion
        def cloneHelper(cur_node, new_node, node_map):
            if cur_node in node_map:
                return

            node_map[cur_node] = new_node
            new_node.val = cur_node.val

            # Clone neighbors
            for nei in cur_node.neighbors:

                # Clone the rest
                if nei not in node_map:
                    new_nei = Node()
                    cloneHelper(nei, new_nei, node_map)

                new_node.neighbors.append(node_map[nei])


        
        new_graph = Node()
        cloneHelper(node, new_graph, {})

        return new_graph