arr = [2,3,4,5,6,7,8,9,10, 11]

# Time: 0(N)
# Space: 0(1)

def slide(arr, k):
    result = []
    windowStart, windowSum = 0,0
    for windowKey in range(len(arr)):
        windowSum += arr[windowKey]

        if windowKey >= k - 1:
            result.append(windowSum/k)
            windowSum -= arr[windowStart]
            windowStart += 1

    return result

print(slide(arr, 5))