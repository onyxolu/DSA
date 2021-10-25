
arr = [
    [1,2,3,4],
    [10,11,12,5],
    [9,8,7,6],
]

arr = [
    [1,2,3,4],
    [10,11,12,5],
    [9,8,7,6],
]

def spiral_matrix(arr):
    cS = 0
    rS = 0
    cE = len(arr) - 1
    rE = len(arr[0]) - 1
    result = []

    while cS <= cE and rS <= rE:
        # Top Row
        topHArr = arr[cS]
        for i in range(rS, rE+1):
            if (cS > cE) or rS > rE:
                continue
            result.append(topHArr[i])
        cS += 1

        # Right Col
        for i in range(cS, cE+1):
            if (cS > cE) or rS > rE:
                continue
            result.append(arr[i][rE])
        rE -= 1

        # Bottom Row
        bottomArr = arr[cE] 
        for i in reversed(range(rS, rE+1)):
            if (cS > cE) or rS > rE:
                continue
            result.append(bottomArr[i])
        cE -= 1

        # left Col
        for i in reversed(range(cS, cE+1)):
            if (cS > cE) or rS > rE:
                continue
            result.append(arr[i][rS])
        rS += 1

        print(result)

    return result

# print(spiral_matrix(arr))


def spiral_matrix2(matrix):
    cS = 0
    rS = 0
    cE = len(matrix) - 1
    rE = len(matrix[0]) - 1
    result = []

    while cS <= cE and rS <= rE:
        # Top Row
        topHArr = matrix[cS]
        for i in range(rS, rE+1):
            result.append(topHArr[i])

        # Right Col
        for i in range(cS+1, cE+1):
            result.append(matrix[i][rE])

        # Bottom Row
        bottomArr = matrix[cE] 
        for i in reversed(range(rS, rE)):
            result.append(bottomArr[i])

        # left Col
        for i in reversed(range(cS+1, cE)):
            result.append(matrix[i][rS])
        
        cS += 1
        rE -= 1
        cE -= 1
        rS += 1

        print(result)
    
    return result

print(spiral_matrix2(arr))


