# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/


# def compute(s):
#   dic = {'A':[], 'B':[], 'C':[]}
#   result = 0
#   length = len(s)

#   # added in reverse order to allow pop() to be O(1)
#   for i in range(len(s)-1,-1,-1):
#     if (s[i] in dic.keys()):
#       dic[s[i]].append(i)
  
#   for i in range (length):
#     vals = list(map(lambda x:x[-1], dic.values()));
#     maxVal = max(vals)
#     minVal = min(vals)
#     result += (len(s) - maxVal)
#     if (i == minVal):
#       if (dic['A'][-1] == minVal):
#         dic['A'].pop()
#         if (len(dic['A']) == 0):
#           break;
#       elif (dic['B'][-1] == minVal):
#         dic['B'].pop()
#         if (len(dic['B']) == 0):
#           break;
#       elif (dic['C'][-1] == minVal):
#         dic['C'].pop()
#         if (len(dic['C']) == 0):
#           break;
#   return result


def analyzeInvestments(s):
    s = s.lower()
    print(s)
    startWindow = 0
    count = 0 
    d = {'a':0,'b':0,'c':0}
    
    for endWindow in range(len(s)):
        if s[endWindow] in d:
            d[s[endWindow]]+=1
        
        while  all(d.values()):
            count += len(s)-endWindow
            if s[startWindow] in d:
                d[s[startWindow]] -= 1
            startWindow += 1
            
    return count

print(analyzeInvestments("ABCCBA"))