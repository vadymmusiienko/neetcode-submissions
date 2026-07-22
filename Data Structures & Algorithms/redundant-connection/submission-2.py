class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = [[] for _ in range(n + 1)]
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        seen = [0] * (n + 1)
        cycle = set()
        cycleStart = -1
        def dfs(node, par):
            nonlocal cycleStart

            if seen[node]:
                cycleStart = node
                return True
            
            seen[node] = True
            for nei in graph[node]:
                if nei == par:
                    continue
                
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False

        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
            
        return []