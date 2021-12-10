

class Solution:
    def addOperators(self, num: str, target: int):
        res = []
        prev = None
        def dfs(i, val, path, prev):
            if i == len(num):
                if val == target:
                    res.append(path)
                return
            cur_val = 0
            for j in range(i, len(num)):
                cur_val = cur_val * 10 + int(num[j])
                if prev == None:
                    dfs(j+1, val+cur_val, path+num[i:j+1],cur_val)
                else:
                    dfs(j+1, val+cur_val,path+'+'+num[i:j+1],cur_val)
                    dfs(j+1, val-cur_val,path+'-'+num[i:j+1],-cur_val)
                    dfs(j+1, val+cur_val*prev-prev,path+'*'+num[i:j+1],cur_val*prev)
                if num[i] == '0':#prevent leading zeros
                    break
        dfs(0, 0, '', None)
        return res