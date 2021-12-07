'''
BRUTE FORCE:

The simplest method is to consider every possible subarray of the given nums array, find the sum of the elements of each of those subarrays and check for the equality of the sum obtained with the given k. Whenever the sum equals k, we can increment the count used to store the required result.

Times out
'''

'''
OPTIMAL: 
If the cumulative sum of two indices i and j has a difference of k, i.e. sum[i] - sum[j], then the sum of the indices between i and j is equal to k.

Based on these, we make use of a hashmap which is used to store the cumulative sum up to all the indices possible along with the number of times the same sum occurs. We store the data in the form: {sum i, no. of occurences of sum i }

We traverse over the array nums and keep on finding the cumulative sum. Every time we encounter a new sum, we make a new entry in the hashmap corresponding to that sum. If the same sum occurs again, we increment the count corresponding to that sum in the hashmap. Further, for every sum encountered, we also determine the number of times the sum−k has occurred already, since it will determine the number of times a subarray with sum k has occurred up to the current index. We increment the count by the same amount.

After the complete array has been traversed, the count gives the required result.


Time complexity : O(n). The entire nums array is traversed only once.

Space complexity : O(n). Hashmap map can contain up to n distinct entries in the worst case.

'''

def subarraySum(self, nums, k):
    
    #[1,2,3] 3
    # {0:1}  diff -3 res = 0
    # [1] diff -2 {0:1, 1:1}  res = 0
    # [1,2] diff 0 {0:1, 1:1, 3: 1} res = 1, we have 1 subarr from 2
    # [1,2,3] diff 3 {0:1, 1:1, 3:1, 6:1} res = 1+1 
    
    res, curSum = 0,0
    prefixSums = {0: 1}
    for n in nums:
        curSum += n
        diff = curSum - k
        
        res += prefixSums.get(diff, 0)
        prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

    return res