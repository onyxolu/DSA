from collections import List 

# Two Pointers

class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0
        while i<len(encoded1):
            prod = encoded1[i][0] * encoded2[j][0]
            minVal = min(encoded1[i][1], encoded2[j][1])
            #if previous product was same, add the result to previous value
            #else append to result array
            if res and res[len(res)-1][0] == prod:
                res[len(res)-1][1] += minVal
            else:
                res.append([prod, minVal])
            #subtract min value from frequency of current value of each array
            # if frequency of any of those is increment current pointer for array
            encoded1[i][1] = encoded1[i][1]-minVal
            encoded2[j][1] = encoded2[j][1]-minVal
            
            if encoded1[i][1]<=0:
                i+=1
            if encoded2[j][1]<=0:
                j+=1
        return res
        