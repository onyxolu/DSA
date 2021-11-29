
# import random

# def startGame():
#     score = 0
#     # Create a matrix of zeros
#     # [0] [0] [0] [0]
#     # [0] [0] [0] [0]
#     # [0] [0] [0] [0]
#     # [0] [0] [0] [0]
#     matrix = [[0] * 4 for _ in range(4)]
#     row = random.randint(0,3)
#     col = random.randint(0,3)
#     matrix[row][col] = 2
#     while matrix[row][col] != 0:
#         print(matrix)
#         row = random.randint(0,3)
#         col = random.randint(0,3)
#     matrix[row][col] = 2
#     print(matrix)






# print(startGame())

# function count(A){
#     let sumA = A.reduce((a, b) => a + b, 0)
#     currentSum = 0
#     ans = 0
#     for(val in A){
#         console.log(parseInt(currentSum) + parseInt(val))
#         if(currentSum + parseInt(val) <= 0){
#             ans += 1
#         }
#         else{
#             currentSum += val
#         }
#     }
#     return ans
# }

# def count(A):
#     currentSum = 0
#     ans = 0
#     for val in A:
#         print("curr", currentSum)
#         if currentSum + val <= 0:
#             print(currentSum + val)
#             ans += 1
#         else:
#             currentSum +=  val
#     return ans

# print(count([5,-2,-3,1]))



# import random


# n = 3
# arr = [1,2,3]



# def calc(n):
#     for i in range(n-1, 0, -1):
#         j = random.randint(0, i+1)
#         print(i, j)
#         arr[i],arr[j] = arr[j],arr[i]
#     return arr
        


# print(calc(n))



def fact(n):
    if (n == 0):
        return 1
    return n * fact(n-1)


def fact2(n):
    res = 1

    while n > 0:
        res *= n
        n -= 1

    return res


def collatz(num, memo={1: 0}):
    if num < 0:
        return 

    if num in memo:
         return memo[num]

    if num % 2:
        res =  1 + collatz(3*num, memo)
    else:
        res = 1 + collatz(num//2, memo)

    memo[num] = res
    print(memo)
    return res

# collatz(15)
