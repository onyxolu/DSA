from typing import List

# Clarify: intervals sorted? touching intervals count as overlapping? expected scale?
# Scale answer → sort + single pass (small) | external merge sort (huge)

# Approach: Sort + Single Pass — O(n log n) time | O(1) space (in-place sort, excluding output)
# Volunteer: empty/single interval → return as is
#            unsorted input → sort first by start time (always assume unsorted)
#            intervals on disk → external merge sort, same merge logic applies

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])      # sort by start time
        res = [intervals[0]]

        for start, end in intervals[1:]:         # start from index 1
            lastEnd = res[-1][1]

            if start <= lastEnd:                 # overlapping or touching
                res[-1][1] = max(lastEnd, end)   # extend end, don't assume end > lastEnd
            else:
                res.append([start, end])         # no overlap, append as is

        return res

# Edge cases:
#   [] → []
#   [[1,4]] → [[1,4]]
#   [[1,4],[4,5]] → [[1,5]]  (touching = overlapping)
#   [[1,4],[2,3]] → [[1,4]]  (fully contained, max handles this)

# Decision guide:
#   Small in-memory    → this solution
#   Huge on disk       → external merge sort → stream sorted chunks → same merge logic