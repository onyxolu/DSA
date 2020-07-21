class Solution:
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkrep(item):
            seen = []
            arr = item[::1]
            duplicate = False
            for v in arr:
                if v == ".":
                    continue
                if v in seen:
                    print(v)
                    duplicate = True  
                seen.append(v)
            return duplicate
                            
                    
        col = [[],[],[],[],[],[],[],[],[]]
        subbox = [[],[],[],[],[],[],[],[],[]]
        #check for repitition in rows
        for i, item in enumerate(board):
            col[0].append(item[0])
            col[1].append(item[1])
            col[2].append(item[2])
            col[3].append(item[3])
            col[4].append(item[4])
            col[5].append(item[5])
            col[6].append(item[6])
            col[7].append(item[7])
            col[8].append(item[8])
            rowValid = checkrep(item)
            if rowValid:
                return False
                break
           
        print(col)
        for val in col:
            checkcol = checkrep(val)
            print(checkcol)
            if checkcol:
                return False
                break
            
        for i,v in enumerate(board[::3]):
            firstidx = i * 3
            subbox[firstidx] = [board[firstidx][0], board[firstidx][1], board[firstidx][2], board[firstidx+1][0],board[firstidx+1][1], board[firstidx+1][2], board[firstidx+2][0], board[firstidx+2][1], board[firstidx+2][2]]
            check1 = checkrep(subbox[firstidx])
            if(check1):
                return False
                break
            
            subbox[firstidx+1] = [board[firstidx][3], board[firstidx][4], board[firstidx][5], board[firstidx+1][3],board[firstidx+1][4], board[firstidx+1][5], board[firstidx+2][3], board[firstidx+2][4], board[firstidx+2][5]]
            check2 = checkrep(subbox[firstidx+1])
            print(subbox)
            if(check2):
                return False
                break
                
            subbox[firstidx+2] = [board[firstidx][6], board[firstidx][7], board[firstidx][8], board[firstidx+1][6],board[firstidx+1][7], board[firstidx+1][8], board[firstidx+2][6], board[firstidx+2][7], board[firstidx+2][8]]
            print(subbox)
            check3 = checkrep(subbox[firstidx+2])
            
            if(check3):
                return False
                break
                
        return True
        print(subbox)