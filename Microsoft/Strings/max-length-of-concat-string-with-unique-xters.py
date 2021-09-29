maxim = 0
def maxLength( arr):

    def dfs(i,curr):
        global maxim
        maxim = max(maxim ,len(curr))
        for j in range(i,len(arr)):
            s1=set(arr[j])
            if len(s1.intersection(curr))!=0 or len(s1)!=len(arr[j]):#Means curr already have a character of arr[j] or arr[j] has a repeating character
                continue
            dfs(j+1,curr+arr[j])
    dfs(0,"")
    return maxim

A = ["un","iq","ue"]
B = ["cha","r","act","ers"]
C = ["abcdefghijklmnopqrstuvwxyz"]
print(maxLength(C))