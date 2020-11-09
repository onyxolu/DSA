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

  def delete_node(self, pos):
    # print(self.head.data)
    cur_node = self.head
    if cur_node and pos == 0:
      self.head = self.head.next
      return

    count = 1
    while cur_node.next:
      if count == pos:
        cur_node.next = cur_node.next.next
        if not cur_node.next:
          return
      cur_node = cur_node.next
      count += 1

    

list1 = LinkedList()
list1.append(5)
list1.append(4)
list1.append(3)
list1.append(2)
list1.append(1)
list1.delete_node(2)
list1.delete_node(0)
# list1.delete_node(5)
print(list1.print_list())