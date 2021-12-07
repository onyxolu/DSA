'''

Approach 1: Brute Force
Intuition & Algorithm

Traverse all the linked lists and collect the values of the nodes into an array.
Sort and iterate over this array to get the proper value of nodes.
Create a new sorted linked list and extend it with the new nodes.


Time complexity : O(NlogN) where NN is the total number of nodes.

                    Collecting all the values costs O(N) time.
                    A stable sorting algorithm costs O(NlogN) time.
                    Iterating for creating the linked list costs O(N) time.

Space complexity : O(N).

                    Sorting cost O(N) space (depends on the algorithm you choose).
                    Creating a new linked list costs O(N) space

'''

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next


'''

APPROACH 2: USING HEAP/PRIORITY QUEUE

Algorithm

Compare every k nodes (head of every linked list) and get the node with the smallest value.
Extend the final sorted linked list with the selected nodes.



Example:

1 -> 3 -> 5
1 -> 4
1 -> 3 -> 6 -> 8

we sort our minheap using the root value of each independent linkedlist, cos the root is the smallest in the LL

minHeap = [1 -> 3 -> 5, 1 -> 4, 1 -> 3 -> 6 -> 8]

to build our LL result, we need to know what .next to add. So we pop the first thing in our minHeap, which is 
1 -> 3 -> 5.

so we just take the root and push it remaining back into the mean heap, which will automatically just resort it self.

so we just pop and ppend to our tail ad continue like that

N - cmbined length of all the lists.

Time complexity : O(Nlogk) where k is the number of linked lists.

                The comparison cost will be reduced to O(logk) for every pop and insertion to priority queue. But finding the node with the smallest value just costs O(1) time.
                There are N nodes in the final linked list.

Space complexity :

                O(n) Creating a new linked list costs O(n)O(n) space.

                heap is O(k) cos the list wil always have k items The code above present applies in-place method which cost O(1) space


'''

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
                #pushing to our minheap array and sort by the index val
                # providing the root val, index and root because i will need the other values later
                # (what to sort by, alternate to sort by if the what to sort by is the same, root so we can always pop it and get the next node) 
                heappush(minHeap, (root.val, idx,  root))
                
                
        # Take the smallest(top) element from the minheap and add to result
        # if the top element has a next element, add to heap
        # based on the sort we add it to the .next and byuild a new linked list
        resultHead, resultTail = None, None
        
        while minHeap:
            nodeVal, idx, node = heappop(minHeap)
            # print(nodeVal, resultHead)
            if resultHead is None:
                resultHead = resultTail = node
            else:
                resultTail.next = node
                resultTail = resultTail.next
                
            if node.next is not None:
                heappush(minHeap, (node.next.val, idx, node.next))
                
        return resultHead