
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        
        for src, dst in prerequisites:
            indegree[dst] += 1
            graph[src].append(dst)

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        taken, result = 0, []
        while queue:
            course = queue.popleft()
            result.append(course)
            taken += 1
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        if taken != numCourses:
            return []
        
        return result[::-1]
