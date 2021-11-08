def twoSum(nums, target):
        s = dict()
        for i in range(len(nums)):
            value = target - nums[i]
            if value not in s:
                s[nums[i]] = i
            else:
                return [s[value],i]