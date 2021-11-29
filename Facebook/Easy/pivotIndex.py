# Time Complexity = 0(N)
# Space Complexity = 0(1)

# Sliding window 

def pivotIndex(nums):
    leftSum = 0
    rightSum = sum(nums)
    for i in range(len(nums)):
        if leftSum == rightSum - nums[i]:
            return i
        leftSum += nums[i]
        rightSum -= nums[i]
    return -1