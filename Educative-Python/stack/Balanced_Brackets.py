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

  def checkOpenBracket(self,item):
    if item in "({[":
      return True
    else:
      return False


  def checkForMatch(self, item1, item2):
    print(item1, item2)
    if item1 == "(" and item2 == ")":
      return True
    if item1 == "{" and item2 == "}":
      return True
    if item1 == "[" and item2 == "]":
      return True
    else:
      return False

  def checkBalanced(self, str):
    index = 0
    isBalanced = True
    while index < len(str) and isBalanced:
      currentItem = str[index]
      if self.checkOpenBracket(currentItem):
        self.push(currentItem)
      else:
        if self.isEmpty():
          print(currentItem, "false first check")
          isBalanced = False
        else: 
          top = self.pop()
          if not self.checkForMatch(top, currentItem):
            isBalanced = False
            print(currentItem, "false second check")
      index = index + 1
    
    if self.isEmpty and isBalanced:
      return  True
    else:
      return False



newStack = stack()
print(newStack.checkBalanced("(((({}))))"))