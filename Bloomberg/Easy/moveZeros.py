# Time Complexity = 0(N)
# Space Complexity = 0(1)

# swap

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]


def moveZeros(nums):
    prevIdx = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[prevIdx], nums[i] = nums[i], nums[prevIdx]
            prevIdx += 1
    return nums


print(moveZeros([1,0,1,0,3,12]))


# No Order


# def moveElement(nums, toMove):
#         left = 0
#         right = len(nums) - 1
#         while left < right:
#             if nums[right] == toMove:
#                 right -= 1
#             if nums[left] == toMove:
#                 nums[right], nums[left] = nums[left], nums[right]
#             left += 1
        