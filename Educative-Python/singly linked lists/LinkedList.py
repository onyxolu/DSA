
# node => node2 => node3

# node {data, next}

# llist {head}


class Node():
    def __init__(self, data) -> None:
        self.data = data;
        self.next = None;

    
class lList():
    def __init__(self) -> None:
        self.head = None;

    def append(self, data):
        cur_node = self.head;
        new_node = Node(data)
        if self.head is None:
            self.head = new_node;
            return
        while cur_node.next:
            cur_node = cur_node.next;
        cur_node.next = new_node;

    def print_list(self):
        arr = [];
        cur_node = self.head;
        if self.head is None:
            return [];
        while cur_node:
            arr.append(cur_node.data);
            cur_node = cur_node.next
        print(arr)

    def prepend(self, data):
        cur_node = self.head;
        new_node = Node(data);
        new_node.next = self.head;
        self.head = new_node;

    def find_by_index(self,idx):
        pos = 0;
        cur_node = self.head
        while cur_node:
            if idx == pos:
                print(cur_node.data)
                return 
            cur_node = cur_node.next
            pos += 1
        print("index not found")

    def delete_by_index(self,idx):
        pos = 0;
        cur_node = self.head
        while cur_node:
            if idx == 0:
                self.head = cur_node.next
                return
            if pos + 1 == idx :
                # prev_node = cur_node
                cur_node.next = cur_node.next.next
                return 
            cur_node = cur_node.next
            pos += 1
        print("index not found")
        
        




list1 = lList()
list1.append(5)
list1.append(6)
list1.append(7)
list1.prepend(8)
list1.delete_by_index(0)

list1.print_list()


# => insert 0(N)
 

# => remove 0(N)


# Using Collections

# => insert 0(1)
 

# => remove 0(1)
        
    
    

