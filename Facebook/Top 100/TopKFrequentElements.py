
from collections import Counter
from heapq import *

# Time = 0(NlogK)
# Space = 0(N)


class Solution:
    def topKFrequent(self, nums, k: int):
        if not nums or k <= 0:
            return []
        
        # create a dictionary
        numsDict = Counter(nums)
        
        #Create a Heap, negative freq to convert to maxHeap
        maxHeap = [(-freq, num) for num, freq in numsDict.items()]
        heapify(maxHeap)
        
        # Return top K results from heap
        result = [heappop(maxHeap)[1] for _ in range(k)]
        return result
        