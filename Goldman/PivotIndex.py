def pivotIndex(self, nums: List[int]) -> int:
    rightSum = sum(nums)
    
    leftSum = 0
    
    for i in range(len(nums)):
        if leftSum == rightSum - nums[i]:
            return i
        
        leftSum += nums[i]
        rightSum -= nums[i]
        
    return -1