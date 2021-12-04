

# Hashmap, Greedy
# 9986543538238
# hashmap, key is num, val is last index
# for each xter, we try to find a xter from 9 to Xter-1 to swap with

# TC = 0(n*9) - 0(N)
# SC = 0(N)


class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list([int(c) for c in str(num)])
            
        last_index = {n:i for i,n in enumerate(num_list)}
        
        for i, n in enumerate(num_list):
            for d in range(9, n, -1):
                if d in last_index and last_index[d] > i:
                    num_list[i] , num_list[last_index[d]] = num_list[last_index[d]], num_list[i]
                    return int("".join([str(d) for d in num_list]))
        return num
                
        