
# sort and check for overlapping (then merge them)

class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals
        
        intervals.sort(key = lambda x: x[0])
        mergeIntervals = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            cur_start , cur_end = interval[0], interval[1]
            if cur_start <= end: # merge
                end = max(cur_end, end)
            else:
                mergeIntervals.append([start, end])
                start = cur_start
                end = cur_end
                
        mergeIntervals.append([start, end])
        return mergeIntervals