# understand properly the range mistake and that didn't work.


# logic: Given a time, chekc whether all cars can be get repaired or not.
# if possible then decrease the time else increase the time.

# Range: 1) start: given there is only one car wih only one mechanic with rank 1.
# 2) end: given there is max possible car 10^6 and only one mechanic is given to repair all car with max possible rank i.e '100'.

# we use high 10^14 because max(rank) = 100 and max(cars) = 10^6 so, r * n * n = 100 * 10^6 * 10^6 = 10^14

# Note: for range try to generalise the value, don't think acc to the particular case . just generalise this.

# time: O(n*log(10^14))

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def isRepairPossible(minTime):  # Given a time, chekc whether all cars can be get repaired or not.
            car= 0
            for rank in ranks:
                car+= int(math.sqrt(minTime/rank))
            return car >= cars
        
        n= len(ranks)
        start, end= 1, 100*(10**6)**2
        while start < end:
            mid= start + (end- start)//2
            # print(mid)
            if isRepairPossible(mid):
                end= mid
            else:
                start= mid + 1
        return start
    

# my mistake in range:

# start= (min(ranks) * cars**2)  # when lowest rank mechanic repair all car
# end=   (max(ranks) * cars**2)  # when max rank mechanic repair all car

# why wrong?
# Thought correct only but other mechanic can also work in parallel (any of them can work parallely)
# But we are not sure that how many will work in parallel .
# so this time our guess for range is not working.

# when you are not sure i.e Q like this then, just generalise the start and end value (take number directly which can be start and end).