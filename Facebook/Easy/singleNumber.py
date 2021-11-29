# Hashmap
    
# def singleNumber(self, nums):
#     dict = {}
#     for num in nums:
#         if num in dict:
#             dict[num] += 1
#         else: dict[num] = 1
    
#     for val in nums:
#         if dict[val] == 1:
#             return val
        
# XOR

#It returns zero if we take XOR of two same numbers.
# It returns the same number if we XOR with zero.
# So we can XOR all the numbers in the input; duplicate numbers will zero out each other and we will be left with the single number.

def singleNumber(nums):
    res = 0
    for num in nums:
        res ^= num
        print(res)
    return res

# 4
# 5
# 7
# 6
# 4


print(singleNumber([4,1,2,1,2]))