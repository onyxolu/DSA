
nums = [2,3,3,3,6,9,9]
def remove_duplicates(nums):
    next_non_duplicate = 1

    i = 1

    while i < len(nums):
        if nums[next_non_duplicate - 1] != nums[i]:
            nums[next_non_duplicate] = nums[i]
            next_non_duplicate += 1
        i += 1

    return next_non_duplicate


print(remove_duplicates(nums))

# Remove instances of key 
num = [3,2,3,6,3,10,9,3]

def remove_instances(num, key):
    next_elem = 0

    for i in range(len(num)):
        if num[i] != key:
            num[next_elem] = num[i]
            next_elem += 1
    
    return next_elem

print(remove_instances(num, 3))