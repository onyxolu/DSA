

# For a valid triangle, a+b > c

# Three Pointers

# Time = 0(NLogN + N^2)
# Space = 0(1)


class Solution:
    def triangleNumber(self, nums) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for k in range(2,n):
            i,j = 0, k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    res += j-i
                    j -= 1
                else:
                    i += 1
                    
        return res
        