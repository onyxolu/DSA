'''
statement : algorithm to minimize the largest sum among these m subarrays.

1.  set low and high limits of ( minimum largest sum)
2.  condition for reaching to possible answer

if subarrays are more than m ,then we need large (min large sum) ,left = mid+1

'''
#time complexity - nlogk 
# where k is the mid value 
# between the max number in array and the total sum in the array

def isvalid(nums,m,possible):    # verify possible subarrays by given sum
    subarrays = 1
    running = 0

    for num in nums:
        running += num
        if running > possible:
            subarrays += 1
            running = num
    return subarrays <= m

def largest_sum(nums,m):
    low = max(nums)
    high = sum(nums)

    while low <= high:
        possible = (low+high)//2

        if isvalid(nums,m,possible):
            high = possible-1          # subarrays are less
        else:
            low = possible+1           # subarrays are more
    return low