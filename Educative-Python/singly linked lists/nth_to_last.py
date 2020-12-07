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
    return length

  def print_nth_from_last(self, n):
    total_len = self.length()
  
    cur = self.head 
    while cur:
        if total_len == n:
            print(cur.data)
            return cur.data
        total_len -= 1
        cur = cur.next
    if cur is None:
        return  