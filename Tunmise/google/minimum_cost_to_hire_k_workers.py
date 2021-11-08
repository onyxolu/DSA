#Note that this problem can be summarized into sum(quality) * max(wage/quality). 
# The rest can be naturally solved via a greedy algo.
from heapq import heappush, heappop
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ans, rsm = float("inf"), 0
        pq = [] # max-heap 
        for q, w in sorted(zip(quality, wage), key=lambda x: x[1]/x[0]): 
            rsm += q 
            heappush(pq, -q)
            if len(pq) > k: rsm += heappop(pq)
            if len(pq) == k: ans = min(ans, rsm * w/q)
        return ans 