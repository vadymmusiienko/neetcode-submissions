class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        n = len(intervals)

        left = 0
        while left < n:
            start = intervals[left][0]
            end = intervals[left][1]

            # Merge
            right = left + 1
            while right < n and intervals[right][0] <= end:
                end = max(end, intervals[right][1])
                right += 1
            
            res.append([start, end])
            left = right
        
        return res
