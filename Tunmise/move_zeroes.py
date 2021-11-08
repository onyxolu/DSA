class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        w ,i,c= 0,0,0
        
        while i < len(nums):
            if nums[i] != 0:
                nums[w] = nums[i]
                w += 1
    
            
            i += 1
        # l = [0]*c
        # nums[w:] = l
        while w < len(nums):
            nums[w] = 0
            w +=1
            
        return nums