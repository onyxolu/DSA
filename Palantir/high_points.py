# def get_high_points(arr):
#     if len(arr) == 1 and len(arr[0]) == 1:
#         return arr
#
#     new_array = []
#     for i in range(len(arr)):
#         row_array = []
#         for j in range(len(arr[i])):
#             row_array.append(0)
#
#         new_array.append(row_array)
#
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             neighbors = []
#             if i == 0:
#                 if len(arr) > 1:
#                     neighbors.append(arr[i + 1][j])
#                 if (j == 0 or 0 < j < len(arr[i]) - 1) and len(arr[i]) > 1:
#                     neighbors.append(arr[i][j + 1])
#                     if len(arr) > 1:
#                         neighbors.append(arr[i + 1][j + 1])
#                 if (j == len(arr[i]) - 1 or 0 < j < len(arr[i]) - 1) and len(arr[i]) > 1:
#                     neighbors.append(arr[i][j - 1])
#                     if len(arr) > 1:
#                         neighbors.append(arr[i + 1][j - 1])
#             elif i == len(arr) - 1:
#                 neighbors.append(arr[i - 1][j])
#                 if (j == 0 or 0 < j < len(arr[i]) - 1) and len(arr[i]) > 1:
#                     neighbors.append(arr[i][j + 1])
#                     neighbors.append(arr[i - 1][j + 1])
#                 if (j == len(arr[i]) - 1 or 0 < j < len(arr[i]) - 1) and len(arr[i]) > 1:
#                     neighbors.append(arr[i][j - 1])
#                     neighbors.append(arr[i - 1][j - 1])
#             else:
#                 neighbors.append(arr[i - 1][j])
#                 neighbors.append(arr[i + 1][j])
#                 if (j == 0 or 0 < j < len(arr[i]) - 1) and len(arr[i]) > 1:
#                     neighbors.append(arr[i + 1][j + 1])
#                     neighbors.append(arr[i][j + 1])
#                     neighbors.append(arr[i - 1][j + 1])
#                 if (j == len(arr[i]) - 1 or 0 < j < len(arr[i]) - 1) and len(arr[i]) > 1:
#                     neighbors.append(arr[i + 1][j - 1])
#                     neighbors.append(arr[i][j - 1])
#                     neighbors.append(arr[i - 1][j - 1])
#
#             new_array[i][j] = 1 if arr[i][j] > max(neighbors) else 0
#
#     return new_array


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
#
