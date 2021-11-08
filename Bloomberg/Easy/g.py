def collatz(N):
    steps = 0
    while N > 1:
        if N %2 == 0:
            N = N//2
        else:
            N = (3*N) + 1
        steps += 1

    return steps
    recursion

# def collatz
# the same

# space is differet

# O(steps) in the call stack

# constant. O(N), we have to reduce N to 1. This is an uppper bound
# k is always less than N. but N is an upper bound


# def collatz(N, steps):
#     if N == 1:
#         return steps
#     if N %2 == 0:
#             return(N//2
#         else:
#             N = (3*N) + 1

# Save previous computations
# Use memoization technique.


# change to recursive approach. Memoization is more intuitive here.
# memoization is a bit more involved in an iterative solution.

# We will n

# def __init__(self):
#     self.dict = {}

# from collections import deque # double ended queue
# def collatz(N):
#     steps = 0
#     queue = deque([N]) # stores intermediate values
#     while N > 1:
#         if N in self.dict:
#             return steps + self.dict[N]

#         if N %2 == 0:
#             N = N//2
#         else:
#             N = (3*N) + 1
#         queue.append(N)
#         steps += 1
    
#     cnt = 0
#     while queue:
#         curr = queue.pop( )
#         cnt += 1
#         self.dict[curr] = cnt
    
#     return self.dict[num]