import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = dict()
        self.l = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.map:
            self.l.append(val)
            self.map[val] = len(self.l)-1
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.map:
            idx_to_deleted = self.map[val]
            #swap the postition of the value to be deleted with the last element in the array
            self.l[idx_to_deleted],self.l[-1]=self.l[-1],self.l[idx_to_deleted]
            #update its value of the swapped last position in the hashmap
            self.map[self.l[idx_to_deleted]] = idx_to_deleted
            #pop the last element(which is the element to be deleted) from the list and from the dictionary
            del self.map[self.l.pop()]
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.l)