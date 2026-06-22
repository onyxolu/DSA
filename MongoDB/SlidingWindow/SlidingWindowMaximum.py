from typing import List
from collections import deque

# Clarify: window_size always ≤ len(numbers)? array can have negative numbers/duplicates?
# Key insight: monotonic decreasing deque of INDICES — front is always the current max
#
# Volunteer before being asked:
#   - Naive: scan all k elements per window → O(n×k), too slow for large k
#   - Optimal: deque holds only "candidates that could still be the max" — pop smaller
#     values from back since they're useless once a bigger value enters the window
#   - Store indices not values → needed to know when an index falls outside the window
#   - Real world: real-time max tracking in streaming data, stock price rolling max

class Solution:
    def maxSlidingWindow(self, numbers: List[int], window_size: int) -> List[int]:
        result = []
        decreasing_deque = deque()                      # stores indices, decreasing by value
        left_pointer = 0

        for right_pointer in range(len(numbers)):
            # pop smaller values from back — they can never be the max anymore
            while (decreasing_deque and
                   numbers[decreasing_deque[-1]] < numbers[right_pointer]):
                decreasing_deque.pop()

            decreasing_deque.append(right_pointer)

            # remove front if it's fallen outside the window
            if decreasing_deque[0] < left_pointer:
                decreasing_deque.popleft()

            # window is full → record the max (front of deque)
            if right_pointer + 1 >= window_size:
                result.append(numbers[decreasing_deque[0]])
                left_pointer += 1

        return result

# Edge cases:
#   window_size == len(numbers) → single result, the global max
#   window_size == 1 → result equals input array unchanged
#   all same values → deque always holds just one index (newest), since none are "smaller"

# Complexity:
#   time  → O(n) — each index pushed and popped from deque at most once
#   space → O(k) — deque never holds more than window_size indices

# Follow-ups:
#   Why indices not values? → need to detect when the max has "expired" (fallen outside window)
#   Why is this O(n) and not O(n×k)? → amortized analysis — each element added/removed once total
#   Sliding window minimum instead? → same pattern, flip the comparison to increasing deque
#   Real world: rolling max/min in monitoring dashboards, max in last N stock ticks