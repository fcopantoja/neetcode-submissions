class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        sett = set()

        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[left])
                left += 1
            longest = max(longest, (r - left) + 1)
            sett.add(s[r])
        
        return longest
