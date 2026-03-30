class Solution:
    def is_palindrome(self, s):
        return s == s[::-1]


    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            for j in range(i + 1, n + 1):
                print(s[i:j])
                if self.is_palindrome(s[i:j]):
                    res += 1

        return res
