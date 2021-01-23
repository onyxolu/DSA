
arr = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]

def longestOnes(arr, k):
    window_start = 0
    window_ones_count = 0
    max_length = 0
    for window_end in range(len(arr)):
        window_length = window_end - window_start + 1
        if arr[window_end] == 1:
            window_ones_count += 1

        if (window_length - window_ones_count) > k:
            if arr[window_start] == 1:
                window_ones_count -= 1
            window_start += 1 

        max_length = max(max_length, window_length)

    return max_length

print(longestOnes(arr, 3))