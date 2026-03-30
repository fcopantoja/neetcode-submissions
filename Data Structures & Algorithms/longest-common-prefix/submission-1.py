class Solution:
    def longestCommonPrefixVertical(self, strs: List[str]) -> str:
        min_length = min([len(s) for s in strs])
        prefix = ""

        for i in range(min_length):
            ch = strs[0][i]
            for s in strs:
                if s[i] != ch:
                    return prefix
            
            prefix += ch
        
        return prefix


    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
        
        return prefix


