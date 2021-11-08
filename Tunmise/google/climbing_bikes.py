#using bucket sort
def assignBikes(self, workers, bikes):
        m, n = len(workers), len(bikes) 
        
        def manhattan(a, b):
            (x1, y1), (x2, y2) = a, b
            return abs(x1-x2) + abs(y1-y2)
            
        buckets = [[] for _ in range(2001)]
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                buckets[manhattan(worker, bike)] += (i, j),
        
        bikes, taken = [n] * m, set()
        for bucket in buckets:
            if len(taken) == m:
                break
            for i, j in bucket:
                if bikes[i] == n and j not in taken:
                    bikes[i] = j 
                    taken.add(j)
        return bikes
##normal sort
def assignBikes2(self, workers, bikes):
        m, n = len(workers), len(bikes) 
        
        def manhattan(a, b):
            (x1, y1), (x2, y2) = a, b
            return abs(x1-x2) + abs(y1-y2)
        
        def sort_key(pair):
            i, j = pair
            return (manhattan(workers[i], bikes[j]), i, j)
            
        output, taken = [n] * m, set()
        for i, j in sorted(((i, j) for i in range(m) for j in range(n)), key = sort_key):
            if len(taken) == m:
                break
            if output[i] == n and j not in taken:
                output[i] = j
                taken.add(j)
        return output

#heap
from heapq import heapify, heappop
def assignBikes3(self, workers, bikes):
        m, n = len(workers), len(bikes) 
        
        def manhattan(a, b):
            (x1, y1), (x2, y2) = a, b
            return abs(x1-x2) + abs(y1-y2)
            
        h = [(manhattan(worker, bike), i, j)
                for i, worker in enumerate(workers)
                for j, bike in enumerate(bikes)]
        heapify(h)
        
        output, taken = [n] * m, set()
        while len(taken) != m:
            _, i, j = heappop(h)
            if output[i] == n and j not in taken:
                output[i] = j
                taken.add(j)
        return output