class Solution:
    def isPrefixAndSuffix(self, s, t):
        if len(t) < len(s):
            return False
        
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
            
            if s[-1 - i] != t[len(t) - 1 - i]:
                print(s, t)
                return False

        return True

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    res += 1
        
        return res