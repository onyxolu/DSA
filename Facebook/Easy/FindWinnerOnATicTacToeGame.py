
from collections import List

# create row and col array and initialize with 0's [0 0 0] [0 0 0]
# create d1 and d2 for the two diagonals
#  creater player , 1 for player1 and -1 for player2
# four ways to know if you win, 3 entries in same row/col, three entries in diagonal

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        rows, cols = [0]*n, [0]*n
        d1, d2 = 0,0
        player = 1
        for r,c in moves:
            rows[r] += player
            cols[c] += player
            if r==c: # [0,0] [1,1] [2,2]
                d1 += player
            if r+c == n-1: # [0,2] [1,1] [0,2]
                d2 += player
            if abs(rows[r]) == n or abs(cols[c]) == n or abs(d1) == n or abs(d2) == n:
                if player == 1:
                    return "A"
                else:
                    return "B"
                
            player *= -1
        if len(moves) == (n*n):
            return "Draw"
        else:
            return "Pending"
            
            
        