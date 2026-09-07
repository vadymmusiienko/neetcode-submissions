import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        discard = {}

        for i in range(k):
            heapq.heappush(heap, -nums[i])

        res = [-heap[0]]

        for right in range(k, len(nums)):
            left = right - k

            # Mark outgoing value for deletion
            discard[nums[left]] = discard.get(nums[left], 0) + 1

            # Add incoming value
            heapq.heappush(heap, -nums[right])

            # Remove stale values from top
            while heap and -heap[0] in discard:
                val = -heap[0]
                heapq.heappop(heap)

                discard[val] -= 1
                if discard[val] == 0:
                    del discard[val]

            res.append(-heap[0])

        return res