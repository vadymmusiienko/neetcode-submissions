import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = list(map(lambda x: -x, stones))
        heapq.heapify(heap)
        
        while len(heap) > 1:
            y = -heapq.heappop(heap) # heaviest
            x = -heapq.heappop(heap)

            if x < y:
                heapq.heappush(heap, x - y) # -(y-x) = (x-y)
            print(heap)
        
        return -heap[0] if heap else 0
