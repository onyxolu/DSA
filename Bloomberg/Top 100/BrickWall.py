

class Solution:
    def leastBricks(self, wall) -> int:
        countGap = {0: 0} # matching pos: count of brick gaps
        
        for r in wall:
            total = 0 #  To know the current position we're at
            for b in r[:-1]: # skip the last one
                total += b
                countGap[total] = 1 + countGap.get(total, 0) # increment pos with no of brick walls
                
        return len(wall) - max(countGap.values())
        