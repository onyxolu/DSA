from heapq import *

# Min Heap Solution
# Time Complexity => 0(k*logN)
# Space => 0(N)

import heapq

def KClosest(points, k):
    res = []
    minHeap = []
    for x,y in points:
        dist = (x*x) + (y*y)
        minHeap.append([dist, x, y])

    heapq.heapify(minHeap)
    for _ in range(k):
        dist,x,y = heapq.heappop(minHeap)
        res.append([x,y])
    return res


print(KClosest([[3,3],[5,-1],[-2,4]], 2))