class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0
        left, right = 0, len(height) - 1

        heighest = 0 # Add after we moved on
        while left < right:
            # Check if can trap water
            trapped_water += max(0, heighest - height[left], heighest - height[right])

            # Move a pointer
            if height[left] < height[right]:
                heighest = max(heighest, height[left])
                left += 1
            else:
                heighest = max(heighest, height[right])
                right -= 1
        
        return trapped_water