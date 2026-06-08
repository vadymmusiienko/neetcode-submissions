class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        profit = 0
        buy = prices[0]
        
        for sell in prices:
            profit = max(profit, sell - buy)
            buy = min(buy, sell)
        
        return profit

        