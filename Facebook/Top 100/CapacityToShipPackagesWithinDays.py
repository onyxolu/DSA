from collections import List 

# Binary search

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):# remember, we can only ship from left to right
            days_needed = 1 # atleast we will be needing 1
            cur_weights = 0
            
            for w in weights:
                cur_weights += w
                
                if cur_weights > capacity:
                    days_needed += 1
                    cur_weights = w
            return days_needed <= days
                    
        left = max(weights) # so we can atleast ship all the weights in our capacity
        right = sum(weights)
        print(left, right) # 10,55
        
        while left < right:
            mid = left + (right - left) // 2
            print(left, right,mid)
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
                
        return left
                