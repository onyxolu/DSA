def CountingPairs(arr, k):
    count = 0
    arr.sort()

    l = 0
    r = 0
    seen = set()

    while r < len(arr):
        if arr[r] - arr[l] == k and (arr[r] not in seen or arr[l] not in seen):
            count += 1
            seen.add(arr[r])
            seen.add(arr[l])
            l += 1
            r += 1

        elif arr[r] - arr[l] > k:
            l += 1
        else:
            r += 1
    return count

print(CountingPairs([1,1,1,2], 1))
