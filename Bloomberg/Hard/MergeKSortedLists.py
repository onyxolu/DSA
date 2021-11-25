

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import *

# Time  = O(N∗logK)
# Space = 0(K)

class Solution:

    def mergeKLists(self, lists):
                # Brute force - Add all  K lists into one list then sort (NLOGN) + nm
        # We can always find the smallest number for the k lists using heap
        
        # Initialize the min heap
        minHeap = []
        
        # put the root of each list in minHeap
        for idx, root in enumerate(lists):
            if root:
                heappush(minHeap, (root.val, idx,  root))
                
                
        # Take the smallest(top) element from the minheap and add to result
        # if the top element has a next element, add to heap
        
        resultHead, resultTail = None, None
        
        while minHeap:
            nodeVal, idx, node = heappop(minHeap)
            print(nodeVal, resultHead)
            if resultHead is None:
                resultHead = resultTail = node
            else:
                resultTail.next = node
                resultTail = resultTail.next
                
            if node.next is not None:
                heappush(minHeap, (node.next.val, idx, node.next))
                
        return resultHead