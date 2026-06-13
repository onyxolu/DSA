
# Hashset
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)

        res = []
        for num in nums2:
            if num in seen:
                res.append(num)
                seen.remove(num)
        return res
    

# Sorting and Two Pointers
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        n, m = len(nums1), len(nums2)
        res, i, j = [], 0, 0

        while i < n and j < m:
            while j < m and nums2[j] < nums1[i]:
                j += 1
            if j < m:
                if nums1[i] == nums2[j]:
                    res.append(nums1[i])
                i += 1
                while i < n and nums1[i] == nums1[i - 1]:
                    i += 1

        return res
