
from collections import List

#Basically, we keep track of the last interval. For every cut we are going to make, we cut the last interval. finally, do some string and list tricks to return in the desired format.

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        intervals = [[lower, upper]]
        for cut in nums:
            if cut == intervals[-1][0]:
                intervals[-1][0] += 1
            else:
                intervals[-1][1] = cut-1
                intervals += [[cut+1, upper]]
        return [f'{start}->{end}' if start != end else str(start) for start, end in intervals if start <= end]