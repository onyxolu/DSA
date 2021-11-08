

def runningSum(nums):
    result = []
    res = 0
    for i in range(len(nums)):
        res += nums[i]
        result.append(res)
    return result