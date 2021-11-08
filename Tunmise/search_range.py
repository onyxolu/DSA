class Solution(object):
    def searchRange(self, nums, target):
        start, end = 0, len(nums) - 1
        left = None 
        # we first try to find the leftest index for the target
        while start <= end:
            mid = start + (end-start)/2
            if nums[mid] > target: 
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                left = mid 
                end = mid - 1
        if left == None: #it means there is no index storing target, no need for the next step
            return [-1, -1]
        
        right = None # we search the rightest index for the target
        start,end = left, len(nums)-1 #no need to search the whole list again, we start from the 'left' index
        while start <= end:
            mid = start + (end-start)/2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                right = mid
                start = mid+1
        return [left, right]