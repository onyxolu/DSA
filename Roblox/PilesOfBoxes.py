def codes(arrOfHeights):
    arrOfHeights.sort(reverse = True)
    i = 0
    step = 0
    while i<len(arrOfHeights)-1:
        if arrOfHeights [i+1] < arrOfHeights[i]:
            step += i+1
        i+=1
    return step