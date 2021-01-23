nums = [1,1,1,1,1,1,2]

# remove duplicates from sorted array

#check for empty array
def remove_dup(nums):
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


s = "cbacdcbc"

def removeDuplicateLetters(s: str) -> str:
    dict = {}
    result = []
    dict = {char: idx for idx, char in enumerate(s)}
    # for i in range(len(s)):
    #     val = s[i]
    #     if val not in dict:
    #         dict[val] = i
    #     else:
    #         maxIdx = max(i, dict[val])
    #         dict[val] = maxIdx
            
    for idx, val in enumerate(s):
        if val not in result:
            while result and val < result[-1] and idx < dict[result[-1]]:
                result.pop()
            result.append(val)
            print(result)
            
    return "".join(result)


print(removeDuplicateLetters(s))



    
    