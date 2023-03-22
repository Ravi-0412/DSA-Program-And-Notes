# just same logic as " Allocate minimum no of pages".

# logic: Given a time, chekc whether all cars can be get repaired or not.
# if possible then decrease the time else increase the time.

# Range: 1) start: given there is only one car wih only one mechanic with rank 1.
# 2) end: given there is max possible car 10^6 and only one mechanic is given to repair all car with max possible rank i.e '100'.

# we use high 10^14 because max(rank) = 100 and max(cars) = 10^6 so, r * n * n = 100 * 10^6 * 10^6 = 10^14

# time: O(n*log(10^14))

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def isRepairPossible(minTime):
            car= 0
            for rank in ranks:
                car+= int(math.sqrt(minTime/rank))
            return car >= cars
        
        n= len(ranks)
        # start= (min(ranks) * cars**2)//n
        # end=   (max(ranks) * cars**2)//n
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
# i thought all mechanic will work simultaneously always. 
# but given in Q 'can': "All the mechanics can repair the cars simultaneously."
# start= (min(ranks) * cars**2)//n
# end=   (max(ranks) * cars**2)//n 
