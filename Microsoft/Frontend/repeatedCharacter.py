

def soln(s):
    res = []
    startIdx = 0;
    for win_end in range(1, len(s)):
        if not (s[win_end] == s[win_end-1]):
            startIdx = win_end
        else:
            if win_end == len(s)-1 or s[win_end] != s[win_end+1]:
                res.append([startIdx, win_end])
    return res


print(soln("hellooooloohjhjjdjjjjjjjjjjjjjjjjjdhffjf00000000000"))