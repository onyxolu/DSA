

class Solution:
    def searchRange(self, nums, target: int):
#         binary search time comp - O(log(N))
        l = 0
        r = len(nums) - 1
        res = [-1, -1]
        
        while(l <= r):
            mid = (l+r)//2
            if nums[mid] == target:
                while(mid >= l and nums[mid] == target):
                    mid -= 1
                res[0] = mid+1
                mid += 1
                while(mid <= r and nums[mid] == target):
                    mid += 1
                res[1] = mid - 1
                break

            elif nums[mid] > target:
                r -= 1
            else:
                l += 1
        
        return res
    
#         time comp - O(N)
#         result = [-1, -1]
#         present = False
        
#         for i in range(len(nums)):
#             if nums[i] == target and present is False:
#                 present = True
#                 result[0] = i
#             if present is True and nums[i] != target:
#                 result[1] = i-1
#                 present = False
#                 break
#             print(result, nums[i], present)
        
#         if present is True and nums[-1] == target:
#             result[1] = len(nums) - 1
            
#         return result