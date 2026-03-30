class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        n = len(prices)
        max_profit = 0
        
        while right < n:
            if  prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1
        return max_profit

