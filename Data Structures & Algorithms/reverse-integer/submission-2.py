
class Solution:
    def reverse(self, x: int) -> int:
        
        res = ""
        y = abs(x)
        while y:
            res += str(y % 10)
            y = y // 10
        if not res:
            return 0
        res = int(res) if x > 0 else -int(res)

        if res > (2 ** 31) or res < (-2 ** 31):
            return 0
        
        return res