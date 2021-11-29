
from collections import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
       
        # sets
        set1 = set(nums1)
        set2 = set(nums2)
        
        return (set1.intersection(set2))


        # dict = Counter(nums1)
        # res = []
        # for val in nums2:
        #     if val in dict:
        #         res.append(val)
        #         del dict[val]
                
        # return res