class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        a, b = 1, 2  # dp[1] = 1, dp[2] = 2
        for _ in range(3, n+1):
            a, b = b, a + b  # Fibonacci update

        return b
