

# slidig window move and shrink

class Solution:
    def longestOnes(self, nums, k: int) -> int:
        l, mx = 0, 0
        for r,n in enumerate(nums):
            k -= (1-n) # if it is a 1, subtract k
            if k < 0: # shrink the window
                k += (1-nums[l])
                l += 1
            mx = max(mx, r-l+1)
            
        return mx