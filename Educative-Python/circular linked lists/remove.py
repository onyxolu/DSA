def remove(self, key):
  if self.head:
    if self.head.data == key:
      cur = self.head 
      while cur.next != self.head:
        cur = cur.next 
      if self.head == self.head.next:
        self.head = None
      else:
        cur.next = self.head.next
        self.head = self.head.next
    else:
      cur = self.head 
      prev = None 
      while cur.next != self.head:
        prev = cur 
        cur = cur.next
        if cur.data == key:
          prev.next = cur.next 
          cur = cur.next