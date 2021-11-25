
from heapq import *
from collections import Counter

class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        # AAABBC
        
        output, maxHeap = 0, []
        
        c = Counter(tasks)
        for k,v in c.items():
            heappush(maxHeap, (-v, k))
            
        while maxHeap:
            i, temp = 0, []
            while i <= n:
                output += 1
                if maxHeap:
                    nums, key = heappop(maxHeap)
                    nums += 1
                    if nums < 0: temp.append((nums, key))
                if not maxHeap and not temp: break
                i += 1
            for k,v in temp:
                heappush(maxHeap, (k,v))
                
        return output