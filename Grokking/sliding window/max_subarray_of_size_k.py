arr = [2, 3, 4, 1, 5]

# // Loop Through
# //  Add value to maxsum till k
# // slide and update with maxsum

# Time: 0(N)
# Space: 0(1)

def maxSubarray(arr, k):
    maxSum = 0
    sum = 0
    windowStart = 0
    for windowKey in range(len(arr)):
        sum += arr[windowKey]

        if windowKey >= k - 1:
            maxSum = max(maxSum, sum)
            sum -= arr[windowStart]
            windowStart += 1

    return maxSum

print(maxSubarray(arr, 2))
