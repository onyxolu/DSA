
# nums = [1, 2, 3, 3]

# HashMap
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        for num in nums:
            if num in numsSet:
                return True
            else:
                numsSet.add(num)
        return False
    
# sorting
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_sorted = sorted(nums)
        for idx in range(1, len(nums)):
            if nums_sorted[idx] == nums_sorted[idx-1]:
                return True
        return False