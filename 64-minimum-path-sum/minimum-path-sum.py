class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        dp = [0] * n
        
        dp[0] = grid[0][0]
        
        # First row
        for j in range(1, n):
            dp[j] = dp[j-1] + grid[0][j]
        
        for i in range(1, m):
            dp[0] += grid[i][0]  # first column
            
            for j in range(1, n):
                dp[j] = grid[i][j] + min(dp[j], dp[j-1])
        
        return dp[-1]
