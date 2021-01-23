
arr = [1,2,3,4,6] 
t = 6

# For only sorted lists
# Time: 0(N)
# SPace: 0(1)

def two_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        cur_target = arr[left] + arr[right]

        if cur_target == target:
            return [left, right]

        if cur_target > target:
            right -= 1
        else:
            left += 1

    return []

print(two_sum(arr, t))