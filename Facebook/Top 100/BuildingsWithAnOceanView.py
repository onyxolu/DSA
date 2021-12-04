
# Double ended queue, appendLeft

from collections import deque, List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxRight = float("-inf")
        ans = deque()
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > maxRight:
                ans.appendleft(i)
            maxRight = max(heights[i], maxRight)
        return ans