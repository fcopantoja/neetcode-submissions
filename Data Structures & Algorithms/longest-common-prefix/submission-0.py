class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min([len(s) for s in strs])
        prefix = ""

        for i in range(min_length):
            ch = strs[0][i]
            for s in strs:
                if s[i] != ch:
                    return prefix
            
            prefix += ch
        
        return prefix


