import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_heap = []

        for idx, (x, y) in enumerate(points):
            # Calculate distance
            dist = x*x + y*y
            heapq.heappush(dist_heap, (dist, idx))
        
        res = []
        for _ in range(k):
            dist, idx = heapq.heappop(dist_heap)
            res.append(points[idx])
        
        return res

        