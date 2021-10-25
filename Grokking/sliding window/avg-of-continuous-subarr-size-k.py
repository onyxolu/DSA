arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5

# Pattern - Sliding window
# sum window val
# for every window of size k find avg
# append to arr and return result


def avgCont(arr, k):
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    k = 5
    w_sum = 0
    w_start = 0
    ans = []

    for i in range(len(arr)):
        w_sum += arr[i]
        if i+1 >= k:
            ans.append(w_sum/k)
            w_sum -= arr[w_start]
            w_start += 1 


    return ans

print(avgCont(arr, k))

# Time Complexity => 0(N)
# Space Complexity => 0(1)