        
arr = [0,1,0]
        
def fruits(tree):
            
    dict = {}
    k = 2
    maxVal = 0
    windowValue = []
    for windowKey in range(len(tree)):
        currentVal = tree[windowKey]
        windowValue.append(currentVal)
        if(currentVal in dict):
            dict[currentVal] += 1
        else: 
            dict[currentVal] = 1


        if len(dict) > k:
            firstLetter = windowValue[0]
            if dict[firstLetter] > 1:
                dict[firstLetter] -= 1
            else:
                del dict[firstLetter]
            windowValue = windowValue[1:]
        else: 
            maxVal = max(len(windowValue), maxVal)


    return maxVal

print(fruits(arr))