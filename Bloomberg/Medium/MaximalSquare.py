
# Looping through the whole values and for each comparing with others will take 0(nm)^2

# So are we repeating any work? so create a cache reping max area for each cell as top right
# Is there a subproblem?

# 0(m*n)
# Recursive top down 

class Solution:
    def maximalSquare(self, matrix) -> int:
        # Recursive top down 
        # Time = 0(n*m), Space = 0(n*m)
        
        rows, cols = len(matrix), len(matrix[0])
        cache = {} # map each (r,c) => maxLength of square
        
        def helper(r,c):
            if r >= rows or c >= cols:
                return 0
            
            if (r,c) not in cache:
                down = helper(r+1, c)
                right = helper(r, c+1)
                diag = helper(r+1, c+1)
                
                cache[(r,c)] = 0
                if matrix[r][c] == "1":
                    cache[(r,c)] = 1 + min(down,right, diag)
                    
            return cache[(r,c)]
        
        helper(0,0)
        return max(cache.values()) ** 2


# dp bottom up

import itertools

class Solution:
    def maximalSquare(self, matrix) -> int:
	#    ''' 
	# 	   Time : O(n*m) 
	# 	   Idea : Every cell of matrix represent the square possible of length cell-val with that cell as bottom-right cell in that square
	#    '''
	   # use matrix as dp to save space
        ROWS, COLS = len(matrix), len(matrix[0])
        for i in range(ROWS):
            for j in range(COLS):
                if not(i and j):  # for first row & col
                    matrix[i][j] = int(matrix[i][j])
                    continue
                if matrix[i][j] == '0': # constraints as per problem
                    matrix[i][j] = 0
                    continue
					
                # explore cell (i, j) as bottom-right cell for possible square
                diagTopLeft = matrix[i-1][j-1]
                top = matrix[i-1][j]
                left = matrix[i][j-1]
				# update matrix aka dp here
                matrix[i][j] = 1 + min(diagTopLeft, top, left)  # 1 minimum ie self itself of length 1

        return max(itertools.chain(*matrix))**2