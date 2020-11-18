
def jump_game(arr):
    furthest_reach = 0
    last_idx = len(arr) - 1
    i = 0
    while i <= furthest_reach and furthest_reach < last_idx:
        furthest_reach = max(furthest_reach, arr[i] + i)
        i += 1
    return furthest_reach >= last_idx

print(jump_game([2,3,1,1,4]))
print(jump_game([3,2,1,0,4]))

print([3,4,5,6,7].pop())
