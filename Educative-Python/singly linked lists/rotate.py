def rotate(self, k):
  if self.head and self.head.next:
    p = self.head 
    q = self.head 
    prev = None
    count = 0
    
    while p and count < k:
        prev = p
        p = p.next 
        q = q.next 
        count += 1
    p = prev
    while q:
        prev = q 
        q = q.next 
    q = prev 

    q.next = self.head 
    self.head = p.next 
    p.next = None