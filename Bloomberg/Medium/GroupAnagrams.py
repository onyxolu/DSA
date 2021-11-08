

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