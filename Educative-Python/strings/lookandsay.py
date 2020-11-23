
# 1 , 11, 21, 1211, 111221, 312211
def look(n):
    ans = []
    for i in range(n):
        if i == 0:
            ans.append("1");
            continue
        count = {}
        str_val = ''
        prev_val = ans[i-1]
        for i in range(len(prev_val)):
            if i+1 == len(prev_val):
                if prev_val[i] in count:
                    count[prev_val[i]] += 1
                    str_val = str_val + str(count[prev_val[i]])  + str(prev_val[i]) 
                else:
                    str_val = str_val + "1" + str(prev_val[i]) 
                continue   

            if prev_val[i] in count:
                count[prev_val[i]] += 1
            else:
                count[prev_val[i]] = 1

            if prev_val[i+1] != prev_val[i]:
                str_val = str_val + str(count[prev_val[i]]) + str(prev_val[i])
                del count[prev_val[i]]

        ans.append(str_val)
        
    return ans



print(look(10))



# def next_number(s):
#     result = []
#     i = 0
#     while i < len(s):
#         count = 1
#         while i + 1 < len(s) and s[i] == s[i+1]:
#             i += 1
#             count += 1
#         result.append(str(count) + s[i])
#         i += 1
#     return ''.join(result)

# s = "1"
# print(s)
# n = 4
# for i in range(n-1):
#     s = next_number(s)
#     print(s)