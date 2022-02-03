

def countMaximum(upright):
    sArr = upright[0].split(" ")
    smallColA = int(sArr[0])
    smallColB = int(sArr[1])

    if len(sArr) > 1:
        for i in range(1, len(upright)):
            sArr = upright[i].split(" ")
            s1 = int(sArr[0])
            s2 = int(sArr[1])
            if s1 < smallColA:
                smallColA = s1
            if s2 < smallColB:
                smallColB = s2
    return smallColA * smallColB


arr = ["2 3", "3 7", "4 1"]
print(countMaximum(arr))
