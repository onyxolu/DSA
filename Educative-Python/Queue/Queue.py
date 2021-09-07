# Using Class

# class queue():
#     def __init__(self) -> None:
#         self.items = [];

#     def push(self, val):
#         self.items.append(val)

#     def pop(self):
#         self.items.pop(0)

#     def peek(self):
#         self.items[-1]


# => insert 0(N)
 

# => remove 0(N)




# Using Deque


from collections import deque

queue1 = deque()

queue1.append("a")
queue1.append("b")
queue1.append("c")

queue1.popleft()

print(queue1)

# => insert 0(1)
 

# => remove 0(1)

