def canReach(x1, y1, x2, y2):
    while True:
        if (x1 == x2 and y2 == y1):
            return 'Yes'
        elif (x2 < x1 or y2 < y1 or x2 == y2):
             return 'No'
        if (x2 > y2):
             x2 -= y2
        elif (y2 > x2):
            y2 -= x2

