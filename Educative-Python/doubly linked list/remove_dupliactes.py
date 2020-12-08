def delete_node(self, node):
  cur = self.head
  while cur:
    if cur == node and cur == self.head:
      # Case 1:
      if not cur.next:
        cur = None 
        self.head = None
        return

      # Case 2:
      else:
        nxt = cur.next
        cur.next = None 
        nxt.prev = None
        cur = None
        self.head = nxt
        return 

    elif cur == node:
      # Case 3:
      if cur.next:
        nxt = cur.next 
        prev = cur.prev
        prev.next = nxt
        nxt.prev = prev
        cur.next = None 
        cur.prev = None
        cur = None
        return

      # Case 4:
      else:
        prev = cur.prev 
        prev.next = None 
        cur.prev = None 
        cur = None 
        return 
    cur = cur.next


def remove_duplicates(self):
  cur = self.head 
  seen = dict()
  while cur:
    if cur.data not in seen:
      seen[cur.data] = 1
      cur = cur.next
    else:
      nxt = cur.next
      self.delete_node(cur)
      cur = nxt