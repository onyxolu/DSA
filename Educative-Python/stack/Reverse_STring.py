class stack:
  def __init__(self):
    self.arr = []

  def push(self, item):
    self.arr.append(item)

  def pop(self):
    return self.arr.pop()

  def peek(self):
    return self.arr[-1]

  def isEmpty(self):
    if self.arr == []:
      return True
    else:
      return False

  def getArr(self):
    print(self.arr)
    return self.arr

  def reverseString(self,str):
    for val in str:
      self.push(val)

    reversedString = ""

    while not self.isEmpty():
      reversedString += self.pop()

    return reversedString

    
newStack = stack()
print(newStack.reverseString("!evitacudE ot emocleW"))