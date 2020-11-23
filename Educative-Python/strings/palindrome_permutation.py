
def palindrome_perm(s):
    dict = {}
    for val in s:
        val_lower = val.lower()
        if val_lower in dict:
            dict[val_lower] += 1 
        else:
            dict[val_lower] = 1
    
    count = 0
    for x in dict.values():
        print(x, dict)
        if x % 2 != 0:
            count += 1

    print(count)
    return count <= 1
print(palindrome_perm("aab"))