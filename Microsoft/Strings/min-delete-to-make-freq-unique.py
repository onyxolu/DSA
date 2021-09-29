def minDeletions(self, s: str) -> int:
    count=[0 for i in range(26)]
    for i in s: count[ord(i)-ord('a')]+=1
    count=[i for i in count if i>0]
    count.sort(reverse=True)
    values=0
    mn=count[0]
    for i in range(1,len(count)):
        if mn <= count[i]:
            mn = max(mn - 1, 0)
            values += count[i] - mn
        else: mn = count[i]
    return values



# ceabaacb
# aaabbcce

# init array with 0 for 26 [00000]
# set alphabet values in their index  [3, 2, 2, 0, 1, 0, 0, 0]
# sort array and remove 0s [3,2,2,1] - 3
# [3,2,1,1]
# [3,2,1,0]