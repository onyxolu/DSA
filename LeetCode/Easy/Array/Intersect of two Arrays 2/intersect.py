class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = {}
        set2 = {}
        intersect = []
        
        for num in nums1:
            if num in set1:
                set1[num] += 1
            else:
                set1[num] = 1
            
            
        for num in nums2:       
            if num in set2:
                set2[num] += 1
            else:
                set2[num] = 1
                
        for valueKey in set1:
            if valueKey in set2:
                inst = min(set2[valueKey],set1[valueKey])
                for num in range(inst):
                    intersect.append(valueKey) 
        return intersect