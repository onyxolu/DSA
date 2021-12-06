
from collections import List

# stack
# Use a stack to keep track of unfinished functions
# call stack [] => [0] => [0,1]
# Time Spent [0,0]

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ftimes = [0] * n
        stack = []  # the ids of function calls
        prev_start_time = 0
        
        for log in logs:
            fid, typ, ftime = log.split(':')
            fid, ftime = int(fid), int(ftime)
            
            if typ == 'start':
                if stack:
                    ftimes[stack[-1]] += ftime - prev_start_time
                stack.append(fid)
                prev_start_time = ftime
            else:
                ftimes[stack.pop()] += ftime - prev_start_time + 1
                prev_start_time = ftime + 1
                
        return ftimes
        