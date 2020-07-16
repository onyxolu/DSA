class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeronum = 0;
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.insert(len(nums) - zeronum, 0)