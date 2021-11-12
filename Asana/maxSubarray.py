# Time Complexity = 0(N)
# Space Complexity = 0(1)

# Kadanes Algorithm



def maxSubArray(self, nums):
    maxSub = nums[0]
    curSum = 0
    for num in nums:
        if curSum < 0:
            curSum = 0
        curSum += num
        maxSub = max(maxSub, curSum)
    return maxSub