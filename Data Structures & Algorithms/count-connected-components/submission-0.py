class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create graph
        graph = {i: [] for i in range(n)}
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)
            # Visit neigbs
            for nei in graph[node]:
                dfs(nei)


        connected = 0
        seen = set()
        for node in range(n):
            if node in seen:
                continue
            
            dfs(node)
            connected += 1
    
        return connected