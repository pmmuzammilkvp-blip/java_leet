class Solution {
    /**
     * Counts the number of distinct subsequences of s that equal t.
     *
     * Uses dynamic programming with a 2D table where dp[i][j] represents
     * the number of ways to form t[0..j-1] using s[0..i-1].
     *
     * Base case: dp[i][0] = 1 for all i (empty t can be formed in 1 way from any prefix of s)
     *
     * Recurrence:
     *   If s[i-1] == t[j-1]:
     *     dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
     *     (either skip s[i-1] or use it to match t[j-1])
     *   Else:
     *     dp[i][j] = dp[i-1][j]
     *     (cannot use s[i-1], so must skip it)
     *
     * Space optimization: We only need the previous row of dp to compute the current row,
     * so we reduce space from O(m*n) to O(n).
     *
     * Time complexity: O(m * n) where m = s.length(), n = t.length()
     * Space complexity: O(n)
     */
    public int numDistinct(String s, String t) {
        int m = s.length();
        int n = t.length();

        // If t is longer than s, no subsequence can equal t
        if (n > m) {
            return 0;
        }

        // dp[j] represents the number of ways to form t[0..j-1] using the current prefix of s
        // Initialize with dp[0] = 1 (empty t can be formed in 1 way)
        int[] dp = new int[n + 1];
        dp[0] = 1;

        // Process each character in s
        for (int i = 1; i <= m; i++) {
            char sChar = s.charAt(i - 1);

            // Traverse t from right to left to avoid overwriting values we still need
            // Must go backwards because dp[j-1] for the current row depends on dp[j-1] from previous row
            for (int j = n; j >= 1; j--) {
                char tChar = t.charAt(j - 1);

                if (sChar == tChar) {
                    // If characters match, we can either:
                    // 1. Skip s[i-1]: use dp[j] (from previous row, which is current dp[j] before update)
                    // 2. Use s[i-1] to match t[j-1]: use dp[j-1] (from previous row)
                    dp[j] = dp[j] + dp[j - 1];
                }
                // If characters don't match, dp[j] remains unchanged (we skip s[i-1])
            }
        }

        return dp[n];
    }
}