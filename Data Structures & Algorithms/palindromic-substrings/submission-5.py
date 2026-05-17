class Solution:
    def countPalindromes(self, l, r, s):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            res += self.countPalindromes(i, i, s)
            res += self.countPalindromes(i, i + 1, s)

        return res
