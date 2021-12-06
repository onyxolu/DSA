from collections import List, random

# prefixSum + Binary Search

# Prefix sum then we can do linear search
# But then linear search is 0(N)
# We can do better, we can use binary search 0(LogN)


class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sum.append(prefix_sum)
        self.total_sum = prefix_sum
        

    def pickIndex(self) -> int:
        random_num = self.total_sum * random.random() # random will give you a value from 0 to 1
        low,high = 0, len(self.prefix_sum)
        while low < high:
            mid = low + (high - low) // 2
            if random_num > self.prefix_sum[mid]:
                low = mid + 1
            else:
                high = mid
        return low
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()