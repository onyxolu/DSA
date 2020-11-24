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

  def swap(self, index1, index2):
    cur_node = self.head
    node1 = {}
    node2 = {}
    if index1 == 0:
        print('HIi')
        node1["prev"] = None
        node1["cur"] = self.head

    if index2 == 0:
        node2["prev"] = None
        node2["cur"] = self.head

    i = 1
    while cur_node:
        if i == index1:
            print("index1", cur_node.next.data)
            node1["prev"] = cur_node
            node1["cur"] = cur_node.next

        if i == index2:
            print("index2", cur_node.next.data)
            node2["prev"] = cur_node
            node2["cur"] = cur_node.next
        cur_node = cur_node.next
        i += 1
    
    if node1["prev"]:
        node1["prev"].next = node2["cur"]
    else:
        # node1["cur"] = node2["cur"]
        print("cur", node1["cur"].data)
        self.head = node2["cur"]

    if node2["prev"]:
        node2["prev"].next = node1["cur"]
    else: 
        self.head = node1["cur"]

    node1["cur"].next, node2["cur"].next = node2["cur"].next, node1["cur"].next           

 


 






list1 = LinkedList()
list1.append(5)
list1.append(4)
list1.append(3)
list1.append(2)
list1.append(1)
# list1.print_list()
list1.swap(4,0)
list1.print_list()

# list1.length()