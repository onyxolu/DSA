from typing import DefaultDict, List


class Solution:
    import math
    def minDominoRotations(self, tops, bottoms) -> int:
        # It has to be one of the top[0] or bottom[0] ;)
        # check cost for both, when they are up, down and return it 4 pass ;)
        # or check only cost of making top equal -> cost of bottom == N - top   
        N = len(tops)
        def check(val):
            cost_on_top, cost_on_bottom = 0, 0
            for i in range(N):
                if tops[i] != val and bottoms[i] != val:
                    return float("inf")
                else:
                    if tops[i] != val: # he is not on top, bring him
                        cost_on_top += 1
                    if bottoms[i] != val:
                        cost_on_bottom += 1
                        
            return min(cost_on_top, cost_on_bottom)
        
        res = min(check(tops[0]), check(bottoms[0]))
        return res if res < float("inf") else -1


#class Solution:
    from collections import defaultdict
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        total = tops + bottoms
        
        d = DefaultDict(int)
        for i in total:
            d[i] += 1
            
        m = max(d, key=d.get)
        
        
        d_tops = defaultdict(int)
        d_bottoms = defaultdict(int)
        
        for i in tops:
            d_tops[i] += 1
        for i in bottoms:
            d_bottoms[i] += 1
            
        count_of_m_top = d_tops[m]
        count_of_m_bottom = d_bottoms[m]
        
        main = 0
        if count_of_m_top >= count_of_m_bottom:
            main = 1
        else:
            main = 2
       
        res = 0
        if main == 1:
            print("a")
            for i in range(len(tops)):
                if tops[i] != bottoms[i]:
                    print("b")
                    if bottoms[i] == m and tops[i] != m:
                        tops[i],bottoms[i] = bottoms[i],tops[i]
                        print("d")
                        res += 1
                        
        elif main == 2:
            for i in range(len(bottoms)):
                if tops[i] != bottoms[i]:
                    if tops[i] == m and bottoms[i] != m:
                        tops[i],bottoms[i] = bottoms[i],tops[i]
                        res += 1
        print(bottoms, tops)
        if len(set(tops)) == 1 or len(set(bottoms)) == 1:
            return res
        
        return -1
                        
                
        
        
            
        
            
            