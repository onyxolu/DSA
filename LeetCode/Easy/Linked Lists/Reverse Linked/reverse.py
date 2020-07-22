# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
          # recurse all the way to end and then begin to flip pointers
        def reverse(head):
            if head is None or head.next is None:
                return head
            
            reversed_ll = reverse(head.next)
            
            # set 5 pointer to me, so reversed ll now has me in the ll
            head.next.next = head
            # set my pointer to None so in next stack fram it doesnt
            # have the remaining list
            head.next = None
            
            return reversed_ll
        
        return reverse(head)
        