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

  def prepend(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node    

  def insert_after_node(self, prev_node, data):
    if not prev_node:
      print("previous node does not exist")
      return
    
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

list1 = LinkedList()
list1.append(5)
list1.append(4)
list1.append(3)
list1.append(2)
list1.append(1)
list1.prepend(6)
list1.insert_after_node(list1.head.next.next, 5)
print(list1.print_list())