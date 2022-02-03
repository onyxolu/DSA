

def consecutiveSum(n):
    count = 0
    L = 1
    while (L * (L + 1) < 2 * n):
        a = (1.0 * n - (L * (L + 1)) / 2) / (L + 1)
        if (a - int(a) == 0.0):
            count += 1
        L += 1
    return count


print(consecutiveSum(21))
