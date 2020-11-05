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

  def getBinary(self,num):
    if num == 0:
      return 0

    while num > 0:
      print(num//2)
      self.push(str(num%2))
      num = int(num/2)
    
    self.push(str(num%2))

    binValue = ""
    while not self.isEmpty():
      print(self.getArr())
      binValue += self.pop() 

    return binValue 


    
newStack = stack()
print(newStack.getBinary(242))