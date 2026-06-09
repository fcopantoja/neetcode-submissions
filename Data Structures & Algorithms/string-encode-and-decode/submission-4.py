class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += f"{len(word)}#{word}"
        
        print(res)
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
            result.append(s[i:int(length) + i])
            i += int(length)
        
        return result
        

      
