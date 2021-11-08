# Time Complexity => O(N*N!)
# Space Complexity => O(N*N!)

from collections import deque

def perm(nums):
    numsLength = len(nums)
    result = []
    permutations = deque()
    permutations.append([])
    for currentNumber in nums:
        n = len(permutations)
        for _ in range(n):
            oldPermutation = permutations.popleft()
            for j in range(len(oldPermutation)+1):
                newPermutation = list(oldPermutation)
                newPermutation.insert(j, currentNumber)
                if len(newPermutation) == numsLength:
                    result.append(newPermutation)
                else:
                    permutations.append(newPermutation)
    return result


def perm_recursive(nums):
    result = []
    generatePerms_rec(nums, 0, [], result)
    return result

def generatePerms_rec(nums, index, currentPermutation, result):
    if index == len(nums):
        result.append(currentPermutation)
    else:
        for i in range(len(currentPermutation)+1):
            newPermutation = list(currentPermutation)
            newPermutation.insert(i, nums[index]) 
            generatePerms_rec(nums, index+1, newPermutation, result)


print(perm_recursive([1,3,5]))