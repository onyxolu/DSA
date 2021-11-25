

# Recursion O(2^N APPROACH)

import sys

class Solution:
    def help(self,grid,i,j,m,n):
        if i==m-1 and j==n-1:
            return grid[i][j]
        if i>=m or j>=n:
            return sys.maxsize
        left=grid[i][j]+self.help(grid,i+1,j,m,n)
        right=grid[i][j]+self.help(grid,i,j+1,m,n)
    

        return min(left,right)
    def minPathSum(self, grid) -> int:
        i=0
        j=0
        m=len(grid)
        n=len(grid[0])
        return self.help(grid,i,j,m,n)


# Dp Top down Approach O(M*N) with recursion call stack space

class Solution:
    def help(self,grid,i,j,m,n,dp):
        if i==m-1 and j==n-1:
            return grid[i][j]
        if i>=m or j>=n:
            return sys.maxsize
        if dp[i][j]!=-1:
            return dp[i][j]
        left=grid[i][j]+self.help(grid,i+1,j,m,n,dp)
        right=grid[i][j]+self.help(grid,i,j+1,m,n,dp)
        dp[i][j] =min(left,right)
        return min(left,right)

    
    

    def minPathSum(self, grid) -> int:
        i=0
        j=0
        m=len(grid)
        n=len(grid[0])
        dp=[[-1 for i in range(n+1)]for j in range(m+1)]
        return self.help(grid,i,j,m,n,dp)