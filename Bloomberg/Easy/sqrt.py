
# Time Complexity = 0(N)
# Space Complexity = 0(1)

# Binary Search

# 1 2 3 4 5 6 7 8 9 10  mid=5 , left=1, right=10 x=10
# 1 2 3 4 5   mid = 3 right=5, left=1  x = 10   
# 4 5 mid = 4 left 4 right = 5

import math
def sqrt(x):
    left = 1
    right = x

    if x < 2:
        return x

    # Binary Search

    while(left < right):

        mid = left + math.floor((right - left)/2)

        if mid * mid == x:
            return mid
        elif mid * mid > x:
            right = mid
        else: left = mid + 1
    return left - 1


print(sqrt(9))