import math

arr = [2, 1, 5, 2, 3, 2]
s = 7

# Pattern - Sliding window
# sum window val
# when window sum is equal or exceeds given sum, shrink
# keep track of minlength
# return min length

def smallArr(arr, s):
    w_start = 0
    w_sum = 0
    min_length = math.inf

    for w_end in range(len(arr)):
        w_sum += arr[w_end]

        while w_sum >= s:
            min_length = min(min_length, w_end - w_start+1)
            w_sum -= arr[w_start]
            w_start += 1
        
    if min_length == math.inf:
        return 0
    return min_length

print(smallArr(arr,s))

# Time Complexity => 0(N)
# Space Complexity => 0(1)