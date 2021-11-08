# Tuple => We need to find a way to store the stationName, id and time

from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.checkOuts = defaultdict(lambda:(0,0))
        self.checkIns = {}
         

    def checkIn(self, id: int, stationName: str, t: int) -> None: 
        self.checkIns[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkIns[id]
        totalTime, trips = self.checkOuts[(startStation, stationName)] 
        self.checkOuts[(startStation, stationName)] = (totalTime + (t - startTime), trips + 1)
    
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, trips = self.checkOuts[(startStation, endStation)]
        return totalTime / trips



        


# Your UndergroundSystem object will be instantiated and called as such:
obj = UndergroundSystem()
obj.checkIn(45, "Leyton", 3)
obj.checkOut(45, "Waterloo", 15)
param_3 = obj.getAverageTime("Leyton", "Waterloo")

print(param_3)