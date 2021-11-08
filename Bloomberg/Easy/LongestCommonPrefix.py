from abc import abstractproperty


# Time Complexity => 0(NM) m = length of shortest array
# Space Complexity => 0(1) 


def longestCommonPrefix(strs):
    result = ""
    # Pick length of first string. i for current letter you are checking for
    for i in range(len(strs[0])):
        for s in strs:
            # check for the smallest array before checking for common prefix
            if i == len(s) or s[i] != strs[0][i]:
                return result
        result += strs[0][i]

    return result

print(longestCommonPrefix(["flower","flow","flight"]))


    