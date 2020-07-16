class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if k == 0:
            return []
        for i in range(k):
            nums.insert(0,nums[len(nums)-1])
            nums.pop()