
from collections import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Brute force -> find all subarrays and cout sum 2^n
        # optimal => Prefix sums TC- 0(N) , SC-0(N)
        
        #[1,2,3] 3
        # {0:1}  diff -3 res = 0
        # [1] diff -2 {0:1, 1:1}  res = 0
        # [1,2] diff 0 {0:1, 1:1, 3: 1} res = 1, we have 1 subarr from 2
        # [1,2,3] diff 3 {0:1, 1:1, 3:1, 6:1} res = 1+1 
        
        res, curSum = 0,0
        prefixSums = {0: 1}
        for n in nums:
            curSum += n
            diff = curSum - k
            
            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        return res