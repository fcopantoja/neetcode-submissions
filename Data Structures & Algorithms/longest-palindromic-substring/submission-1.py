class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        n = len(s)

        for i in range(n):
            # Odd length
            l = i
            r = i
            while l >= 0 and r < n and s[l] == s[r]:
                word = s[l: r + 1]
                if len(word) > len(longest):
                    longest = word
                l -= 1
                r += 1


            # Even length
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                word = s[l: r + 1]
                if len(word) > len(longest):
                    longest = word

                l -= 1
                r += 1
        

        
        return longest