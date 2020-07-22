class node:
  def __init__(self, data = None):
    self.data = data
    self.next = None

class linked_list:
  def __init__(self):
    self.head = node()

  def append(self, data):
    new_node = node(data)
    cur = self.head
    while cur.next != None:
      cur = cur.next
    cur.next = new_node

  def length(self):
    cur = self.head
    total = 0
    while cur.next != None:
      total +=1
      cur = cur.next
    print(total)
    return total

  def display(self):
    cur = self.head
    item = []
    while cur.next != None:
      val = cur.next.data
      item.append(val)
      cur = cur.next
    print(item)
  
  def get(self, index):
    if index >= self.length():
      print("Index Out of range")
    cur = self.head.next
    cur_idx = 0
    while cur.next != None:
      if(cur_idx == index):
        print(cur.data)
        return
      cur = cur.next
      cur_idx +=1

  def erase(self, index):
    if index >= self.length():
      print("Index Out of range")
    cur = self.head.next
    cur_idx = 0
    while True:
      print("hiii")
      last_node = cur
      cur = cur.next
      if(cur_idx == index):
        cur.next = last_node.next
        print("nawaooo")
        break
        return
      cur_idx +=1

my_list = linked_list()

my_list.append(5)
my_list.append(4)
my_list.append(100000)
my_list.append(300000)
my_list.append(400000)

my_list.length()
my_list.display()
my_list.erase(1)
my_list.display()

