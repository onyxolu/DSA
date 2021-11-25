# Time = 0(nm)
# Space = 0(n)

# Dynamic Programming Bottom Up

# If we go greedy starting from largest num to smallest it doesn't pass all
# [1,3,4,5] will give 5,1,1 (3) instead of expected 3,4 (2)
# 
# DP Bottom UP - for each coin keep subtracting by target and checking with all the coins till you hit negative and keep track of smallest
# Normal recursion but dp to optimize like memoization for repetitve work


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [amount + 1] * (amount + 1)   # fill array with vals(amount+1) from 0 to amount    
        dp[0] = 0 #we need for amount zero is o steps min
        
        for a in range(1, amount + 1):
            for c in coins:
                # coin = 4
                # amount = 7
                # dp[7] = 1 + dp[3]
                if a - c >= 0: # if it is non zero we can continue searching
                    dp[a] = min(dp[a], 1 + dp[a-c])
                    
        return dp[amount] if dp[amount] != amount + 1 else -1




# COIN CHANGE 2!!!!!!

# Brute force - Get all paths, m^n use memoization to reduce to m*n .
# Issue, how do we guarantee we don't have duplicates. We can put rules to ignore previous coins to avoid duplicates
# We can also use dp to get m*n


def change(self, amount: int, coins) -> int:
    # MEMOIZATION
    # Time: O(n*m) 
    # Memory: O(n*m)
    cache = {}      
    
    def dfs(i, a):
        if a == amount:
            return 1
        if a > amount:
            return 0
        if i == len(coins):
            return 0
        if (i, a) in cache:
            return cache[(i, a)]
        
        cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a) # Second case is if we skip the coin at index i
        return cache[(i, a)]
    
    return dfs(0, 0)
        
        

    # DYNAMIC PROGRAMMING
    # Time: O(n*m) 
    # Memory: O(n*m)
def change(self, amount: int, coins) -> int:
    dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
    dp[0] = [1] * (len(coins) + 1)
    for a in range(1, amount + 1):
        for i in range(len(coins) - 1, -1, -1):
            dp[a][i] = dp[a][i + 1]
            if a - coins[i] >= 0:
                dp[a][i] += dp[a - coins[i]][i]
    return dp[amount][0]
    
    

    # DYNAMIC PROGRAMMING
    # Time: O(n*m) 
    # Memory: O(n) where n = amount
def change(self, amount: int, coins) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1
    for i in range(len(coins) - 1, -1, -1):
        nextDP = [0] * (amount + 1)
        nextDP[0] = 1
        
        for a in range(1, amount + 1):
            nextDP[a] =  dp[a]
            if a - coins[i] >= 0:
                nextDP[a] += nextDP[a - coins[i]] 
        dp = nextDP
    return dp[amount]
    
    