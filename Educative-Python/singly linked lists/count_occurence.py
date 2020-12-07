def count_occurences_iterative(self, data):
  count = 0
  cur = self.head
  while cur:
      if cur.data == data:
          count += 1
      cur = cur.next
  return count 