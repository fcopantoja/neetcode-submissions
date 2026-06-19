class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        res = float("-inf")

        while r < len(prices):
            if prices[r] > prices[l]:
                res = max(res, prices[r] - prices[l])
            elif prices[r] < prices[l]:
                l = r
            r += 1
        
        return res if res != float("-inf") else 0
