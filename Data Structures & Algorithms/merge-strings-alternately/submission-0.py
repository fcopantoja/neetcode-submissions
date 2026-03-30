class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i = 0

        while i < len(word1) and i < len(word2):
            res += word1[i]
            res += word2[i]                
            
            i += 1
        
        if len(word1) >= i:
            res += word1[i:]
        
        if len(word2) >= i:
            res += word2[i:]
        
        return res


            

