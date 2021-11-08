import collections
def sort_matrix_dia(matrix):

    #to get the top entry
    _dict = collections.defaultdict(list)

    for i in range(len(matrix[0])):
        geteachTopDiagonal(matrix, 0, i, _dict, 0, i)

    #to get the left entry
    for i in range(1, len(matrix)):
        geteachTopDiagonal(matrix, i, 0, _dict, i, 0)

    #sorting the _dict values
    for key, value in _dict.items():
        _dict[key] = sorted(value)

    for key , val in _dict.items():
        puteachDiagonal(matrix, key[0], key[1], val)

    print(_dict)
    print(matrix)

def geteachTopDiagonal(matrix, i, j, _dict, x, y):
    
    if i == len(matrix) - 1  or j == len(matrix[0]) - 1:
        print(i, j)
        _dict[(x, y)].append(matrix[i][j])
        return 
    else:
        _dict[(x, y)].append(matrix[i][j])
        geteachTopDiagonal(matrix, i+1, j+1, _dict, x, y)

def puteachDiagonal(matrix, i, j, val):
    if i == len(matrix) - 1  or j == len(matrix[0]) - 1:
        matrix[i][j] = val[0]
        return
    else:
        matrix[i][j] = val[0]
        puteachDiagonal(matrix, i+1, j+1, val[1:])

matrix = [
    [3,3,6,1,2],
    [2,2,1,2,3],
    [1,1,1,2,2]
]

print(sort_matrix_dia(matrix))




