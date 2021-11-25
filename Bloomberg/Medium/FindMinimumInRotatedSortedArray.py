
# Binary Search


class Solution:
    def findMin(self, nums) -> int:
        if not nums: 
            return 0
        
        lo = 0
        hi = len(nums)-1
        while nums[lo] > nums[hi]:
            mid = (lo+hi)//2
            if nums[mid] < nums[hi]:
                # notice it's not mid-1
                hi = mid
            else:
                lo = mid+1
        return nums[lo]   
        