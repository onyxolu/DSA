
arr = [3, 4, 1, 1, 6]

# [5,2]

def smallest_subarray(arr, k):
    min_length = float("inf")
    window_start = 0
    window_sum = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while(window_sum >= k):
            print(min_length, window_end - window_start + 1)
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    if min_length == float("inf"):
        return 0
    return min_length


print(smallest_subarray(arr, 8))

