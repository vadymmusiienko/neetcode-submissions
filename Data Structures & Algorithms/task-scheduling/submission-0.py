import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = {}
        for task in tasks:
            freqs[task] = freqs.get(task, 0) - 1
        
        # Tasks
        heap = [freq for freq in freqs.values()]
        heapq.heapify(heap)

        # Cooldown
        queue = deque() # (time ready, num of tasks)
        time = 0

        while heap or queue:

            if heap:
                task = heapq.heappop(heap) + 1
                if task < 0:
                    queue.append((time + n, task))
            
            if queue and queue[0][0] <= time:
                _, ready = queue.popleft()
                heapq.heappush(heap, ready)
            
            time += 1
        
        return time

        
