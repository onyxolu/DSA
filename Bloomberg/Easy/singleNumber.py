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

def singleNumber(nums):
    res = 0
    for num in nums:
        res ^= num
        print(res)
    return res


print(singleNumber([4,1,2,1,2]))