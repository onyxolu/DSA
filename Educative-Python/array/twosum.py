def twosum(nums, target):
    dic = {}
    for i in range(len(nums)):
        rem = target - nums[i]
        if nums[i] in dic:
            return [dic[nums[i]], i]
        dic[rem] = i
    return []

print(twosum([2,7,11,15], 9))
    