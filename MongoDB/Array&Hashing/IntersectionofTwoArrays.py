from typing import List

# Clarify: duplicates ignored? empty return ok? immutable input? expected scale?
# Scale answer → HashSet (small) | Two Pointers (sorted/memory tight) | Stream/External sort (huge)

# Approach 1: HashSet — O(n+m) time | O(min(n,m)) space
# Volunteer: one huge → stream it; both huge → external merge sort + Approach 2
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1         # store smaller
        seen = set(nums1)
        res = []
        for num in nums2:
            if num in seen:
                res.append(num)
                seen.remove(num)                # prevent dupes
        return res

# Approach 2: Sort + Two Pointers — O(n log n + m log m) time | O(1) space
# Volunteer: already sorted → skip sort → O(n+m); on disk → stream both sorted files
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res, i, j = [], 0, 0
        while i < len(nums1) and j < len(nums2):
            while j < len(nums2) and nums2[j] < nums1[i]:
                j += 1
            if j < len(nums2):
                if nums1[i] == nums2[j]:
                    res.append(nums1[i])
                i += 1
                while i < len(nums1) and nums1[i] == nums1[i-1]:
                    i += 1                      # skip dupes in nums1
        return res