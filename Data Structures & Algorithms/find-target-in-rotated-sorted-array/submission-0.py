class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Search for pivot
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + ((right - left) // 2)

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        min_idx = left
        n = len(nums)
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2) # Imaginary idx
            real_mid = (mid + min_idx) % n

            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return -1