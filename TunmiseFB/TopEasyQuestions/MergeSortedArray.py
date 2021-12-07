class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num = m+n-1
        p1 = m-1
        p2 = n-1
        
        while num >= 0:
            m_val = nums1[p1] if p1 >= 0 else float('-inf')
            n_val = nums2[p2] if p2 >= 0 else float('-inf')
            if m_val > n_val:
                nums1[num] = m_val
                p1 -= 1
            else:
                nums1[num] = n_val
                p2 -= 1
            
            num -= 1