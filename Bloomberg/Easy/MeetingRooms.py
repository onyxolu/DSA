
# sort and find overlapping

class Solution:
    def canAttendMeetings(self, intervals):
        if len(intervals) < 2:
            return True
        
        intervals.sort(key=lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        canAttend = True
        
        for i in range(1,len(intervals)):
            cur_start, cur_end = intervals[i]
            if cur_start < end:
                return False
            else:
                start = cur_start
                end = cur_end
                
        return canAttend