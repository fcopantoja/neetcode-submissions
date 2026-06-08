class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        curr_sum = sum(cardPoints[n - k:])
        res = curr_sum
        l, r = 0, n - k
        
        while r < len(cardPoints):
            curr_sum += (cardPoints[l] - cardPoints[r])
            res = max(res, curr_sum)
            r += 1
            l += 1
        
        return res

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        curr_sum = 0
        l, r = 0, 0
        window_size = n - k
        res = float("-inf")
        
        while r < len(cardPoints):
            curr_sum += cardPoints[r]
            window_length = (r - l + 1)
            
            if (r - l + 1) > window_size:
                curr_sum -= cardPoints[l]
                l += 1
            
            if (r - l + 1) == window_size:
                res = max(res, total - curr_sum)
        
            r += 1

        
        return res



