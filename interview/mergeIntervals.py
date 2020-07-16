class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      
        if len(intervals) == 2:
            if (intervals[0][1] >= intervals[1][0]):
                if (intervals[0][1] >= intervals[1][0]):
                    sleft = sorted([intervals[0][0] , intervals[1][0]])
                    sright = sorted([intervals[0][1] , intervals[1][1]]) 
                    if(intervals[1][0] == 0) and (intervals[1][1] == 0):
                        return [[sleft[0], sright[0]], [sleft[1], sright[1]]]
                   
                return [ [sleft[0], sright[1]]]

    
        for i in range(len(intervals) - 2):
            list1 = intervals[i]
            list2 = intervals[i+1]
            l1 = intervals[i][0]
            l2 = intervals[i][1]
            r1 = intervals[i+1][0]
            r2 = intervals[i+1][1]
            print(l1,l2,r1,r2)
            if ( l2 >= r1 ):
                sleft = sorted([l1 , r1])
                sright = sorted([l2 , r2]) 
                mergedList = [sleft[0], sright[1]]
                intervals[i] = mergedList 
                intervals.remove(intervals[i+1])
        return intervals
            