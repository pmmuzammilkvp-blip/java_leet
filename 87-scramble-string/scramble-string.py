class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n != len(s2):
            return False

        # dp[i][j][l] = True if s1[i:i+l] is a scramble of s2[j:j+l]
        dp = [[[False] * n for _ in range(n)] for _ in range(n)]

        # Base case: length 1
        for i in range(n):
            for j in range(n):
                dp[i][j][0] = (s1[i] == s2[j])

        # Fill for lengths 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                for j in range(n - length + 1):
                    # Check all possible split points
                    for split in range(1, length):
                        # Case 1: no swap
                        # s1[i:i+split] matches s2[j:j+split] AND s1[i+split:i+length] matches s2[j+split:j+length]
                        if dp[i][j][split - 1] and dp[i + split][j + split][length - split - 1]:
                            dp[i][j][length - 1] = True
                            break
                        # Case 2: swap
                        # s1[i:i+split] matches s2[j+length-split:j+length] AND s1[i+split:i+length] matches s2[j:j+length-split]
                        if dp[i][j + length - split][split - 1] and dp[i + split][j][length - split - 1]:
                            dp[i][j][length - 1] = True
                            break

        return dp[0][0][n - 1]