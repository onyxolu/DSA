
from collections import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase , decrease = False, False
        
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                increase = True
            elif nums[i] > nums[i+1]:
                decrease = True
                
            if increase and decrease:
                return False
        return True
        