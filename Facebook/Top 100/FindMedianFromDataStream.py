

# let's say 1,3,2,4
# small heap [1,2] it's max heap cos I need the max value
# large heap [3,4] it's min heap cos I need the min value

# flow
# by default add to small heap

import heapq

class MedianFinder:

    def __init__(self):
        # two heaps, large, small, minHeap, maxHesp
        # heaps should be equal size
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        # by default, add to small heap
        heapq.heappush(self.small, -1 * num)
        
        #make sure every num small is <= every num in large
        if (self.small and self.large and
           (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # uneven size?
        if len(self.small) > len(self.large) + 1: # diff is 2 or greater
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2
        