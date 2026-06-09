class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += f"{len(word)}#{word}"
        
        return res
       

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            length = ""
            while s[i].isdigit():
                length += s[i]
                i += 1
            
            i += 1
            word = ""
            for j in range(i, i + int(length)):
                word += s[j]
                i += 1
            print(word)
            result.append(word)
            #i += int(length)
        
        return result
        

      
