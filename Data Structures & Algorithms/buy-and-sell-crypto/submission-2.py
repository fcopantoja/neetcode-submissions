class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        n = len(prices)
        max_profit = 0
        
        while right <= n - 1:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)

            if  prices[right] < prices[left]:
                left += 1
            else:
                right += 1
        return max_profit

