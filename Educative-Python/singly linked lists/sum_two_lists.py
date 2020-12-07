def sum_two_lists(self, llist):
  p = self.head  
  q = llist.head

  sum_llist = LinkedList()

  carry = 0
  while p or q:
      if not p:
          i = 0
      else:
          i = p.data
      if not q:
          j = 0 
      else:
          j = q.data
      s = i + j + carry
      if s >= 10:
          carry = 1
          remainder = s % 10
          sum_llist.append(remainder)
      else:
          carry = 0
          sum_llist.append(s)
      if p:
          p = p.next
      if q:
          q = q.next
  return sum_llist