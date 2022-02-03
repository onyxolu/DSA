
# sorting and hashmap 0(NLOGN)

class Solution:
    def frequencySort(self, s: str) -> str:
        dict = {}
        res = ""
        for val in s:
            if val in dict:
                dict[val] += 1
            else:
                dict[val] = 1
        s = sorted(dict, key = lambda x: dict[x] , reverse = True)
        for val in s:
            res += val * dict[val]
        return res


    
        