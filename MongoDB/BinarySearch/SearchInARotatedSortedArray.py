from typing import List

# Clarify: distinct values? always rotated or could be fully sorted? return index or value?
# O(log n) required → binary search with rotation awareness
#
# Key insight: at any midpoint, one side is ALWAYS fully sorted
# Use that to determine if target falls within the sorted side
#
# Volunteer before being asked:
#   - nums[l] <= nums[mid] → left side sorted (handles non-rotated case too)
#   - Check if target in sorted range → if yes search there, if no search other side
#   - Single element → while loop handles it naturally
#   - Real world: searching in circular buffers, rotated logs, ring queues

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                # target outside left range → search right
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            # right sorted portion
            else:
                # target outside right range → search left
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

# Edge cases:
#   single element → returns it or -1
#   not rotated → nums[l] <= nums[mid] always true, behaves like normal binary search
#   target not in array → returns -1
#   rotation at index 0 → not rotated, handled naturally

# Complexity:
#   time → O(log n)
#   space → O(1)

# Follow-ups:
#   Find the pivot index → same binary search, find where nums[mid] > nums[mid+1]
#   Array has duplicates → nums[l] == nums[mid] is ambiguous → l++ to skip, worst O(n)
#   Large array on disk → can't do binary search without random access → need index