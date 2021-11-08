class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        min_price_so_far = prices[0]
        profit = 0
        max_profit_so_far = 0
        
        for price in prices[1:]:
            profit = price - min_price_so_far
            max_profit_so_far = max(profit,max_profit_so_far)
            min_price_so_far = min(price,min_price_so_far)
        
        return max_profit_so_far