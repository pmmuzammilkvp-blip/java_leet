class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [0] * n
        
        # Starting point
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0
        
        for i in range(m):
            for j in range(n):
                
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0  # obstacle → no path
                
                elif j > 0:
                    dp[j] += dp[j-1]
        
        return dp[-1]
