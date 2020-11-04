
import copy

def bfs(grid, start):
    width, height = len(grid), len(grid[0])
    # queue = deque([[start]])
    queue = [[start]]
    seen = {start}
    result = [start]
    while queue:
        path = queue.pop(0)
        x, y = path[-1]
        for x2, y2 in (
        (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x - 1, y + 1), (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[x2][y2] < grid[x][y] and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                result.append((x2, y2))
                seen.add((x2, y2))

    return result


def new_get_high_points(arr):
    if len(arr) == 1 and len(arr[0]) == 1:
        return arr

    new_array = []
    for i in range(len(arr)):
        row_array = []
        for j in range(len(arr[i])):
            row_array.append(0)

        new_array.append(row_array)

    for x in range(len(arr)):
        for y in range(len(arr[x])):
            high_point = 1
            for x2, y2 in (
                    (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x - 1, y + 1), (x + 1, y + 1), (x - 1, y - 1),
                    (x + 1, y - 1)):
                if 0 <= x2 < len(arr) and 0 <= y2 < len(arr[x2]) and arr[x2][y2] >= arr[x][y]:
                    high_point = 0
                    break

            new_array[x][y] = high_point
    return new_array



def risk_score(initial_arr):
    arr = new_get_high_points(initial_arr)

    high_points = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                high_points.append((i, j))

    first_stage = []
    for i in range(len(arr)):
        row_array = []
        for j in range(len(arr[i])):
            row_array.append(0)

        first_stage.append(row_array)

    for start in high_points:
        for cell_x, cell_y in bfs(initial_arr, start):
            first_stage[cell_x][cell_y] += 1
            # first_stage[cell_x][cell_y].append('flood')

    # second_stage = copy.deepcopy(first_stage)
    #
    # for i in range(len(arr)):
    #     for j in range(len(arr[i])):
    #         second_stage[i][j] = len(first_stage[i][j])

    # return second_stage
    return first_stage


print(new_get_high_points([[1, 2, 1, 3, 4],
                           [1, 5, 2, 2, 2],
                           [4, 5, 1, 9, 7],
                           [3, 5, 3, 7, 6],
                           [4, 3, 1, 7, 3]]))

print(bfs([[1, 2, 1, 3, 4],
           [1, 5, 2, 2, 2],
           [4, 5, 1, 9, 7],
           [3, 5, 3, 7, 6],
           [4, 3, 1, 7, 3]], (2, 3)))

print(risk_score([[1, 2, 1, 3, 4],
                  [1, 5, 2, 2, 2],
                  [4, 5, 1, 9, 7],
                  [3, 5, 3, 7, 6],
                  [4, 3, 1, 7, 3]]))
