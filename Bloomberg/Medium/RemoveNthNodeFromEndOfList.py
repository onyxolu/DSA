

class Solution:
    	    # fast = slow = head #Initialising both fast and slow to head
        #we are making Fast to point to the node which is right next to the node which is to be removed
	def removeNthFromEnd(self, head, n: int):
        fast = slow = head
        for i in range(n):
            fast = fast.next 
        
        if fast is None: 
            return head.next 
        
        while fast.next:
            fast = fast.next  #After this we are increasing both fast and head by 1 step each
            slow = slow.next
        
        #when fast reaches end of the list, slow points to the node behind the target, so we skip the target and move to next of target

        slow.next = slow.next.next 
        return head