class Solution:
    def reverse_string(self, s: str) -> str:
        return s[::-1] 

    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            for j in range(1, len(s) + 1):
                word = s[i:j]
                if word == self.reverse_string(word):
                    if len(word) > len(longest):
                        longest = word
        
        return longest