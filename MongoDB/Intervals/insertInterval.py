from typing import List

# Clarify: guaranteed sorted by start? touching intervals overlap? expected scale?
# Key advantage over Merge Intervals: already sorted → skip sort → O(n) vs O(n log n)

# Approach: Single Pass — O(n) time | O(1) space (excluding output)
# 3 cases based on position of newInterval relative to current interval
#
# Volunteer before being asked:
#   - Empty intervals → append newInterval and return
#   - newInterval before all → prepend and return
#   - newInterval after all → append at end (handled by res.append after loop)
#   - Large input on disk → already sorted, stream one interval at a time, same 3 cases
#   - vs Merge Intervals: no sort needed here → O(n) not O(n log n)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # case 1:Insert Before => newInterval ends before current starts → insert, return rest
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            # case 2:Insert After newInterval starts after current ends → current comes first
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # case 3: overlap → merge, keep expanding newInterval
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        res.append(newInterval)  # handles: no case 1 hit, or last interval merged
        return res

# Edge cases:
#   [] → [newInterval]
#   newInterval before all → [newInterval] + intervals
#   newInterval after all → intervals + [newInterval]
#   newInterval overlaps all → [merged single interval]

# Scale decision guide:
#   Small in-memory        → this solution, O(n) time
#   Large on disk          → stream intervals one at a time, same 3 cases (no sort needed)
#   Unsorted large input   → external merge sort first, then stream + this logic
    

# Binary Search

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        n = len(intervals)
        target = newInterval[0]
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1

        intervals.insert(left, newInterval)

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res