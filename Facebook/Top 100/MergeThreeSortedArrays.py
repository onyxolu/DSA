# Python program to merge three sorted arrays
# simultaneously.


from heapq import *

# Time  = O(N∗logK)
# Space = 0(K)



def mergeKLists( a,b,c):
	# Brute force - Add all  K lists into one list then sort (NLOGN) + nm
	# We can always find the smallest number for the k lists using heap
	
	# Initialize the min heap
	minHeap = []

	if a:
		heappush(minHeap, a)
	
	if b:
		heappush(minHeap, b)

	if c:
		heappush(minHeap, c)
	
			
			
	# Take the smallest(top) element from the minheap and add to result
	# if the top element has a next element, add to heap
	
	res = []
	
	while minHeap:
		val = heappop(minHeap)

		if not res or val[0] != res[-1]:
			res.append(val[0])
		if len(val) > 1:
			heappush(minHeap, val[1:])
			
			
	return res


	
def merge_arrays(arr1, arr2, arr3):
    aptr, bptr, cptr = 0, 0, 0
    result = []
    
    while aptr < len(arr1) or bptr < len(arr2) or cptr < len(arr3): # 1, 2, 0
        num1 = arr1[aptr] if aptr < len(arr1) else float('inf') # 4
        num2 = arr2[bptr] if bptr < len(arr2) else float('inf') # 4
        num3 = arr3[cptr] if cptr < len(arr3) else float('inf') # 3
        
        min_val = min(num1, num2, num3) # 2
        if not result or result and result[-1] != min_val:
            result.append(min_val) # 1 2
            
        if min_val == num1:
            aptr += 1
        if min_val == num2:
            bptr += 1
        if min_val == num3:
            cptr += 1
            
    return result


a = [1, 2, 2, 3, 41, 52, 84]
b = [1, 2, 41, 52, 67]
c = [1, 2, 41, 52, 67, 85]

print(merge_arrays(a,b,c))
