
from collections import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Two Pointers 0(N)
        # highest that can happen is the most negative number bigger than the most positive number
        
        if not nums:
            return []
        ans = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        insertLoc = right
        
        while left <= right:
            leftSq = nums[left] * nums[left]
            rightSq = nums[right] * nums[right]
            
            if leftSq <= rightSq:
                ans[insertLoc] = rightSq
                right -= 1
                
            else:
                ans[insertLoc] = leftSq
                left += 1
                
            insertLoc -= 1
        return ans