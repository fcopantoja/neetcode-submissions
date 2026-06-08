class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        curr_sum = sum(cardPoints[n - k:])
        res = curr_sum
        print(curr_sum)

        l, r = 1, n - k

        while r < len(cardPoints):
            curr_sum += cardPoints[l - 1] - cardPoints[r]
            res = max(res, curr_sum)
            r += 1
            l += 1
        
        return res



