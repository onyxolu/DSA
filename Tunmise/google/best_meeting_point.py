#convert 2D -> 1D, sorting, median return sum
#time complexity = 0(mn)
def minTotalDistance(self, grid):
    m = len(grid)
    n = len(grid[0])

    rows = []
    cols = []

    for row in range(m):
        for col in range(n):
            if grid[row][col]:
                rows.append(row)
                cols.append(col)

    rows.sort()
    cols.sort()

    med_row = rows[len(rows) // 2]
    med_col = cols[len(cols)// 2]

    return sum(abs(row-med_row) for row in rows) + sum(abs(col-med_col) for col in cols)



        
