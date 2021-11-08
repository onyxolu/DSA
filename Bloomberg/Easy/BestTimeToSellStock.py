# [7,1,5,3,6,4]

# Time Complexity = 0(N)
# Space Complexity = 0(1)

# Two Pointers

def maxProfit(prices):
    l,r = 0,1
    maxP = 0
    while r < len(prices):
        print(prices[l], prices[r])
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(profit, maxP)
        else:
            l = r
        r += 1
    return maxP

print(maxProfit([7,1,5,3,6,4]))


# More than one transaction
def maxProfit2(prices):
    profit = 0
    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            profit += prices[i+1] - prices[i]
    return profit
