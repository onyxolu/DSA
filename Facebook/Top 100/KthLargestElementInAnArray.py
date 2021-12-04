
from collections import List
from heapq import *

class Solution:
	# using sorted
	# time O(nlogn)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]


	# using maxheap
	# time O(n + (n-k)logn)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums) # takes O(n) to sort
        for _ in range(len(nums)-k):  # takes (size-k)*logn to pop
            heappop(nums)
        return nums[0]  # kth largest element can now be found at root

	# using Quick Select
	# time Best => 0(N) worst => 0(n^2)

    # pick a pivot
    # put all numbers lesser to the left and greater to the right
    # Have a left and right pointer
    # if left > p and right < p, then swap
    # when left > right, if p is k, then we've found it else we do QS on left or right (unlike quick sort, we are not looking at both halves)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k    # to get the index of k
        
        def quickSelect(l,r):
            pivot, p = nums[r], l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p] # swap
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            
            if p > k: return quickSelect(l, p-1)
            elif p < k: return quickSelect(p + 1, r)
            else: return nums[p]
        return quickSelect(0, len(nums) - 1)


