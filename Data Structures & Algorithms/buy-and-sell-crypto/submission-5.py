class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = float("-inf")

        while r <= len(prices) - 1:
            if prices[r] > prices[l]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r
                
            r += 1
        
        return max_profit if max_profit != float("-inf") else 0


