
# BFS

Time = 0(10^4 * 4^2)
Space = 0(10^4 * 4) # queue and set

# See it as start date and end date, "0000" - "0230"

from collections import deque

class Solution:
    def openLock(self, deadends, target: str) -> int:
        deadSet = set(deadends)
        
        if "0000" in deadSet:
            return -1
        queue = deque(["0000"])
        ans = 0
        seen = set()
        seen.add("0000")
        
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                
                if cur == target:
                    return ans
                
                for i in range(4):
                    newDigit1 = (int(cur[i]) + 1) % 10
                    newCode1 = cur[:i] + str(newDigit1) + cur[i+1:]
                    
                    if newCode1 not in seen and newCode1 not in deadSet:
                        queue.append(newCode1)
                        seen.add(newCode1)
                        
                    newDigit2 = (int(cur[i]) + 10 - 1) % 10
                    newCode2 = cur[:i] + str(newDigit2) + cur[i+1:]
                    
                    if newCode2 not in seen and newCode2 not in deadSet:
                        queue.append(newCode2)
                        seen.add(newCode2)
                        
                    # print(newDigit1, newCode1, newDigit2, newCode2)
                    # 1 1000 9 9000
                    # 1 0100 9 0900
                    # 1 0010 9 0090
                    # 1 0001 9 0009
                    # 2 2000 0 0000
                    # 1 1100 9 1900
                    # 1 1010 9 1090
                    # 1 1001 9 1009
                    # 0 0000 8 8000
                    # 1 9100 9 9900
                    # 1 9010 9 9090
                    # 1 9001 9 9009
                    # 1 1100 9 9100
                    # 2 0200 0 0000
                    # 1 0110 9 0190
                    # 1 0101 9 0109
                    # 1 1900 9 9900
                    # 0 0000 8 0800
                        
            ans += 1
        return -1