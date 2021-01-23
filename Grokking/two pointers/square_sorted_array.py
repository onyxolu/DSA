arr = [-2, -1, 0, 2, 3]

def make_squares(arr):
    highest_square_idx = len(arr) - 1
    left = 0
    right = len(arr) - 1
    square = [0 for x in range(len(arr))]

    while left <= right:
        left_square = (arr[left]) ** 2
        right_square = (arr[right]) ** 2

        if left_square > right_square:
            square[highest_square_idx] = left_square
            left += 1
        else:
            square[highest_square_idx] = right_square
            right -= 1

        highest_square_idx -= 1

    return square


print(make_squares(arr))
