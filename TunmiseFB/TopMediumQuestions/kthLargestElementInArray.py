'''
We can simply use sort and count the kth element from the back, this will result in O(N log N time), simple and straight forward.
'''

class Solution:
	# using sorted
	# time O(nlogn)
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[len(nums) - k]


'''
APPROACH 2: USING HEAP

The idea is to init a heap "the smallest element first", and add all elements from the array into this heap one by one keeping the size of the heap always less or equal to k. That would results in a heap containing k largest elements of the array.

The head of this heap is the answer, i.e. the kth largest element of the array.

The time complexity of adding an element in a heap of size k is \mathcal{O}(\log k)O(logk), and we do it N times that means \mathcal{O}(N \log k)O(Nlogk) time complexity for the algorithm.

In Python there is a method nlargest in heapq library which has the same \mathcal{O}(N \log k)O(Nlogk) time complexity and reduces the code to one line.

This algorithm improves time complexity, but one pays with \mathcal{O}(k)O(k) space complexity.

'''

from heapq import *

	# using maxheap
	# time O(n + (n-k)logn)
class Solution:
    def findKthLargest(self, nums, k):
        heapify(nums) # takes O(n) to sort
        for _ in range(len(nums)-k):  # takes (size-k)*logn to pop
            heappop(nums)
        return nums[0]  # kth largest element can now be found at root




'''
APPROACH 3: USE QUICK SORT

Finally the overall algorithm is quite straightforward :

Choose a random pivot.

Use a partition algorithm to place the pivot into its perfect position pos in the sorted array, move smaller elements to the left of pivot, and larger or equal ones - to the right.

Compare pos and N - k to choose the side of array to proceed recursively.


Time complexity : O(N) in the average case, O(N^2)in the worst case.
Space complexity : O(1).

In early versions of Quick Sort where the leftmost (or rightmost) element is chosen as a pivot, the worst occurs in the following cases. 

1) Array is already sorted in the same order. 
2) Array is already sorted in reverse order. 
3) All elements are the same (a special case of cases 1 and 2) 
'''



	# using Quick Select
	# time Best => 0(N) worst => 0(n^2)

    # pick a pivot
    # put all numbers lesser to the left and greater to the right
    # Have a left and right pointer
    # if left > p and right < p, then swap
    # when left > right, if p is k, then we've found it else we do QS on left or right (unlike quick sort, we are not looking at both halves)

import random
class Solution:
    def findKthLargest(self, nums, k):
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
            
            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]  
            
            return store_index
        
        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element
            
            # select a random pivot_index between 
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest 
        return select(0, len(nums) - 1, len(nums) - k)


# listA = [1,2,3,4,5]
# random.shuffle(listA)
# print(listA)