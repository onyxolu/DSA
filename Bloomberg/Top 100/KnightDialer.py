
class Solution:
    def knightDialer(self, n: int) -> int:
        dct = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [],
               6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        dp = [1]*10
        for _ in range(n-1):
            new = [0]*10
            for el in dct:
                for num in dct[el]:
                    new[num] += dp[el]
            dp = new
        return sum(dp) % (10**9+7)


class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1] * 10
        MOD = 10 ** 9 + 7

        for i in range(2, n+1):
            old_copy = dp.copy()
            # the movements (Two vertical one Horizontal, one vertical two horizontal)
            dp[0] = old_copy[4] + old_copy[6]
            dp[1] = old_copy[6] + old_copy[8]
            dp[2] = old_copy[7] + old_copy[9]
            dp[3] = old_copy[4] + old_copy[8]
            dp[4] = old_copy[3] + old_copy[9] + old_copy[0]
            dp[5] = 0
            dp[6] = old_copy[1] + old_copy[7] + old_copy[0]
            dp[7] = old_copy[2] + old_copy[6]
            dp[8] = old_copy[1] + old_copy[3]
            dp[9] = old_copy[2] + old_copy[4]

        ans = sum(dp) % MOD
        return ans
