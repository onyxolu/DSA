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
    return length

  def remove_duplicates(self):
    cur_node = self.head
    prev_node = None
    seen = []
    while cur_node:
        if cur_node.data in seen:
            prev_node.next = cur_node.next
        else:
            seen.append(cur_node.data)
            prev_node = cur_node
        cur_node = prev_node.next

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
        




list1 = LinkedList()
list1.append(5)
list1.append(4)
list1.append(3)
list1.append(2)
list1.append(1)
list1.append(4)
list1.append(1)

print(list1.print_nth_from_last(4))