from collections import defaultdict
def typesquat1(list1,list2):
    result = []
    d = defaultdict(str)
    for i in list1:
        split_string = i.split('.')
        key = split_string[0]
        value = split_string[1]
        d[key] = value

    for i in list2:
        split_string = i.split('.')
        key = split_string[0]
        value = split_string[1]

        if key in d:
            if d[key] != value:
                result.append(i)

    return result

print(typesquat1(["palantir.com","apple.com"],["palantir.biz","apple.org","apple.com","appleorchard.com"]))

def typesquat2(list1,list2):
    result = []
    s = defaultdict(list)
    s["1"] = ["i","j","!","|"]
    s["i"] = ["1","j","l","|"]
    s["j"] = ["1","i","l","|"]
    s["l"] = ["1","i","j","|"]
    s["|"] = ["1","i","j","l"]

    s["s"] = ["5","$"]
    s["5"] = ["s","$"]
    s["$"] = ["s","5"]

    s["o"] = ["0"]
    s["0"] = ["o"]

    s["a"] = ["@"]
    s["@"] = ["a"]

    s["e"] = ["3"]
    s["3"] = ["e"]
    d = defaultdict(str)
    for i in list1:
        split_string = i.split('.')
        key = split_string[0]
        value = split_string[1]
        d[key] = value

    for i in list2:
        split_string = i.split('.')
        key = split_string[0]
        value = split_string[1]

        if key in d:
            if d[key] != value:
                result.append(i)
        else:
            keys_in_dict = d.keys()

            for item in keys_in_dict:
                if len(item) == len(key):
                    for j in range(len(item)):
                        if item[j] != key[j]:
                            if key[j] in s[item[j]]:
                                result.append(i)
                            break
                        
    return result

print(typesquat2(["palantir.com","nic.ci"],["paiantir.com","nic.cl","palantirtechnologies.com","nlc.biz"]))

def typesquat3(list1,list2):
    result = []
    s = defaultdict(list)
    s["1"] = ["i","j","l","|"]
    s["i"] = ["1","j","l","|"]
    s["j"] = ["1","i","l","|"]
    s["l"] = ["1","i","j","|"]
    s["|"] = ["1","i","j","l"]

    s["s"] = ["5","$"]
    s["5"] = ["s","$"]
    s["$"] = ["s","5"]

    s["o"] = ["0"]
    s["0"] = ["o"]

    s["a"] = ["@"]
    s["@"] = ["a"]

    s["e"] = ["3"]
    s["3"] = ["e"]



    d = defaultdict(str)
    for i in list1:
        split_string = i.split('.')
        key = split_string[0]
        value = split_string[1]
        d[key] = value

    for i in list2:
        split_string = i.split('.')
        key = split_string[0]
        value = split_string[1]

        if key in d:
            if d[key] != value:
                result.append(i)
        else:
            keys_in_dict = d.keys()

            for item in keys_in_dict:
                if len(item) == len(key):
                    for j in range(len(item)):
                        if item[j] != key[j]:
                            if key[j] in s[item[j]]:
                                result.append(i)
                            break

    for i in list1:
        for j in list2:
            if len(i) == len(j):
                editCount = 0
                k = 0
                while k < len(i)-1:
                    if i[k] != j[k]:
                        if i[k+1] == j[k]:
                            editCount += 1
                            k += 1
                    k += 1
                if editCount == 1:
                    result.append(j)
    return result

print(typesquat3(["palantir.com","apple.com"],["plaantir.com","aplantirtechnologies.com","palanti.rbiz"]))
                        
        



