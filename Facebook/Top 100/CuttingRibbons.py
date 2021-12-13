
# Binary Search

from collections import List

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        
        low, high = 1, max(ribbons)
        
        while low <= high:
            
            mid = low + (high - low) // 2
            
            # add number of ribons that can be made
            num_cuts = sum(ribbon//mid for ribbon in ribbons)
            print(num_cuts, mid)
            # 3 5
            # 2 7
            # 2 6
            
            # keep searching for a possibly larger size that can make k 
            if num_cuts >= k:
                low = mid + 1
            else:
                high = mid - 1
        
        return low - 1
    
    
    
