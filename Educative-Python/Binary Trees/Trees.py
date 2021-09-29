
class Node():
    def __init__(self, data) -> None:
        self.value = data;
        self.left = None;
        self.left = None;

class Tree():
    def __init__(self) -> None:
        self.root = None;


BT = Tree()
BT.root = Node(5)
BT.root.left = Node(4)
BT.root.right = Node(5)