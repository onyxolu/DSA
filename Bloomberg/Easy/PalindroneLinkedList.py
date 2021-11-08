class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    # using string
    def isPalindrone(self, head):
        s = ""
        p = head
        while p:
            s += str(p.val)
            p = p.next
        return s == s[::-1]

    def isPalindromeQueue(self, head):
        slow=head
        from collections import deque
        queue=deque()
        while slow:
            queue.append(slow.val)
            slow=slow.next
        while len(queue)>1:
            if queue.popleft()==queue.pop():
                continue
            else:
                return False
        return True