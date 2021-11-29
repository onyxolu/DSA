# Time Complexity = 0(N)
# Space Complexity = 0(N)

# Hashmap

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

def twoSum(nums, target):
    dic = {}
    for i in range(len(nums)):
        val = nums[i]
        rem = target - val
        if val in dic:
            return [dic[val], i]
        dic[rem] = i
    return []