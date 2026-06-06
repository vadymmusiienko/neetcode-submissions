class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return -1

        left = 1
        right = k = max(piles)

        while left <= right:
            mid = left + ((right - left) // 2)

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            
            if hours <= h:
                k = mid
                right = mid - 1
            else:
                left = mid + 1

        return k