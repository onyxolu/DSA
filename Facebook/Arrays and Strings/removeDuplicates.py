

def removeDuplicates(arr):
    next_non_duplicate = 0
    i = 1
    while i < len(arr):
        print(next_non_duplicate, i, arr)
        if arr[next_non_duplicate] != arr[i]:
            arr[next_non_duplicate+1] = arr[i]
            next_non_duplicate += 1
        i += 1

    for j in range(next_non_duplicate +1, len(arr)):
            del arr[-1]

    return arr


print(removeDuplicates([2,3,3,3,6,9,9]))

# 0 1 [2, 3, 3, 3, 6, 9, 9]
# 1 2 [2, 3, 3, 3, 6, 9, 9]
# 1 3 [2, 3, 3, 3, 6, 9, 9]
# 1 4 [2, 3, 3, 3, 6, 9, 9]
# 2 5 [2, 3, 6, 3, 6, 9, 9]
# 3 6 [2, 3, 6, 9, 6, 9, 9]