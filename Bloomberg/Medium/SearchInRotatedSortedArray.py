
# To sort is NLOGN
# to loop through and find is 0(N)
# Binary Search - 0(LogN)

class Solution:
    def search(self, nums, target: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1   0(N)
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            
            # Left Sorted Portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # Right Sorted Portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
        return -1