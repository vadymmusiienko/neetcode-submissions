class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                left = dp[r][c - 1] if (c - 1) >= 0 else 0
                up = dp[r - 1][c] if (r - 1) >= 0 else 0
                dp[r][c] = max(left + up, 1)

        return dp[m - 1][n - 1]
        