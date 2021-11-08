

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if height == []:
            return 0
        
        globalMax = height[0]
        globalMaxIndex = 0
        
        rainWater = 0
        
        for i in range(1, len(height)):
            if height[i] > globalMax:
                globalMax = height[i]
                globalMaxIndex = i
                
        leftMax = 0
        
        #09152705835
        
        for i in range(globalMaxIndex):
            if height[i] >= leftMax:
                leftMax = height[i]
            else:
                rainWater += leftMax - height[i]
            
        rightMax = 0
        for i in range(len(height)-1, globalMaxIndex, -1):
            if height[i] >= rightMax:
                rightMax = height[i]
            else:
                rainWater += rightMax - height[i]
                
        return rainWater


def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    areas = 0
    max_l = max_r = 0
    l = 0
    r = len(height)-1
    while l < r:
        if height[l] < height[r]:
            if height[l] > max_l:
                max_l = height[l]
            else:
                areas += max_l - height[l]
            l +=1
        else:
            if height[r] > max_r:
                max_r = height[r]
            else:
                areas += max_r - height[r]
            r -=1
    return areas