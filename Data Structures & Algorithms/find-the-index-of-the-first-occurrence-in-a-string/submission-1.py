class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = len(needle)

        for i in range(len(haystack) - k + 1):
            if haystack[i: i + k] == needle:
                return i
        
        return -1