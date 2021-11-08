def maxTime(s):
    s=list(s)
    if s[0] == '?':
        s[0] = '2' if s[1] <= '3' or s[1] == '?' else '1'
    if s[1]=='?': s[1]='9' if s[0]!='2' else '3'
    if s[3]=='?': s[3]='5'
    if s[4]=='?': s[4]='9'
    return ''.join(s)