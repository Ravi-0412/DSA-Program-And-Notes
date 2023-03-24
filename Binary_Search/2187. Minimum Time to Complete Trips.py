# logic: 1) just find the range in which our ans can lie.
# start= 1 , end= 10**7 * 10**7 because max value of time and totalTrips= 10**7 so suppose a case in which all ele val= 10**7 and totalTrips= 10**7.
# in this case our ans can go upto 10**7 * 10**7.

# Note: so must think the start and end value first properly then only start solving.
# so if you will put end= max(array) or something , you will get wrong ans and in very high constraint restriction TLE also. same for start value also.

# range:
# 1) start: min(time). when there is only one trip to complete then we can take bus with minimum time.
# 2) end:   when there is only bus which take max time i.e 10^7 and we have to complete all the trips.

# time: O(n*log(10**7 * 10**7))
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        def isPossible(minTime):  # we will be abl eto comaplet all the trips in this much time or not?
            trips= 0
            for t in time:
                trips+= (minTime//t)
            return trips >= totalTrips

        start, end= min(time), totalTrips
        while start < end:
            mid= start + (end- start)//2
            if isPossible(mid):
                end= mid
            else:
                start= mid + 1
        return start


# when we get ans for any raneg then , in case we decrease our start and increase our end then also we will get the correct and always.
# how range is taken here:
# 1) start: there is one trip to complete with bus which take only '1' minute(say).
# 2) end:   there is max trip (10^7) to complete with only one bus which take max time (10^7).

# note vvi: we canm just take min possible and max possible according to the constraint given if you don't want to think much. That's it.
# very useful in contest and interview also if you are not able to find the exact possible ans. 
# No need to think just take minimum and max according to constarint and Q logic.

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        def isPossible(minTime):
            trips= 0
            for t in time:
                trips+= (minTime//t)
            return trips >= totalTrips

        start, end= 1, 10**7 * 10**7
        while start < end:
            mid= start + (end- start)//2
            if isPossible(mid):
                end= mid
            else:
                start= mid + 1
        return start



