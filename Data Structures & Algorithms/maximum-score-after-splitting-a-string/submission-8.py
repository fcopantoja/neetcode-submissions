class Solution:
    def maxScore(self, s: str) -> int:
        left = [0] * len(s)
        right = [0] * len(s)

        if s[0] == "0":
            left[0] = 1
        
        for i in range(1, len(s)):
            left[i] = left[i - 1] + (1 if s[i] == "0" else 0)
        
        if s[-1] == "1":
            right[-1] = 1

        for i in range(len(s) - 2, -1, -1):
            right[i] = right[i + 1] + (1 if s[i] == "1" else 0)
        
        res = 0

        for i in range(1, len(s)):
            res = max(res, left[i - 1] + right[i])
        
        return res



            
