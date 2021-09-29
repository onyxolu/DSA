def sumZero(n: int):
    
    d, m, o = *divmod(n, 2), []
    for x in range(1, d + 1):
        o.extend([x, -x])
    if m:
        o.append(0)
    return o


print(sumZero(5))