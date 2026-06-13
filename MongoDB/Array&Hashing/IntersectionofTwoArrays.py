from typing import List

# ─── Senior clarifying questions (ask before coding) ─────────────────
#
# 1. "Should the result ignore duplicates?"
# 2. "Is an empty array a valid return if there's no intersection?"
# 3. "Can I modify the input arrays, or should I treat them as immutable?"
# 4. "What's the expected scale — small in-memory arrays or could these
#     be large datasets that don't fit in memory?"
#     → Answer guides which approach to use (HashSet vs Two Pointers
#       vs streaming)

# ─── Approach 1: HashSet ─────────────────────────────────────────────
# Time: O(n + m) | Space: O(min(n, m))
#
# Choose when: arrays unsorted, memory not constrained
# Self-review: empty input → [], all dupes → [], no intersection → []
#
# Volunteer before being asked:
#   - Already optimised: store smaller array (swap below)
#   - One array too large for memory → set the small, stream the large
#   - Both too large → external merge sort + Approach 2
#   - Real world: equivalent to a DB index lookup vs full table scan

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1         # always set the smaller

        seen = set(nums1)
        res = []

        for num in nums2:
            if num in seen:
                res.append(num)
                seen.remove(num)                # prevent duplicate results

        return res


# ─── Approach 2: Sort + Two Pointers ─────────────────────────────────
# Time: O(n log n + m log m) | Space: O(1) excluding output
#
# Choose when: memory constrained, or input already sorted
# If already sorted: skip sort → O(n + m) time
#
# Volunteer before being asked:
#   - Arrays on disk → stream both sorted files, same logic applies
#   - Why skip duplicate i? → prevents adding same value twice to result

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        n, m = len(nums1), len(nums2)
        res, i, j = [], 0, 0

        while i < n and j < m:
            while j < m and nums2[j] < nums1[i]:
                j += 1                          # advance j to catch up

            if j < m:
                if nums1[i] == nums2[j]:
                    res.append(nums1[i])
                i += 1
                while i < n and nums1[i] == nums1[i - 1]:
                    i += 1                      # skip duplicates in nums1

        return res


# ─── Decision guide ──────────────────────────────────────────────────
# Scale: small, unsorted        → Approach 1  (HashSet)
# Scale: small, sorted          → Approach 2  (Two Pointers, skip sort)
# Scale: one array huge         → set the small, stream the large
# Scale: both arrays huge       → external merge sort → Approach 2