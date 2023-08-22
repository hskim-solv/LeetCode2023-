class UndergroundSystem:

    def __init__(self):
        self.times = defaultdict(list)
        self.iin = defaultdict(list)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.iin[id] += [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        if id in self.iin:
            self.times[(self.iin[id][0],stationName)].append( t-self.iin[id][1] )
            del self.iin[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.times[(startStation,endStation)]) / len(self.times[(startStation,endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)