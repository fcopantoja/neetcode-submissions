class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = defaultdict(int)
        res = 0
        for ch in s:
            counts[ch] += 1
            if counts[ch] % 2 == 0:
                res += 2
        
        for ch in s:
            if counts[ch] % 2 == 1:
                res += 1
                break
        
        return res