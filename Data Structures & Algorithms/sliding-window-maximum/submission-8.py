import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))

        res = [-heap[0][0]]

        for right in range(k, len(nums)):
            left = right - k

            # Add incoming value
            heapq.heappush(heap, (-nums[right], right))

            # Remove stale values from top
            while heap and heap[0][1] <= left:
                heapq.heappop(heap)

            res.append(-heap[0][0])

        return res