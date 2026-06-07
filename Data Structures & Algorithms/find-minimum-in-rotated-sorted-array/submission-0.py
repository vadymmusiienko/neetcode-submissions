class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = nums[0]

        while left <= right:
            mid = left + ((right - left) // 2)
            result = min(nums[left], nums[right], nums[mid], result)

            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1


        return result

        