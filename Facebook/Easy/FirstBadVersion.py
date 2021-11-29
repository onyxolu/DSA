
# Binary Search

def isBadVersion(version):
    return "hi"


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = int(left + (right - left)/2)
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
                
        return left


        