class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            t1 = prices[i]
            t2 = prices[i+1]
            if t1 < t2:
                profit += t2-t1
        return profit
       