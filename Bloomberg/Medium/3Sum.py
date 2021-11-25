

# Time => 0(N^2)
# Space => 0(N)

def threeSum(nums):
    targetSum = 0
    nums.sort()
    triplets = set()
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]
            if currentSum == targetSum:
                triplets.add((nums[i] , nums[left] , nums[right]))
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return list(triplets)


print(threeSum([-1,0,1,2,-1,-4]))