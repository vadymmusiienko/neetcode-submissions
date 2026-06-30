class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cur, prev = 0, 0 
        for i in range(len(cost)):
            tmp = cur
            cur = min(cur + cost[i], prev + cost[i])
            prev = tmp
        
        return min(cur, prev)