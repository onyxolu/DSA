

from collections import Counter
from heapq import *

# Time = 0(NlogK)
# Space = 0(N)

class Solution:
    def topKFrequent(self, words, k: int):
        
        # error checking
        if not words or k <= 0:
            return []
        
        # create a dictionary
        wordsDict = Counter(words)
        
        #Create a Heap, negative freq to convert to maxHeap
        maxHeap = [(-freq, word) for word, freq in wordsDict.items()]
        heapify(maxHeap)
        
        # Return top K results from heap
        result = [heappop(maxHeap)[1] for _ in range(k)]
        return result