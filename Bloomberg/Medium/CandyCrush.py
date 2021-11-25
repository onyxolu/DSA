

# [4,5,6,8,9,0]
# [2,1,1,1,1,4]   crush rows [2,-1,-1,-1,-1,4]
# [3,4,1,6,8,9]   crush col  [3,4,-1,6,8,9]
# [2,8,1,4,6,7]   cursh col  [2,8,-1,4,6,7]

# Step 1: crush rows
# Step 2: crush cols
# Step 3: Gravity

def candyCrush(board):
    if not board:
        return board

    done = True

    # Step 1: Crush Rows
    for r in range(len(board)):
        for c in range(len(board[r]) - 2): # have a window of three items
            # board[r][c] are all positive nums so I need abs to check against prev crushed
            num1 = abs(board[r][c])
            num2 = abs(board[r][c+1])
            num3 = board[r][c+2]

            if num1 == num2 == num3 and num1 != 0:
                board[r][c] = -num1
                board[r][c+1] = -num2
                board[r][c+2] = -num3
                done = False

    # Step 2: Crush Columns
    for c in range(len(board[0])):
        for r in range(len(board) - 2):
            num1 = abs(board[r][c])
            num2 = abs(board[r+1][c])
            num3 = abs(board[r+2][c])

            if num1 == num2 == num3 and num1 != 0:
                board[r][c] = -num1
                board[r+1][c] = -num2
                board[r+2][c] = -num3
                done = False

    # Step 3: Gravity - Move Zeros
    for c in range(len(board[0])):
        # move all positive numbers down
        prevIdx = len(board) - 1
        for r in reversed(range(len(board))):  # bottom up vertically
            if board[r][c] > 0:
                board[prevIdx][c] = board[r][c]
                prevIdx -= 1

        # replace with zeros for missing pieces
        for r in reversed(range(prevIdx +1)):
            board[r][c] = 0

    return board if done else candyCrush(board)
