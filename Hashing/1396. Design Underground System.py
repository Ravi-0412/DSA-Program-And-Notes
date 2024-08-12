# Logic: 'Average' nikalne ke liye hmko us route ka 'total count' and 'total time' track karna hoga.
# Isko hm ek hashmap se tarck karenge.

# Note: Jb 'checkout' called hoga then hmko ye pta hona chahiye ki ye 'id' wala kahan se checkIn kiya tha
# and kis time pe kiya tha.
# Isko bhi hm ek hashmap se tarck karenge.

# checkIn me hmesha recent wala value rakhenge.

# All operation : O(1)

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
    

# java
# About 'Pair' inbuilt class in java : 
"""
In Java 8, a Pair<V, K> is added in javafx.util package. 
The class represent key-value pairs and supports very basic operations like getKey(), getValue(), hashCode(), equals(java.lang.Object o).
"""

"""
class UndergroundSystem {
    Map<Integer, Pair<String, Integer>> checkInMap = new HashMap<>();  // Uid - {StationName, Time}
    Map<String, Pair<Double, Integer>> routeMap = new HashMap<>(); // RouteName - {TotalTime, Count}

    public UndergroundSystem() {}

    public void checkIn(int id, String stationName, int t) {
        checkInMap.put(id, new Pair<>(stationName, t));
    }

    public void checkOut(int id, String stationName, int t) {
        Pair<String, Integer> checkIn = checkInMap.get(id);
        checkInMap.remove(id); // Remove after using it which will not make HashTable big

        String routeName = checkIn.getKey() + "_" + stationName;
        int totalTime = t - checkIn.getValue();

        Pair<Double, Integer> route = routeMap.getOrDefault(routeName, new Pair<>(0.0, 0));
        routeMap.put(routeName, new Pair<>(route.getKey() + totalTime, route.getValue() + 1));
    }

    public double getAverageTime(String startStation, String endStation) {
        String routeName = startStation + "_" + endStation;
        Pair<Double, Integer> trip = routeMap.get(routeName);
        return trip.getKey() / trip.getValue();
    }
}
"""