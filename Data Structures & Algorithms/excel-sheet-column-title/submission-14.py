class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        
        while columnNumber:
            columnNumber -= 1
            val = columnNumber % 26
            res = chr(ord('A') + val) + res
            columnNumber = columnNumber // 26
        
        return res