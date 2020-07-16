class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        if(collections.Counter(nums).most_common()[0][1]>=2):
            return True
        return False
            