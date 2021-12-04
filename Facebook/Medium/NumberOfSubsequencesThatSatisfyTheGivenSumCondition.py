

# Two Pointers

from collections import List

# Brute force check every single combination, 2^n
# Optimal => 0(NlogN) worst 0(n^2)
# sort
# for each letter, check for length (n) of subsequence that meets requirement. then add 2^n to result
# e.g [3,5,6,7], 9 will be [3,5,6] n = 3
# then return ans

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        mod = (10**9 + 7)
        
        r = len(nums) - 1
        for i, left in enumerate(nums):
            while (left + nums[r]) > target and i <= r:
                r -= 1
            if i <= r:
                res += (2**(r-i)) 
                res %= mod
                
        return res
        