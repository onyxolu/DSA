import math
#use_binary_search
#if the sum of diff between each consecutive distances
#divided by mid distance is greater than k
#increase left to mid
#nlog(upper_bound)
class Solution:
    """
    @param stations: an integer array
    @param k: an integer
    @return: the smallest possible value of D
    """
    def minmaxGasDist(self, stations, k):
        # Write your code here
        left, right = 1e-6, stations[-1] - stations[0]
        while left + 1e-6 < right:
            mid = (left + right) / 2				
            count = 0
            for a, b in zip(stations, stations[1:]):
                count += math.ceil((b - a) / mid) - 1		
            if count > k:					
                left = mid
            else:							
                right = mid
        return right