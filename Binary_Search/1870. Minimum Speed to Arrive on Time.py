# logic vvi : We only need to wait between two trains, so do a ceiling division of (distance/speed) for all trains 
# but after the last one we don't have to wait so for last do exact division.

# method 1:
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n= len(dist)

        def possibleToReach(mid):
            totalHour= 0
            # last train don't have to wait
            for d in dist[: -1]:
                totalHour+= ceil(d/mid)   # since we can only start at integer time. 
            # for last train only have to add the time.
            totalHour+= dist[n-1] / mid
            return totalHour <= hour

        start= 1
        end= 10**7 + 1   # to handle 'not possible' case
        while start < end:
            mid= start + (end - start)//2
            if possibleToReach(mid):
                end= mid
            else:
                start= mid + 1
        return start if start != 10**7 + 1 else -1


# method 2: Better one

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n= len(dist)
        # we have to take each train and we can only start train at 'integer' .
        # # so minimum time required will at least 'n-1' hour + time taken by the last train. 
        if hour <= n-1:
            return -1

        def possibleToReach(mid):
            totalHour= 0
            # The last train will not need to wait.
            for d in dist[: -1]:
                totalHour+= ceil(d/mid)
            totalHour+= dist[n-1] / mid
            return totalHour <= hour

        start= 1   # Atleast we have to take one train then in that case only travel time will add & that can be less than '1' also.
        end= 10**7   # max ans can go till this only.  
        while start < end:
            mid= start + (end - start)//2
            if possibleToReach(mid):
                end= mid
            else:
                start= mid + 1
        return start


# Note: in this we don't know the max range of ans so taken the largest possible one.