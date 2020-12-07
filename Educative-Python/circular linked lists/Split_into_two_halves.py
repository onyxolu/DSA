def split_list(self):
    size = len(self)    

    if size == 0:
        return None
    if size == 1:
        return self.head

    mid = size//2
    count = 0

    prev = None
    cur = self.head

    while cur and count < mid:
        count += 1
        prev = cur
        cur = cur.next
    prev.next = self.head 

    split_cllist = CircularLinkedList()
    while cur.next != self.head:
        split_cllist.append(cur.data)
        cur = cur.next
    split_cllist.append(cur.data)

    self.print_list()
    print("\n")
    split_cllist.print_list()