class UndergroundSystem:
    
    def __init__(self):
        self.checkInMap= {}  # id -> (startStation, time)
        self.routeMap= {}    # (startStation, endStation) -> (time, count)
        # for calculating the ans, we need the "sum of diff of time" and "no of times that route has been taken".


    def checkIn(self, id: int, startStation: str, t: int) -> None:
        self.checkInMap[id]= (startStation, t)
        

    def checkOut(self, id: int, endStation: str, t: int) -> None:
        # find the station and time at which this person was checked in
        startStation, time= self.checkInMap[id]
        route= (startStation, endStation)
        if route not in self.routeMap:
            self.routeMap[route]= [0, 0]
        # add the diff of time and no of time this route has been taken
        self.routeMap[route][0] += t - time
        self.routeMap[route][1] += 1


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time, count= self.routeMap[(startStation, endStation)]
        return time / count