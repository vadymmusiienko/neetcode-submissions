class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n and nums[i] < 0:
            i += 1
        
        left = i - 1
        right = i
        res = []
        while left >= 0 or right < n:

            if left < 0:
                res.append(nums[right]**2)
                right += 1
            elif right >= n:
                res.append(nums[left]**2)
                left -= 1
            else:
                
                if -nums[left] < nums[right]:
                    res.append(nums[left]**2)
                    left -= 1
                else:
                    res.append(nums[right]**2)
                    right += 1
        
        return res

