
from collections import defaultdict, List, random
# Hashmap

class Solution:

    def __init__(self, nums: List[int]):
        self.index_dict = defaultdict(list)
        
        for i, num in enumerate(nums):
            self.index_dict[num].append(i)

    def pick(self, target: int) -> int:
        index_list = self.index_dict[target]
        return random.choice(index_list)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)