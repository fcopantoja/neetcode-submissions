class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        res = 0
        freq = [0] * 26
        maxf = defaultdict(int)

        while r < len(s):
            maxf[s[r]] += 1

            while (r - l + 1) - max(maxf.values()) > k:
                maxf[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))
            r += 1

        return res


