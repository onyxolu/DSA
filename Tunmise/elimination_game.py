def elimination_game(n):
    return helper(n,True)

def helper(n,sig):
    if n == 1:
        return 1
    if sig:
        return 2*helper(n//2,False)
    else:
        if n%2 == 0:
            return 2*helper(n//2,True) -1
        else:
            return 2*helper(n//2,True)
# print(elimination_game(9))
