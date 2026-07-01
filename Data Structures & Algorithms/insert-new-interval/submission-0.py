class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Binary search by the end of intervals
        new_start = newInterval[0]
        new_end = newInterval[1]
        left = 0
        right = len(intervals) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if intervals[mid][0] > new_start:
                right = mid - 1
            else:
                left = mid + 1
        
        # Left is the insert pos
        intervals.insert(left, newInterval)

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        
        return res
        


