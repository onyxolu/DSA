# Hashmap

def findDisappearedNumbers(self, nums):
    ans = []
    hashSet = set(nums)            
    for i in range(1,len(nums)+1):
        if i not in hashSet:
            ans.append(i)
    return ans
        


# Better space > absolute

def findDisappearedNumbers(nums):
    missingNums = []
    for i in range(len(nums)):
        cur = abs(nums[i])
        nums[cur-1] = -(abs(nums[cur-1]))
        
    for j in range(len(nums)):
        if nums[j] > 0:
            missingNums.append(j+1)
            
    return missingNums