def welshdic(alphabets,strings):
   
    alpha_index = {}
    for idx,val in enumerate(alphabets):
        alpha_index[val] = idx
    
    def comp(s):
        res = []
        i = 0
        while i < len(s)-1:
            if s[i] + s[i+1] in alpha_index.keys():
                res.append(alpha_index[s[i] + s[i+1]])
                i+=2
            else:
                res.append(alpha_index[s[i]])
                i += 1
        res.append(alpha_index[s[len(s)-1]])
        print(res)
        return tuple(res)
    strings.sort(key=comp)
    return strings
    
strings = ['abcd', 'abcdd']
alphabets = ['a','b','c','ch','dd','d','e', 'f', 'ff', 'g', 'ng', 'h', 'i', 'j', 'l', 'll', 'm', 'n', 'o', 'p', 'ph', 'r', 'rh', 's', 't', 'th', 'u', 'w', 'y']
    
print(welshdic(alphabets,strings))