

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobo_dict = {'0':'0', '1':'1','6':'9','8':'8', '9':'6'}
        num_180 = ""
        for i in num[::-1]:           
           if i not in strobo_dict:
              return False
              break
           else:
              num_180+= strobo_dict[i]
        return num_180==num