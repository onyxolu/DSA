'''
BRUTE APPROACH 1:

We ignore the sparsity of the array and store the original array.

Complexity Analysis

Let nn be the length of the input array.

Time complexity: O(n) for both constructing the sparse vector and calculating the dot product.

Space complexity: O(1) - for constructing the sparse vector as we simply save a reference to the input array and O(1) for calculating the dot product.
'''

class SparseVector:
    def __init__(self, nums):
        self.array = nums

    def dotProduct(self, vec):
        result = 0
        for num1, num2 in zip(self.array, vec.array):
            result += num1 * num2
        return result






'''
EFFICIENT APPROACH:

Store the non-zero values and their corresponding indices in a dictionary, with the index being the key. Any index that is not present corresponds to a value 0 in the input array.
'''

class SparseVector:
    def __init__(self, nums: List[int]):
        self.seen = {}
        for idx, num in enumerate(nums):
            if num != 0:
                self.seen[idx] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        
        for key in vec.seen:
            if key in self.seen:
                ans += self.seen[key] * vec.seen[key]
        
        return ans
    






'''
OPTIMAL SOLUTION:
The optimised implementation would be to use a linked-list data structure to store the Sparse vector. Then we can use iterators to advance to next elements one at a time.

We also need to store the index of the non-zero elements so that we can compare the indices – only sum up the product if both indices are equal. And at each iteration we only advance the iterator with smaller index – until we reach one of the end.

The time and space complexity is both O(M). In C++, the STL::list is a linked-list data structure – which is perfect in this case. However, we can still replace it with vector which still works.


'''