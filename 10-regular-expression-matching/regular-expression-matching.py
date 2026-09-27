class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # dp[i][j] = True if s[0:i] matches p[0:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Initialize: check if the empty string matches the pattern p[0:j]
        # This handles cases like "a*", "a*b*" where the pattern can match empty string
        for j in range(1, n + 1):
            # If p[j-1] is '*', it can match zero occurrences of p[j-2]
            if p[j - 1] == '*' and p[j - 2] in ('.', s[0] if m > 0 else ''):
                # Actually, we just need to check if p[j-2] is a valid character
                # and that dp[0][j-2] is True (meaning s[:0] matches p[:j-2])
                if dp[0][j - 2]:
                    dp[0][j] = True

        # More robust initialization for empty string matching
        # Let's redo it properly
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*' and dp[0][j - 2]:
                dp[0][j] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.':
                    # '.' matches any single character
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == s[i - 1]:
                    # Characters match directly
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # '*' matches zero or more of the preceding element
                    # Case 1: Treat '*' as matching zero occurrences -> skip the two chars (preceding + "*")
                    # Case 2: Treat '*' as matching one or more of the preceding element
                    #   - If s[i-1] matches p[j-2] (or p[j-2] is '.'), then we can "consume" s[i-1]
                    #     and keep using the same pattern that ends with '*'
                    dp[i][j] = dp[i][j - 2]  # zero occurrences
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]  # one or more occurrences

        return dp[m][n]