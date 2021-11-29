# Two Pointers

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Brute force => use first LL in set and loop second ll to find if it is in set the return node
        # Optimal => Two pointers
        
        curA, curB = headA, headB
        a,b = 0,0
        
        # get the length of a
        while curA:
            a+=1
            curA = curA.next
        # get the length of b
        while curB:
            b+=1
            curB = curB.next
            
        # determine which is longer and get the difference
        if a>b:
            curL = headA # curL longer
            diff = a-b
            curS = headB
        else: #a<b
            curL = headB
            diff = b-a
            curS = headA
            
        # move to where curS starts
        i=0
        while i < diff:
            i += 1
            curL = curL.next
            
        # find intersect
        while curL != curS:
            curL = curL.next
            curS = curS.next
            
        return curL