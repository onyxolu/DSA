
# DP - Bottom Up
# TC => 0(n^2)
# SC => 0(n^2)

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        
        dp = [[0] * (n+1) for _ in range(n+1)]
        # dp[i][j] from i to j, what is the min remove from substr
        # remember how we check palindrome, s[i] == s[j]
        # so if they are the same we can check dp[i+1][j-1]
        
        for i in range(n+1, 0, -1):
            for j in range(i, n+1):
                if s[i-1] == s[j-1]:
                    # j - i < 2 it is a palindrome so no removes
                    dp[i][j] = 0 if j - i < 2 else dp[i+1][j-1]
                else:
                    # if we remove i=> dp[i+1][j]
                    # if we remove j=> dp[i][j-1]
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
        #   
        return dp[1][n] <= k
        