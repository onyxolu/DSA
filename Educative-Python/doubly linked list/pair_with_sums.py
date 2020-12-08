def pairs_with_sum(self, sum_val):
  pairs = list()
  p = self.head 
  q = None 
  while p:
    q = p.next
    while q:
      if p.data + q.data == sum_val:
          pairs.append("(" + str(p.data) + "," + str(q.data) + ")")
      q = q.next
    p = p.next
  return pairs