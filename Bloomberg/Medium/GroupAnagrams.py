

class Solution:
    def groupAnagrams(self, strs):
        dict = {}
        ans = []
        
        for i in range(len(strs)):
            val = strs[i]
            sortedVal = ''.join(sorted(val))
            
            if sortedVal in dict:
                dict[sortedVal].append(val)
            else:
                dict[sortedVal] = [val]
                
        for i, v in enumerate(dict):
            ans.append(dict[v])
            
        return ans


# Hash
    
class Solution:
    def groupAnagrams(self, strs):
        gruops = {}
        
        for s in strs:
            key = 0
            
            for char in s:
                key += hash(char)
            
            if key in gruops:
                gruops[key].append(s)
            else:
                gruops[key] = [s]
        
        return gruops.values()