
import random

def startGame():
    score = 0
    # Create a matrix of zeros
    # [0] [0] [0] [0]
    # [0] [0] [0] [0]
    # [0] [0] [0] [0]
    # [0] [0] [0] [0]
    matrix = [[0] * 4 for _ in range(4)]
    row = random.randint(0,3)
    col = random.randint(0,3)
    matrix[row][col] = 2
    while matrix[row][col] != 0:
        print(matrix)
        row = random.randint(0,3)
        col = random.randint(0,3)
    matrix[row][col] = 2
    print(matrix)






print(startGame())