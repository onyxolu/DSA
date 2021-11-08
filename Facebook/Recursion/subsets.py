# Time Complexity => O(N*2^N)
# Space Complexity => O(N*2^N)

# []
# [] - [1]
# [] [1] - [2] [1,2]
# [] [1] [2] [1,2] - [3] [1,3] [2,3] [1,2,3]


def subsets(nums):
    subsets = [[]]
    for currentNumber in nums:
        n = len(subsets)
        for i in range(n):
            set = list(subsets[i])
            set.append(currentNumber)
            subsets.append(set)
    return subsets


def subsets_reptitive(nums):
    subsets = [[]]
    startIndex, endIndex = 0,0
    for i in range(len(nums)):
        startIndex = 0
        n = len(subsets)
        if i > 0 and nums[i] == nums[i-1]:
            startIndex = endIndex + 1
        endIndex = len(subsets) - 1
        for j in range(startIndex, endIndex + 1):
            set = list(subsets[j])
            set.append(nums[i])
            subsets.append(set)
    return subsets


# Recursive

def subsets_rec(nums, idx=None):
    if idx is None:
        idx = len(nums) - 1
    elif idx < 0:
        return [[]]
    ele = nums[idx]
    subsets = subsets_rec(nums, idx - 1)
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [ele])
    return subsets



print(subsets_reptitive([1,3,3]))
