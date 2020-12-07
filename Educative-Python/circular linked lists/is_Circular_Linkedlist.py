def is_circular_linked_list(self, input_list):
  cur = input_list.head
  while cur.next:
    cur = cur.next
    if cur.next == input_list.head:
      return True
  return False