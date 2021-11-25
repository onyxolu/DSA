
from collections import defaultdict
import heapq

class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        inNodeCount, prerequisite = [[0, i] for i in range(numCourses)], defaultdict(lambda:set())
        for [i,j] in prerequisites:
            prerequisite[i].add(j)
            inNodeCount[j][0]+=1
        while inNodeCount:
            heapq.heapify(inNodeCount)
            top = heapq.heappop(inNodeCount)
            if top[0]>0: return False
            for i in range(len(inNodeCount)):    #Adjust elements
                if inNodeCount[i][1] in prerequisite[top[1]]: inNodeCount[i][0]-=1
        return True