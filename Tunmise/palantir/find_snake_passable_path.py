def find_snake_passable_path(m):
    rows = []
    for i in range(len(m)):
        s =set(m[i])
        if len(s) == 1 and list(s)[0] == "0":
            rows.append(i)

    cols = []
    for i in range(len(m[0])):
        l = []
        for j in range(len(m)):
            l.append(m[j][i])
        s = set(l)
        if len(s) == 1 and list(s)[0] == "0":
            cols.append(i)

    return (rows,cols)
straight_board_1 = [['+', '+', '+', '0', '+', '0', '0'],
['0', '0', '0', '0', '0', '0', '0'],
['0', '0', '+', '0', '0', '0', '0'],
['0', '0', '0', '0', '+', '0', '0'],
['+', '+', '+', '0', '0', '0', '+']]
straight_board_2 = [['+', '+', '+', '0', '+', '0', '0'],
['0', '0', '0', '0', '0', '+', '0'],
['0', '0', '+', '0', '0', '0', '0'],
['0', '0', '0', '0', '+', '0', '0'],
['+', '+', '+', '0', '0', '0', '+']]
straight_board_3 = [['+', '+', '+', '0', '+', '0', '0'],
['0', '0', '0', '0', '0', '0', '0'],
['0', '0', '+', '+', '0', '+', '0'],
['0', '0', '0', '0', '+', '0', '0'],
['+', '+', '+', '0', '0', '0', '+']]
straight_board_4 = [['+']]
print(find_snake_passable_path(straight_board_1))
print(find_snake_passable_path(straight_board_2))
print(find_snake_passable_path(straight_board_3))
print(find_snake_passable_path(straight_board_4))
