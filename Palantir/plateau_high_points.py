from collections import deque


def plateau_bfs(grid, start):
    width, height = len(grid), len(grid[0])
    # queue = deque([[start]])
    queue = [[start]]
    seen = {start}
    result = [start]
    while queue:
        path = queue.pop(0)
        x, y = path[-1]
        for x2, y2 in (
                (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x - 1, y + 1), (x + 1, y + 1), (x - 1, y - 1),
                (x + 1, y - 1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[x2][y2] == grid[x][y] and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                result.append((x2, y2))
                seen.add((x2, y2))
            elif 0 <= x2 < width and 0 <= y2 < height and grid[x2][y2] > grid[x][y] and (x2, y2) not in seen:
                return []

    print(result)
    return result


def plateau_high_points(arr):
    output = []

    visited_plateau = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (i, j) not in visited_plateau:
                plateau = plateau_bfs(arr, (i, j))
                visited_plateau.extend(plateau)

                output.extend(plateau)

    output_set = list(set(output))

    final_result = []
    for i in range(len(arr)):
        row_array = []
        for j in range(len(arr[i])):
            row_array.append(0)
        final_result.append(row_array)

    for cell_x, cell_y in output_set:
        final_result[cell_x][cell_y] = 1

    return final_result


print(plateau_high_points([[1, 2, 1, 3, 4],
                           [1, 5, 2, 2, 2],
                           [4, 5, 1, 9, 7],
                           [3, 5, 3, 7, 6],
                           [4, 3, 1, 7, 3]]))

# print(plateau_high_points([[1, 1, 1, 1, 1],
#                            [1, 2, 2, 2, 1],
#                            [1, 2, 3, 2, 1],
#                            [1, 2, 2, 2, 1],
#                            [1, 1, 1, 1, 1],
#                            [1, 1, 1, 1, 3]]))
