
from collections import List

# prefix Sum
# store the mod in hashmap, key is mod, val is index
# Keep adding and try to find mod in app (basically mimicking remove previously visited)
# if found check if index is before cur index


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = {0:-1} # the position of the prefix sum
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            mod = summ % k
            print(prefix, summ, mod)
            # {0: -1} 23 5
            # {0: -1, 5: 0} 25 1
            # {0: -1, 5: 0, 1: 1} 29 5
            if mod in prefix:  # the same remainder 
                if i - prefix[mod] > 1:
                    return True     
            else:
                prefix[mod] = i
        return False