class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tracker = {}
        for num in nums:
            if num in tracker:
                tracker[num] += 1
            else:
                tracker[num] = 1
        
        for valueKey in tracker:
            if tracker[valueKey] == 1:
                return valueKey
