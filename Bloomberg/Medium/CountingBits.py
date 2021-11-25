

class Solution:
    def countBits(self, n: int):
        result = []
        for i in range(n+1):
            count = 0
            n = i
            while n:
                bit = n & 1
                if bit == 1: count += 1
                n >>= 1
            result.append(count)
        return result

    
# using cache

class Solution:
    def countBits(self, n: int):
        dp = [0]* (n+1)
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i: offset = i
            dp[i] = dp[i-offset]+1
        return dp