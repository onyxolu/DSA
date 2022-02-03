
class Solution:
    def checkPossibility(self, nums) -> bool:
        N = len(nums)
        mn, mx = float("inf"), float("-inf")
        n, m = 0,0
        
        # first pass
        for i in range(N):
            if nums[i] < mx:
                n += 1
            mx = max(nums[i], mx)
            
        # second pass
        for j in range(N-1, -1,-1):
            if nums[j] > mn:
                m += 1
            mn = min(nums[j], mn)
        
        return n <= 1 or m <= 1