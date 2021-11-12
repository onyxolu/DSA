
from heapq import *

def find_num(nums,k):
    minHeap = []
    # Push first k elements in heap
    for i in range(k):
        heappush(minHeap, nums[i])

    for i in range(k, len(nums)):
        if nums[i] > minHeap[0]:
            heappop(minHeap)
            heappush(minHeap, nums[i])
    return list(minHeap)


print(find_num([5, 12, 11, -1, 12], 3))