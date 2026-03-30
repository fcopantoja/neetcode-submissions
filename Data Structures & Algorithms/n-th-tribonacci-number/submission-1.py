class Solution:
    def tribonacciDP(self, n: int) -> int:
        fib = [0, 1, 1, 2]

        if n <= 2:
            return fib[n]

        for i in range(3, n + 1):
            fib.append(fib[i - 3] + fib[i - 2] + fib[i - 1])
        
        return fib[n]

    
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1

        if n == 0:
            return a

        if n == 1:
            return b

        if n == 2:
            return c

        for i in range(3, n + 1):
            a, b, c = b, c, a + b + c
        
        return c