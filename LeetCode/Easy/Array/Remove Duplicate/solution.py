  nums = [1,1,1,1,1,1,2]
  
  #check for empty array
        if not nums:
            return 0
        #set initial value
        current = nums[0]
        #loop from index 1
        for num in nums[1:]:
            if num == current:
                nums.remove(num)
            else:
                current = num
            
        return len(nums)
    