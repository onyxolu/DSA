
from collections import List, Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        dict = Counter(nums1)
        res = []
        for val in nums2:
            if val in dict and dict[val] > 0:
                res.append(val)
                dict[val] -= 1
                
        return res
    
    
    
    
        # follow Up
        # if sorted
        # i, j = 0,0
        # output = []
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] < nums2[j]:
        #         i += 1
        #     elif nums1[i] > nums2[j]:
        #         j += 1
        #     else:
        #         output.append(nums1[i])
        #         i += 1
        #         j += 1
        # return output
            