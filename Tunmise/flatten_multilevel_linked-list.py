class Node:
    def __init__(self,val,prev,next,child):
        
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        dummy = prev = Node(0,None,None,None)
        stack = [head]
        while stack:
            c = stack.pop()
            curr = Node(c.val,prev,None,None)
            prev.next = curr
            prev = prev.next

            if c.next:
                stack.append(c.next)
            if c.child:
                stack.append(c.child)
        dummy = dummy.next
        dummy.prev = None
        return dummy
