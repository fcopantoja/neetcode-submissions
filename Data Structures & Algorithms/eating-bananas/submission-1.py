import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = float("inf")

        while left <= right:
            k = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
                        
            if hours <= h:
                right = k - 1
                res = min(res, k)
            
            else:
                left = k + 1
        
        return res