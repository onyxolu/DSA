import heapq
from collections import deque
# since the array is sorted, then Binary Search to search for x index


# Two Pointers - Optimal
# Time = 0(logN + 0(K))
# Space = 0(1)

def find_closest_elem(arr, k, x):
    idx = binary_search(arr,x)
    left, right = idx, idx+1
    n = len(arr)
    result = deque()
    for i in range(k):
        if left >= 0 and right < n:
            dif1 = abs(x - arr[left])
            dif2 = abs(x - arr[right])
            # we are looking for the smaller one
            if dif1 <= dif2: # left is smaller
                result.appendleft(arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
        elif left >= 0:
            result.appendleft(arr[left])
            left -= 1
        elif right < n:
            result.append(arr[right])
            right += 1

    return result





# Heap Solution 
# Time = 0(LogN + kLogK)
# Space = 0(K)

def find_closest_elem2(arr, k, x):
    idx = binary_search(arr,x)
    low, high = idx - k, idx + k
    low = max(low,0) # low should not be less than Zero
    high = min(high, len(arr) - 1) # high should not be greater than the size of the array

    minHeap = []
    # Add all values from low to high to minHeap sorted by Absolute differnce from X
    for i in range(low, high+1):
        heapq.heappush(minHeap, (abs(arr[i] - x), arr[i]))

    result = []
    # get top K elements
    for _ in range(k):
        result.append(heapq.heappop(minHeap)[1])
    result.sort()
    return result


def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = int(low + (high - low)/2)
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if low > 0:
        return low - 1
    return low


print(find_closest_elem([1,2,3,4,5], 4, 3))
