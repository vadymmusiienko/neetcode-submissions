class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break

            mid = left + ((right - left) // 2)

            result = min(nums[mid], result)

            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1


        return result

        