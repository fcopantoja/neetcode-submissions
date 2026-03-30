class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapPW, mapWP = {}, {}
        words = s.split()

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            p = pattern[i]
            word = words[i]
            
            if(
                (p in mapPW and mapPW[p] != word) or
                (word in mapWP and mapWP[word] != p)
            ):
                return False


            mapPW[p] = word
            mapWP[word] = p
        
        return True
