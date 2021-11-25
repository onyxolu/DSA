
# bruteforce : create an additional linkedlist, make the next of our curr node the next of our copy, and then set our current to the next of our copy. 
# time : O(n) space : O(n)

# reduce space by using only 3 pointers : curr, next, nextcurr.
# starting at our head : 
#     curr = head
#     next = curr.next
#     nextCurr = next.next

# then we can set next.next to curr, then curr.next to nextCurr.

# we set curr to nextCurr, and repeat 7-9

# time : O(n), space O(1)

# [2,1,4,3]

# curr = None
# next = None
# nextcurr = None

# head = 1

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        curr = head
        nextNode = curr.next
        nextCurr = nextNode.next
        
        head = nextNode
        
        while nextNode is not None:
            nextNode.next = curr # what if nextNOde is none
            if nextCurr is None or nextCurr.next is None:
                curr.next = nextCurr
                break
            curr.next = nextCurr.next
            curr = nextCurr
            nextNode = curr.next
            nextCurr = nextNode.next
            
        
        return head