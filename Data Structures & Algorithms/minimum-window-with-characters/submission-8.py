class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counterT = defaultdict(int)
        counterS = defaultdict(int)
        
        for ch in t:
            counterT[ch] += 1
        
        l, r = 0, 0
        min_length = float("inf")
        min_seq = ""

        while r < len(s):
            counterS[s[r]] += 1
            while self.is_valid(counterS, counterT):
                if (r - l + 1) < min_length:
                    min_length = (r - l + 1)
                    min_seq = s[l: r + 1]

                counterS[s[l]] -= 1
                l += 1
            r += 1

        return min_seq
        
    def is_valid(self, counterS, counterT):
        for k, v in counterT.items():
            if not(k in counterS and counterS[k] >= v):
                return False

        return True