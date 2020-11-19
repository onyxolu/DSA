def maxprofit(prices):
  profits = []
  for i in range(len(prices)):
    if i >= len(prices) -1:
      break
    sellingPrices = prices[i+1:]
    maxsellingprice = max(sellingPrices)
    if maxsellingprice > prices[i]:
      profits.append(maxsellingprice-prices[i])
  print(profits)
  if not profits:
    return 0
  return max(profits)

print(maxprofit([7,1,5,3,6,4, 7]))