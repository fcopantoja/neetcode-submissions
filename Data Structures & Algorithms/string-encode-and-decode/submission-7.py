class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += f"{len(word)}#{word}"
        
        return res
       

    def decode(self, s: str) -> List[str]:
        result = []
        print(s)
        i = 0
    
        while i < len(s):
            length = ""
            while s[i].isdigit():
                length += s[i]
                i += 1
            
            i += 1
            word = ""

            for idx in range(i, i + int(length)):
                word += s[idx]
            
            result.append(word)
            i = i + int(length)
        
        return result

            
        

      
