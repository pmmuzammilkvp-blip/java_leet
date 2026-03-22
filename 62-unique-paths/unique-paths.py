class Solution:
    def uniquePaths(self, m, n):
        res = 1
        for i in range(1, m):
            res = res * (n - 1 + i) // i
        return res
