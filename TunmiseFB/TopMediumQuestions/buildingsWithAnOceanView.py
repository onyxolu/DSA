'''
Algorithm

1 - Initialize maxHeight to -1. It will store the maximum height of the buildings to the right of the current building.
2 - Iterate over the buildings array from right to left.
    If the current building is taller than maxHeight, then append its index to the answer array and update maxHeight with the current building's height.
3 - At the end, the answer array has the indices of the buildings that can see the ocean in descending order.
4 - Reverse the answer array (to make it in ascending order) and return it.


Here N is the size of the given array.

Time complexity: O(N) - We iterate over the given array once, and for each building height, we perform a constant    number of operations.
The answer array is reversed at the end, which also takes O(N) time.

Space complexity: O(1) - No auxiliary space was used other than for the output array.
'''


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = []
        max_height = -1
        
        for current in reversed(range(n)):
            # If there is no building higher (or equal) than the current one to its right,
            # push it in the answer array.
            if max_height < heights[current]:
                answer.append(current)
            
                # Update max building till now.
                max_height = heights[current]
        
        answer.reverse()
        return answer

#        for i in range(len(heights)-1,-1,-1) 