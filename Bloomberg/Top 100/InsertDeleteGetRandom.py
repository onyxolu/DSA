
# Hashmap and list
# list to keep track of index and hashmap to keep track of uniqueness

import random


class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            # move the last element to the place idx of the element to delete
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            # delete the last element
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)

 # Hash set


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
