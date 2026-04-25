class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(len(s) - 1):
            s1 = s[:i + 1]
            s2 = s[i+1:]

            res = max(res, s1.count("0") + s2.count("1"))
        
        return res
            
