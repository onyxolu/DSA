# Good thing is , It's in reverse

#  carry 1
# 5-6-4
# 4-4-3-3
# --------
# 9 0 8 3 
# --------

# edge case


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        cur = dummy = ListNode()
        
        carry = 0
        while l1 or l2 or carry:  # or carry to handle test  case 8+7
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # add New digit
            val = val1 + val2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            
            # update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next

    def addTwoNumbers2_1(self, l1, l2):
        num1, num2 = 0,0
        
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
            
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
            
        numSum = num1 + num2
        dummy = head = ListNode()
        
        if numSum == 0:
            return head
        
        while numSum > 0:
            head.next = ListNode(numSum % 10)
            head = head.next
            numSum //= 10
            
        # reverse linked list
        prev = None
        head = dummy.next
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
            
        return prev



    def addTwoNumbers2(self, l1, l2):
        num1, num2 = 0,0
        
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
            
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
            
        numSum = num1 + num2
        dummy = head = ListNode()
        
        if numSum == 0:
            return head
        
        while numSum > 0:
            head.next = ListNode(numSum % 10, head.next)
            numSum //= 10
            
        return dummy.next