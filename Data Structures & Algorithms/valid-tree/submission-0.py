class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # No cycles and fully connected (n-1 edges)
        if len(edges) != n - 1:
            return False
        
        graph = {i : [] for i in range(n)} # Node: [neibs]
        visited = set()
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        
        dfs(0)
        return len(visited) == n
