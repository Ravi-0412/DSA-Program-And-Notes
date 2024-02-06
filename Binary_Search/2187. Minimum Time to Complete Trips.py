# logic: 1) just find the range in which our ans can lie.
# start= 1 , end= 10**7 * 10**7 because in case if there is only one bus having time = 10**7 and totaltrips = 10**7

# Note: so must think the start and end value first properly then only start solving.
# so if you will put end= max(array) or something , you will get wrong ans and in very high constraint restriction TLE also. 
# same for start value also.

# when we get ans for any range then , in case we decrease our start and increase our end then also we will get the correct and always.
# how range is taken here:
# 1) start: there is one trip to complete with bus which take only '1' minute(say).
# 2) end:   there is max trip (10^7) to complete with only one bus which take max time (10^7).

# note vvi: we can just take min possible and max possible according to the constraint given if you don't want to think much. That's it.
# very useful in contest and interview also if you are not able to find the exact possible ans. 
# No need to think just take minimum and max according to constarint and Q logic.

# time: O(n*log(10**7 * 10**7))

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


# Related Q:
# 2594. Minimum Time to Repair Cars


