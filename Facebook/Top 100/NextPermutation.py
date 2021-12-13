from collections import List

# How to swap and how to select the elements to swap?

# for decending array, we either sort(nlogn) or use swap method (n)
# for ascending array, we can swap any elements but we need the next greater so we swap the last two

# Algo
# swap only using the last ascending sub array bcos any element b4 it will have a higher weight tag
# then sorting the rest to the right is important
# [2,3,4,2]
# after swapping [2,4,3,2]
# after sorting ascending [2,4,2,3] from left swap to the end
# SPecial case [1,2,3,5,4,2]
# we can't swap [3,5] cos 4 is greater than 3, so we swap [3,4]

#TC - nlog(N) worst 

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return
        i = 1
        lastInc = -1
        # get last increasing
        while i < n:
            if nums[i] > nums[i-1]:
                lastInc = i
            i += 1
        # check if array is descending and handle
        if lastInc == -1:
            #sort to ascending with swap method 
            for i in range(n//2):
                nums[i], nums[n-i-1] = nums[n-i-1], nums[i]
            return
        # find elements in the range (nums[lastInc-1] to nums[lastInc])
        index = lastInc
        # handle special case SPecial case [1,2,3,5,4,2]
        for i in range(lastInc, n):
            if nums[i] > nums[lastInc-1] and nums[i] < nums[index]:
                index = i
            
        # swap and sort
        nums[lastInc-1], nums[index] = nums[index], nums[lastInc-1]
        nums[lastInc:] = sorted(nums[lastInc:])
        return nums
            