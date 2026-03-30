class Solution:
    def isPrefixAndSuffix(self, s, t):
        return t.startswith(s) and t.endswith(s)

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    res += 1
        
        return res