import random

class RandomizedSet:

    def __init__(self):
        self.hashset = set()

    def insert(self, val: int) -> bool:
        if val in self.hashset:
            return False
        self.hashset.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.hashset:
            self.hashset.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.hashset))
