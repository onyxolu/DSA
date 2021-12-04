
from collections import List

# The idea is to traverse both list of intervals one by one with two pointers approach. We can have options:

# If we have curr[0] <= curr[1], it means that we have new intersection piece, add it to answer.
# if A[i][1] <= B[j][1], it means, that we need to move pointer for A, in the opposite case we move pointer for B.
# Complexity
# It is O(n + m) for time and the same for space.

# Code




class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j, ans = 0, 0, []
        
        while i < len(firstList) and j < len(secondList):
            curr = [max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])]
            if curr[0] <= curr[1]: # overlapping
                ans.append(curr)
            if firstList[i][1] <= secondList[j][1]:
                i += 1
            else:
                j += 1

        return ans
        
        