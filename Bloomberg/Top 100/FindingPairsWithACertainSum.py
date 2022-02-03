
# Hashmap + list
from collections import Counter

class FindSumPairs:

    def __init__(self, nums1, nums2):
        self.n1, self.n2 = Counter(nums1), Counter(nums2)
        self.n = [i for i in nums2]

    def add(self, index: int, val: int) -> None:
        self.n2[self.n[index]] -= 1 # Remove the element from the dict
        self.n[index] += val # Add the val to the given index
        self.n2[self.n[index]] += 1 # add the (elem+val) to the dictionary

    def count(self, tot: int) -> int:
        res = 0
        for j in self.n1:
            if tot - j in self.n2: # found a pair
                res += self.n2[tot - j] * self.n1[j] 
        return res
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)