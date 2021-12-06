
from collections import List
# we can do linear search but its 0(N)
# so we use binary search 0(logN) since its sorted to a point


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid
                
        return left
#         peak = 0
#         peakVal = float("-inf")
#         for i in range(len(nums)):
#             if nums[i] >= peakVal:
#                 peak = i
#                 peakVal = nums[i]
                
#         return peak
