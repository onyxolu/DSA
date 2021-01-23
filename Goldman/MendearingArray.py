def meanderingArray(nums):
    meandered = []
    nums = sorted(nums)
    n = len(nums)
    half = int(n/2)
    
    if half%2 == 0:
        half+=1
    
    for i in range(half):
        meandered.append(nums[n-1-i])
        if n-1-i != i:
            print(i)
            meandered.append(nums[i])
    
    if(n%2!=0):
        meandered.append(nums[half])
   
    return meandered