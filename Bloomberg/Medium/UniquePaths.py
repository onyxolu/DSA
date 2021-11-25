

# Bottom up DP
# Time: O(M*N), where M <= 100 is number of rows, N <= 100 is number of columns.
# Space: O(M*N)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    dp[r][c] = 1
                elif r == 0:
                    dp[r][c] = dp[r][c-1]
                elif c == 0:
                    dp[r][c] = dp[r-1][c]
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[m-1][n-1]


#  Solution 2: Bottom up DP (Space Optimized)

# Since we only access 2 states: current state dp and previous state dpPrev, we can reduce the space complexity to O(M).


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp, dpPrev = [0] * n, [0] * n
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    dp[c] = 1
                elif r == 0:
                    dp[c] = dp[c-1]
                elif c == 0:
                    dp[c] = dpPrev[c]
                else:
                    dp[c] = dpPrev[c] + dp[c-1]
            dp, dpPrev = dpPrev, dp
        return dpPrev[n-1]


# Time: O(M*N), where M <= 100 is number of rows, N <= 100 is number of columns.
# Space: O(M)