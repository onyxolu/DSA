def optimaltask(A):
    A = sorted(A)

    for i in range(len(A)//2):
        print(A[i], A[~i])  

print(optimaltask([6, 3, 2, 7, 5, 5]))