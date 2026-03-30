class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        
        stack = []
        mapping = {"}":"{", ")":"(", "]":"["}


        for char in s:
            if char not in mapping:
                stack.append(char)
            else:
                if not stack:
                    return False
                elif mapping[char] != stack[-1]:
                    return False
                else:
                    stack.pop()
        
        return True if not stack else False
        