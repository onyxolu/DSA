# Time Complexity = 0(N)
# Space Complexity = 0(1)

# Kadanes Algorithm



import math

def maxSubArray(self, nums):
    w_sum = 0
    max_sum = -math.inf
    for i in range(len(nums)):
        w_sum +=  nums[i]
        print(w_sum, max_sum)
        max_sum = max(max_sum, w_sum)
        if w_sum < 0:
            w_sum = 0
    return max_sum