
from collections import List

# Set

class SparseVector:
    def __init__(self, nums: List[int]):
        self.s = set()
        self.nums = nums
        for idx, num in enumerate(nums):
            if num != 0:
                self.s.add(idx)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        
        for idx in self.s & vec.s:
            ans += self.nums[idx] * vec.nums[idx]
        
        return ans
    
    
# Hashmap


class SparseVector:
    def __init__(self, nums: List[int]):
        self.seen = {}
        for idx, num in enumerate(nums):
            if num != 0:
                self.seen[idx] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        
        for key in vec.seen:
            if key in self.seen:
                ans += self.seen[key] * vec.seen[key]
        
        return ans
    
    
    
    
    
    

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)