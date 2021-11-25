
# Sliding window

class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        # the idea is to implement sliding window with cumulative sum
        # when (csum) >= (target), we can shrink the window from the left
        # the (res) keeps the minimum size of the subarray
		# the time complexity is O(n)
        
        left, csum, res = 0, 0, float("inf")
        
        for i, val in enumerate(nums):
            csum += val
            while csum >= target:
                res = min(res, i - left + 1)
                csum -= nums[left]
                left += 1
        
        return res if res != float("inf") else 0