def rank(matrix, n):
    for i in range(len(matrix)):
        matrix[i] =  [sum(matrix[i]), i]

    copy = sorted(matrix, reverse = True, key=lambda x: (x[0], - x[1]))
    return copy[n-1][1]