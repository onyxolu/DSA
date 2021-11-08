class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.find(board,word,i,j):
                        return True
        return False
    def find(self,board,word,row,col,i=0):
        if i == len(word):
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[i]:
            return False
        
        board[row][col] = "#"
        res = self.find(board,word,row,col+1,i+1) or 
        self.find(board,word,row,col-1,i+1) or 
        self.find(board,word,row+1,col,i+1) or 
        self.find(board,word,row-1,col,i+1)
        board[row][col] = word[i]
        
        return res