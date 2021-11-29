
from collections import List

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        i,j,k = 0,0,0
        output = []
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                output.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:           
                minVal = min(arr1[i], arr2[j], arr3[k])
                if arr1[i] == minVal:
                    i += 1
                elif arr2[j] == minVal:
                    j += 1
                elif arr3[k] == minVal:
                    k += 1
                
        return output