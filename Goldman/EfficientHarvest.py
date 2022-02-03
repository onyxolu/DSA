def maxHarvest(arr, k):
    n = len(arr)
    maxProfit = float('-inf')

    # Evaluate all n/2 harvesting options (6 slices->3 options, 4 slices->2 options, and so on)
    for i in range(n//2):
        sm = 0
        for j in range(k):
            currIndex = i+j
            # adding n//2 gets us the opposite slice's index. %2 for wrapping around array
            oppositeIndex = (currIndex+(n//2)) % n
            sm += arr[currIndex] + arr[oppositeIndex]
        maxProfit = max(maxProfit, sm)

    return maxProfit


print(maxHarvest([3, -5], 1))  # -2
print(maxHarvest([1, 5, 1, 3, 7, -3], 2))  # 16
print(maxHarvest([-6, 3, 6, -3], 1))  # 0


def effHarvest(arr, k):
    n = len(arr)
    rotate = n // 2
    windowSum = float('-inf')
    iterator = 0
    prefixSum = [0] * (2 * n + 1)

    for i in range(n):
        prefixSum[i + 1] = prefixSum[i] + arr[i]
    for i in range(n):
        prefixSum[i + n + 1] = prefixSum[i + n] + arr[i]

    while iterator <= (len(arr) // 2) - 1:
        currSum = (prefixSum[iterator + k] - prefixSum[iterator]) + \
            (prefixSum[iterator + rotate + k] - prefixSum[iterator + rotate])
        windowSum = max(windowSum, currSum)
        iterator += 1

    return windowSum


def max_profit(k: int, profit: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(profit)//2
    sum = 0
    for i in range(k):
        sum += profit[i] + profit[i+n]
    max_sum = sum
    for i in range(1, n):
        sum = sum + profit[(i+k-1) % n] - profit[i-1] + \
            profit[(i+k-1) % n+n] - profit[i+n-1]
        if sum > max_sum:
            max_sum = sum
    return max_sum


# https://leetcode.com/discuss/interview-question/1321204/efficient-harvest-faang-oa-question-2021
