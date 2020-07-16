# Brute Force

nums = [2,7,11,15]
target = 9

#loop through list
        for i in range(len(nums)):
            #condition to check if we are at the end of the list
            if i < len(nums) - 1:
                for j in range(len(nums)):
                    if (i != j):
                        #add two numbers and check
                       if(nums[i] + nums[j] == target):
                         return [i, j]


#efficient hashmap


         #keep track of seen items
        seen = {}
      #loop through the element
        for i,v in enumerate(nums):
            rem = target - v
            #get remainder and check in seen
            if rem in seen:
                return[seen[rem], i]
            seen[v] = i
            
        return[]
            

        