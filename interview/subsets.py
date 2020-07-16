def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        if not nums:
            return ans
        
        #loop through the array to 2*n
        pow = 2 ** len(nums)
        for i in range(pow):
            
        #create subset arr
            subset = []
        
        #convert value to binary string
            binValue = bin(i).replace("0b", "")
            binValue = binValue.zfill(len(nums))
            print(binValue)
            
        #loop through the binary
            for j in range(len(nums)):
                # print(binValue[j])
        #check for value of 1 and push to subset
                if binValue[j] == "1":
                    subset.append(nums[j-1])
        #push subset to ans
            ans.append(subset)
        return ans
        
        