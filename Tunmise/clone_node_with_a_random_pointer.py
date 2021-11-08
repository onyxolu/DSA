"""Approach 1 (Linear Space Solution)

Use a hashtable to facilitate the cloning.

Complexities

Time: O( n )

We will perform linear time traversals that keep our asymptotic behavior linear.

Space: O( n )

We will store a clone mapping for each node entailing linear space complexity with respect to the original list passed to us.


Approach 2 (Constant Space Solution)

Use the original list's node's next pointer to map to the clone list.

Complexities

Time: O( n )

We are still only doing linear time traversals

Space: O( 1 )

We do not store any auxiliary space that will scale as the input size gets arbitrarily large.
"""
class Node:
    def __init__(self,val,nxt,rand):
        val = val
        nxt = next
        rand = rand

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        curr = head
        while curr:
            next = curr.next
            clone = Node(curr.val)
            clone.next = curr.next
            curr.next = clone
            curr = next
            
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        curr = head
        dummy = clone = Node(-1)
        while curr:
            next = curr.next.next
            copy = curr.next
            clone.next = copy
            clone = clone.next
            curr = next
            
        return dummy.next
            
            
            
#         if not head:
#             return None
        
#         d = dict()
#         curr = head
#         while curr:
#             d[curr] = Node(curr.val)
#             curr = curr.next
            
#         curr = head
#         while curr:
#             clone_node = d[curr]
#             if curr.next:
#                 clone_node.next = d[curr.next]
#             if curr.random:
#                 clone_node.random = d[curr.random]
#             curr = curr.next
            
#         return d[head]