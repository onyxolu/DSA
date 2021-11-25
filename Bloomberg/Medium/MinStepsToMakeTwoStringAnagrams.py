
# Hashmap solution

from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sFreq = Counter(s)
        tFreq = Counter(t)
        steps = 0
        
        for val in sFreq:
            si = sFreq.get(val, 0) - tFreq.get(val,0)
            if si > 0:
                steps += si
                
        return steps