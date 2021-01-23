# BST
# BST PROP NOdes Val Less than nodes val in rigth and greater than or = to node val in left

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Time - Average Case 0(LogN) Worst Case 0(N)
    # Space - Average Case 0(1) Worst Case 0(1)
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                currentNode = currentNode.left

            elif value >= currentNode.value:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                currentNode = currentNode.right 

        return self

    # Time - Average Case 0(LogN) Worst Case 0(N)
    # Space - Average Case 0(1) Worst Case 0(1)
    def search(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left

            elif value >= currentNode.value:
                currentNode = currentNode.right 
            
            else:
                return True

        return False

    
    # Time - Average Case 0(LogN) Worst Case 0(N)
    # Space - Average Case 0(1) Worst Case 0(1)
    def delete(self, value, parentNode = None):
        currentNode = self    
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left

            elif value >= currentNode.value:
                parentNode = currenNode
                currentNode = currentNode.right

            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)

                elif parentNode is None:

                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left

                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.right = currentNode.right.right
                        currentNode.left = currentNode.right.left

                    else:
                        currentNode.value = None

                elif parentNode.left = currentNode:
                    parentNode.left = currentNode.left is currentNode.left is not None else currentNode.right

                elif parentNode.right = currentNode:
                    parentNode.right = currentNode.left is currentNode.left is not None else currentNode.right
                break


    
    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value