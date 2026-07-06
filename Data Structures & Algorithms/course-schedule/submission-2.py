class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {c : [] for c in range(numCourses)} # Node: [neighbs]
        for course, prer in prerequisites:
            graph[course].append(prer)
        
        reachable = set()
        def dfs(c, seen):
            nonlocal reachable
            if c in seen:
                return False
            
            seen.add(c)
            
            for nei in graph[c]:
                if nei in reachable:
                    continue
                if not dfs(nei, seen):
                    return False

            reachable |= seen
            return True

        for course in graph.keys():
            if course in reachable:
                continue
            if not dfs(course, set()):
                return False
        
        return True
        