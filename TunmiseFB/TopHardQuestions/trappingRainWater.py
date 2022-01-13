# Multiple soln link: https://www.geeksforgeeks.org/trapping-rain-water/

'''

APPROACH 1: BRUTE FORCE

The idea is to traverse every array element and find the highest bars on the left and right sides. Take the smaller of two heights. The difference between the smaller height and height of the current element is the amount of water that can be stored in this array element.

Algorithm: 
1. Traverse the array from start to end.
2. For every element, traverse the array from start to that index and find the maximum height (a) and traverse the array from the current index to end, and find the maximum height (b).
3. The amount of water that will be stored in this column is min(a,b) – array[i], add this value to the total amount of water stored
4. Print the total amount of water stored.


Time Complexity - O(n2) - There are two nested loops traversing the array, So time Complexity is O(n2).
Space Complexity - O(1) - No extra space is required.
'''


def maxWater(arr, n):

    # To store the maximum water
    # that can be stored
    res = 0

    # For every element of the array
    for i in range(1, n - 1):

        # Find the maximum element on its left
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        # Find the maximum element on its right
        right = arr[i]

        for j in range(i + 1, n):
            right = max(right, arr[j])

        # Update the maximum water
        res = res + (min(left, right) - arr[i])

    return res


'''
APPROACH 2: DP

In the previous solution, to find the highest bar on the left and right, array traversal is needed which reduces the efficiency of the solution. 
To make this efficient one must pre-compute the highest bar on the left and right of every bar in linear time. Then use these pre-computed values to find the amount of water in every array element.

Algorithm: 
1. Create two arrays left and right of size n. create a variable max_ = INT_MIN.
2. Run one loop from start to end. In each iteration update max_ as max_ = max(max_, arr[i]) and also assign MAX LEFT left[i] = max_
3. Update max_ = INT_MIN.
4. Run another loop from end to start. In each iteration update max_ as max_ = max(max_, arr[i]) and also assign max right right[i] = max_
5. Traverse the array from start to end.
6. The amount of water that will be stored in this column is min(a,b) – array[i],(where a = left[i] and b = right[i]) add this value to total amount of water stored
7. Print the total amount of water stored.

Time Complexity - O(n) - Only one traversal of the array is needed, So time Complexity is O(n).
Space Complexity - O(n) - Two extra arrays are needed each of size n.

'''


def findWater(arr, n):

    # left[i] contains height of tallest bar to the
    # left of i'th bar including itself
    left = [0]*n

    # Right [i] contains height of tallest bar to
    # the right of ith bar including itself
    right = [0]*n

    # Initialize result
    water = 0

    # Fill left array
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i-1], arr[i])

    # Fill right array
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i + 1], arr[i])

    # Calculate the accumulated water element by element
    # consider the amount of water on i'th bar, the
    # amount of water accumulated on this particular
    # bar will be equal to min(left[i], right[i]) - arr[i] .
    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]

    return water


'''
OPTIMIZING THE SPACE OF THE ABOVE SOLUTION:

Instead of maintaining two arrays of size n for storing the left and a right max of each element, maintain two variables to store the maximum till that point. 

Since water trapped at any element = min(max_left, max_right) – arr[i]. 
Calculate water trapped on smaller elements out of A[lo] and A[hi] first and move the pointers till lo doesn’t cross hi.

Time Complexity - O(n) - Only one traversal of the array is needed.
Auxiliary Space - O(1) - As no extra space is required.
'''


def findWater(arr, n):

    # initialize output
    result = 0

    # maximum element on left and right
    left_max = 0
    right_max = 0

    # indices to traverse the array
    lo = 0
    hi = n-1

    while(lo <= hi):

        if(arr[lo] < arr[hi]):

            if(arr[lo] > left_max):

                # update max in left
                left_max = arr[lo]
            else:

                # water on curr element = max - curr
                result += left_max - arr[lo]
            lo += 1

        else:

            if(arr[hi] > right_max):
                # update right maximum
                right_max = arr[hi]
            else:
                result += right_max - arr[hi]
            hi -= 1

    return result


'''
APRROACH USING STACK

We can use a Stack to track the bars that are bounded by the longer left and right bars. This can be done using only one iteration using Stacks.

Approach:

1. Loop through the indices of the bar array.

2. For each bar, we can do the following:
    -   While the Stack is not empty and the current bar has a height greater than the top bar of the stack,
    -   Store the index of the top bar in pop_height and pop it from the Stack.
    -   Find the distance between the left bar(current top) of the popped bar and the current bar.
    -   Find the minimum height between the top bar and the current bar.
    -   The maximum water that can be trapped in distance * min_height.
    -   The water trapped including the popped bar is (distance * min_height) – height[pop_height].
    -   Add that to the fans.

3. Final answer will the ans.

Time Complexity: O(n)
Auxiliary Space: O(n) 

'''


def maxWater(height):

    # Stores the indices of the bars
    stack = []

    # size of the array
    n = len(height)

    # Stores the final result
    ans = 0

    # Loop through the each bar
    for i in range(n):

        # Remove bars from the stack
        # until the condition holds
        while(len(stack) != 0 and (height[stack[-1]] < height[i])):

            # store the height of the top
            # and pop it.
            pop_height = height[stack[-1]]
            stack.pop()

            # If the stack does not have any
            # bars or the the popped bar
            # has no left boundary
            if(len(stack) == 0):
                break

            # Get the distance between the
            # left and right boundary of
            # popped bar
            distance = i - stack[-1] - 1

            # Calculate the min. height
            min_height = min(height[stack[-1]], height[i])-pop_height

            ans += distance * min_height

        # If the stack is either empty or
        # height of the current bar is less than
        # or equal to the top bar of stack
        stack.append(i)

    return ans


'''
Method 5 (Two Pointer Approach)

At every index, The amount of rainwater stored is the difference between current index height and a minimum of left max height and right max-height



Time Complexity: O(n)
Auxiliary Space: O(1)


as we move our pointers, we are comparing our current index with the max we'v seen so far for left and right

we compare the heights to know which to check first.

e.g




'''


class Solution:
    def trap(self, height):
        ans = 0
        maxLeft, maxRight = 0, 0
        l = 0
        r = len(height) - 1
        while l < r:
            if height[l] < height[r]:
                if height[l] > maxLeft:
                    maxLeft = height[l]
                else:
                    ans += maxLeft - height[l]
                l += 1
            else:
                if height[r] > maxRight:
                    maxRight = height[r]
                else:
                    ans += maxRight - height[r]
                r -= 1

        return ans
