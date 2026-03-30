class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += f"{len(word)}#{word}"
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        n = len(s)
        result = []

        while i < n:
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            
            i += 1 # Skip #
            length = int(length)
            result.append(s[i:i + length])
            i += length
        
        return result
