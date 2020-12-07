class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, data):
    cur_node = self.head
    new_node = Node(data)
    if cur_node is None:
      self.head = new_node
      return
    while cur_node.next:
      cur_node = cur_node.next
    cur_node.next = new_node

  def print_list(self):
    cur_node = self.head
    while cur_node:
      print(cur_node.data) 
      cur_node = cur_node.next

  def length(self):
    cur_node = self.head
    length = 0
    while cur_node:
      length+=1
      cur_node = cur_node.next
    print(length)

  def merge(self, llist):
    p = self.head
    q = llist.head
    s = None
    if not p:
        return q
    if not q:
        return p
    # new_head = s
    if p and q:
        if p.data <= q.data:
            s = p
            p = p.next
        else:
            s = q
            q = q.next
    while p and q:
        if p.data <= q.data:
            s.next = p 
            s = p
            p = p.next
        else:
            s.next = q
            s = q
            q = q.next
    if not p:
        s.next = q
    if not q:
        s.next = p
    
    # return new_head
    



list1 = LinkedList()
list2 = LinkedList()
list1.append(1)
list1.append(5)
list1.append(7)
list2.append(2)
list2.append(4)
list2.append(6)
print(list1.print_list())
print(list2.print_list())
list1.merge(list2)
print(list1.print_list())
