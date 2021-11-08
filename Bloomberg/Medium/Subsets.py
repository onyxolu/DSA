

# Time Complexity => O(2^N)
# Space Complexity => O(2^N)

#BFS 


# [1,2,3]
# []
# [], [1]
# [], [1], [2], [1,2]
# [], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]



def find_subsets(nums):
    subsets = []
    subsets.append([])
    for currentNumber in nums:
        n = len(subsets)
        for i in range(n):
            new = list(subsets[i])
            new.append(currentNumber)
            subsets.append(new)
    return subsets


def find_subsets_duplicate(nums):
    list.sort(nums)
    subsets = []
    subsets.append([])
    startIndex, endIndex = 0,0
    for i in range(len(nums)):
        startIndex = 0
        # find duplicate nums
        if i > 0 and nums[i] == nums[i-1]:
            # start from where we stopped in last iteration
            startIndex = endIndex + 1
        endIndex = len(subsets) - 1
        for j in range(startIndex, endIndex+1):
            set = list(subsets[j])
            set.append(nums[i])
            subsets.append(set)
    return subsets






print(find_subsets_duplicate([1,3,3]))