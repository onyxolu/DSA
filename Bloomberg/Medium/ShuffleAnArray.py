
# Fisher Yates Algorithm
import random

class Solution:

    def __init__(self, nums):
        self.original = nums
        

    def reset(self):
        return self.original
        

    def shuffle(self):
        # Fisher Yate's Algorithm
        # Start from the last element and swap one by one. We don't
        # need to run for the first element that's why i > 0
        arr = self.original[:]
        n = len(arr)
        for i in range(n-1,0,-1):
            # Pick a random index from 0 to i
            j = random.randint(0,i)

            # Swap arr[i] with the element at random index
            arr[i],arr[j] = arr[j],arr[i]
        return arr
        