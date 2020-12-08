  def add_after_node(self, key, data):
    cur = self.head
    while cur:
      if cur.next is None and cur.data == key:
        self.append(data)
        return
      elif cur.data == key:
        new_node = Node(data)
        nxt = cur.next 
        cur.next = new_node
        new_node.next = nxt
        new_node.prev = cur 
        nxt.prev = new_node
        return
      cur = cur.next

  def add_before_node(self, key, data):
    cur = self.head 
    while cur:
      if cur.prev is None and cur.data == key:
        self.prepend(data)
        return
      elif cur.data == key:
        new_node = Node(data)
        prev = cur.prev
        prev.next = new_node
        cur.prev = new_node
        new_node.next = cur
        new_node.prev = prev
        return
      cur = cur.next