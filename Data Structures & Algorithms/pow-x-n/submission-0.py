class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        for i in range(abs(n)):
            result *= x
        print(result)
        return result if n > 0 else 1 / result