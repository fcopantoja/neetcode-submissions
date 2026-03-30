class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]


        for i in range(n):
            if obstacleGrid[0][i] == 1:
                dp[0][i] = 0
                break
            else:    
                dp[0][i] = 1 
        
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                break
            else:    
                dp[i][0] = 1 

        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] == 0:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        
        return dp[m-1][n-1]