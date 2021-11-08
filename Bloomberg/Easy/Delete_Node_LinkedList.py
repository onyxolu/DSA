

class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

    def delete(self, node):
        if node is None:
            return None
        if node.next:
            # copy the value of next node
            node.val = node.next.val
            # erase the next node
            node.next = node.next.next