class Solution:
    def tribonacci(self, n: int) -> int:
        fib = [0, 1, 1]

        if n <= 2:
            return fib[n]

        for i in range(3, n + 1):
            fib.append(fib[i - 3] + fib[i - 2] + fib[i - 1])
        
        return fib[n]