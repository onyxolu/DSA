
arr = [2, 3, 4, 1, 5]
k = 2

# Pattern - Sliding window
# sum window val
# for every window of size k compute max sum
# return maxsum
        
def maxSum(arr, k):
    w_sum = 0
    w_start = 0
    max_sum = 0


    for w_end in range(len(arr)):
        w_sum += arr[w_end]
        if w_end + 1 >= k:
            if w_sum > max_sum:
                max_sum = w_sum
            w_sum -= arr[w_start]
            w_start += 1

    return max_sum

print(maxSum(arr, k))

# Time Complexity => 0(N)
# Space Complexity => 0(1)