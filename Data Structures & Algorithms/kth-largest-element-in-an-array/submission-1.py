import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap = [-n for n in nums]
        # heapq.heapify(heap)
        # for _ in range(k-1):
        #     heapq.heappop(heap)
        
        # return -heapq.heappop(heap)
        heapq.heapify(nums)
        for _ in range(len(nums) - k ):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)
        