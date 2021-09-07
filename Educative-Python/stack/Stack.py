
# using class 


class stack():
    def __init__(self):
        self.item = []

    def push(self, val):
        self.append(val)

    def pop(self):
        self.pop()

    def isEmpty(self):
        if self.item == []:
            return True
        else:
            return False

    def peek(self):
        return self.items[-1]

    
    

# => Lookup 0(1)


# => Search 0(N)


# => insert 0(N)
 

# => remove 0(N)



# Using deque

from collections import deque

stack = deque()

stack.append("a")
stack.append("b")
stack.append("c")

stack.pop()

print(stack)

# => insert 0(1)
 

# => remove 0(1)

