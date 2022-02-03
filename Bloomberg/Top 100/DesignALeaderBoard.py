
import heapq

class Leaderboard:
    def __init__(self):
        self.d = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.d:
            self.d[playerId] = 0
        
        self.d[playerId] += score

    def top(self, K: int) -> int:
        # put d in heap and get largest k scores
        dValues = self.d.values()
        topK = heapq.nlargest(K, dValues)
        return sum(topK)
        ## 0(NlogK) => 0(N) to heapify, logK to pop k elements

    def reset(self, playerId: int) -> None:
        if playerId in self.d:
            del self.d[playerId]