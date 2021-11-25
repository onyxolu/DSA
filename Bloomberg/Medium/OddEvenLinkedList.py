

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if head:
            
            # Assign odd
            odd = head
            
            # Assing even and it's head
            even_head = even = head.next
            
            # Loop till there are two consecutive elements
            while even and even.next:
                # First element connects to third element
                odd.next = even.next
                # First element becomes third element
                odd = odd.next
                # Second element connects to fourth element
                even.next = odd.next
                # Second element becomes fourth element
                even = even.next
                
            # Third elemenet connects to second element    
            odd.next = even_head
            
        return head