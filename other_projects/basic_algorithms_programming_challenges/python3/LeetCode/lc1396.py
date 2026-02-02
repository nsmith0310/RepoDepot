class UndergroundSystem:

    def __init__(self):
        self.combo = dict()
        self.ind = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ind[id] = [t,stationName]
            
                
            
                 

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        try:
            
            self.combo[self.ind[id][1]+":"+stationName].append(t - self.ind[id][0])
        except:
            self.combo[self.ind[id][1]+":"+stationName] = [t - self.ind[id][0]]
        del self.ind[id]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        t = 0
        c = 0
        for x in self.combo[startStation+":"+endStation]:
            t+=x
            c+=1
        return t/c


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
