

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