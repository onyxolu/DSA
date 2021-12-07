'''
BRUTE FORCE APROACH: 

One of the easiest way to solve this problem to take a number, find the product of all the numbers to its left, find the product of all the numbers to its right, and the product of these two numbers is the answer. Let us look into the code snippet.

Time Complexity - O(N²) where N is the number of elements in the list.
Space Complexity - O(N) where N is the number of elements in the list.
'''


class ProductFinder:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            left = 1
            right = 1
            for j in range(0, i):
                left *= nums[j]
            for k in range(i+1, len(nums)):
                right *= nums[k]
            output.append((left*right))
        return output





'''
APPROACH 2: Left and Right product lists

It's much easier to build an intuition for solving this problem without division once you visualize how the different products except self look like for each of the elements. So, let's take a look at an example array and the different products.


Algorithm

Initialize two empty arrays, L and R where for a given index i, L[i] would contain the product of all the numbers to the left of i and R[i] would contain the product of all the numbers to the right of i.

We would need two different loops to fill in values for the two arrays. For the array L, L[0] would be 1 since there are no elements to the left of the first element. For the rest of the elements, we simply use L[i] = L[i - 1] * nums[i - 1]. Remember that L[i] represents product of all the elements to the left of element at index i.

For the other array, we do the same thing but in reverse i.e. we start with the initial value of 1 in R[length - 1]R[length−1] where lengthlength is the number of elements in the array, and keep updating R[i] in reverse. Essentially, R[i] = R[i + 1] * nums[i + 1]. Remember that R[i] represents product of all the elements to the right of element at index i.

Once we have the two arrays set up properly, we simply iterate over the input array one element at a time, and for each element at index i, we find the product except self as L[i] * R[i].


Time complexity - O(N) where NN represents the number of elements in the input array. We use one iteration to construct the array L, one to construct the array R and one last to construct the answeranswer array using L and R.

Space complexity - O(N) used up by the two intermediate arrays that we constructed to keep track of product of elements to the left and right.
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # The length of the input array 
        length = len(nums)
        
        # The left and right arrays as described in the algorithm
        L, R, answer = [0]*length, [0]*length, [0]*length
        
        # L[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the L[0] would be 1
        L[0] = 1
        for i in range(1, length):
            
            # L[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            L[i] = nums[i - 1] * L[i - 1]
        
        # R[i] contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R[length - 1] would be 1
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            
            # R[i + 1] already contains the product of elements to the right of 'i + 1'
            # Simply multiplying it with nums[i + 1] would give the product of all 
            # elements to the right of index 'i'
            R[i] = nums[i + 1] * R[i + 1]
        
        # Constructing the answer array
        for i in range(length):
            # For the first element, R[i] would be product except self
            # For the last element of the array, product except self would be L[i]
            # Else, multiple product of all elements to the left and to the right
            answer[i] = L[i] * R[i]
        
        return answer




'''
APPROACH 3: BETTER SOLUTION WITH O(1) SPACE

The output array does not count towards the space complexity. 
This approach is essentially an extension of the approach above. Basically, we will be using the output array as one of L or R and we will be constructing the other one on the fly. Let's look at the algorithm based on this idea.

Algorithm.

1 - Initialize the empty answer array where for a given index i, answer[i] would contain the product of all the numbers to the left of i.

2 - We construct the answer array the same way we constructed the L array in the previous approach. These two algorithms are exactly the same except that we are trying to save up on space.

3 - The only change in this approach is that we don't explicitly build the R array from before. Instead, we simply use a variable to keep track of the running product of elements to the right and we keep updating the answer array by doing answer[i] = answer[i] * R. For a given index i, answer[i] contains the product of all the elements to the left and R would contain product of all the elements to the right. We then update R as R = R * nums[i].


Time complexity - O(N) where N represents the number of elements in the input array. We use one iteration to construct the array L, one to update the array answeranswer.

Space complexity - O(1) since we don't use any additional array for our computations. The problem statement mentions that using the answeranswer array doesn't add to the space complexity.
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # The length of the input array 
        length = len(nums)
        
        # The answer array to be returned
        answer = [0]*length
        
        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):
            
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1;
        for i in reversed(range(length)):
            
            # For the index 'i', R would contain the 
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer