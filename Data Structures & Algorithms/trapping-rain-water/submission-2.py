class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0
        left, right = 0, len(height) - 1

        max_left, max_right = 0, 0
        while left < right:

            # Move shorter side
            if height[left] < height[right]:
                trapped_water += max(0, max_left - height[left])
                max_left = max(max_left, height[left])
                left += 1
            else:
                trapped_water += max(0, max_right - height[right])
                max_right = max(max_right, height[right])
                right -= 1
        
        return trapped_water