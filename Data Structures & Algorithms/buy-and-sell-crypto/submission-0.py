class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        profit = 0
        buy = prices[0]
        for sell_idx in range(len(prices)):
            sell = prices[sell_idx]
            
            if sell > buy:
                profit = max(profit, sell - buy)
            
            buy = min(buy, sell)
        
        return profit

        