
from collections import List
# Linear Search

class Solution:
	def findKthPositive(self, arr: List[int], k: int) -> int:
		j = 0
		for i in range(1, arr[-1]):
			if i == arr[j]:
				j += 1
			else:
				k -= 1

			if k == 0:
				return i

		return arr[-1] + k



# Binary Search

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        l = 0
        r = len(arr)
        
        while l < r:
            mid_i = l + (r-l)//2
            
            mid = arr[mid_i]
            
            if mid - (mid_i+1) < k:
                l = mid_i + 1
            else:
                r = mid_i
             
    
        start = l - 1
        
        if start == -1:
            return k
        
        start_num = arr[start]
        return start_num + k - (start_num - (start+1))