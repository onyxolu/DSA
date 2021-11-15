
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



