# def urlify(s,n):
#     l = list(s)
#     spaceCount  = 0
#     for i in range(n):
#         if l[i] == " ":
#             spaceCount += 1
#     index = n + spaceCount * 2
#     j = index


#     for i in range(n-1,0,-1):
#         if l[i] == " ":
#             l[index-1] = "0"
#             l[index-2] = "2"
#             l[index-3] = "%"
#             index -= 3
#         else:
#             l[index-1] = l[i]
#             index -= 1
#     return l[:j]

# print(urlify("Mr John Smith       ",13))  
def uniqueCharaters(a,b):
    result_string = ""
    b_set = set(b)
    for letter in a:
        if letter not in b_set:
            result_string += letter
    return result_string

def uniqueCharaters2(a,b):
    result_string = ""
    hash_table = [False] * 128 

    for let in b:
        key = ord(let)
        hash_table[key] = True

    for letter in a:
        key = ord(letter)
        if hash_table[key] == False:
            
    return result_string

print(uniqueCharaters2("abbxcv","acv"))

def sum(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum