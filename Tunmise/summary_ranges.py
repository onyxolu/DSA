class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == None or nums == []:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        ranges =[]
        start = nums[0]
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] != 1:
                if nums[i-1] == start:
                    ranges.append(str(start))
                else:
                    ranges.append(str(start)+"->"+str(nums[i-1]))
                start = nums[i]
                
        if nums[len(nums)-1] == start:
            ranges.append(str(start))
        else:
            ranges.append(str(start)+"->"+str(nums[len(nums)-1]))
        return ranges