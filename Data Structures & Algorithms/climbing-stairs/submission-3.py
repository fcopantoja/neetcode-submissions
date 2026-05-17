class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 2] + dp[i - 1] 
        return dp[n - 1]
    
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        
        a = 1
        b = 1

        for i in range(2, n + 1):
            a, b = b, a + b
        print(a, b)
        return b
