import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            y = heapq.heappop(heap) # heaviest
            x = heapq.heappop(heap)

            # (-x) < (-y) == x > y
            if x > y:
                heapq.heappush(heap, y - x)
        
        return -heap[0] if heap else 0
