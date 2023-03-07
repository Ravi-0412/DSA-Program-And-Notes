# logic: 1) just find the range in which our ans can lie.
# start= 1 , end= 10**7 * 10**7 because max value of time and totalTrips= 10**7 so suppose a case in which all ele val= 10**7 and totalTrips= 10**7.
# in this case our ans can go upto 10**7 * 10**7.

# Note: so must think the start and end value first properly then only start solving.
# so if you will put end= max(array) or something , you will get wrong ans and in very high constraint restriction TLE also. same for start value also.

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
