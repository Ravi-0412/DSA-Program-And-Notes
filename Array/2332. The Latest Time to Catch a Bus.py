# Logic:
# Return the latest time you may arrive at the bus station to catch a bus is same as: 
# "Return the maximum late possible time for which you can board the bus".
# i.e latest == late

# How to approach?
# Here we have to come as late as possible and still be able to board on the bus.
# We have to come late, so definitely the optimal approach is to board on the last bus as far as possible.
# Cases:
# 1) Last bus is not full: We can reach at bus time, but we have to make sure that our time should not clash with any other passenger.
# 2) Last bus is full: We have to reach before the last person which is on board and 
# we have to make sure that our time should not clash with any other passenger.

# TC: O(NlogN) + O(MlogM)
# SC: O(1)

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        n , m = len(buses) , len(passengers)
        i, j = 0, 0   # will denote the cur indices of 'bus' and 'passengers'
        # start keeping passengers in bus one by one
        while i < n:
            # we can only put in cur bus if bus is not full and arrival time of passenger <= departure time of bus
            curCapacity = 0
            while j < m and curCapacity < capacity and passengers[j] <= buses[i]:
                j += 1
                curCapacity += 1

            # we wil only try to board the last bus. so check if cur bus is last bus
            if i == n - 1:
                j -= 1  # we will check from last boarded passenger so '-1'. 
                # case 1) if last bus is empty 
                if curCapacity < capacity:
                    possibleArrivalTime = buses[i]
                    # check if there is already some passenger with this arrival time so keep on decreasing till you get any unique time
                    while j >= 0 and possibleArrivalTime == passengers[j]:
                        possibleArrivalTime -= 1
                        j -= 1

                    return possibleArrivalTime

                # 2) if last bus if full then we need to come before arrival time of last boarded passenger
                else:  
                    possibleArrivalTime = passengers[j] - 1
                    j -= 1    # have to reach before the last boarded passenger otherwise we won't be able to get the bus
                              # so here we will compare from the 2nd last boarded for unique value
                    # check if there is already some passenger with this arrival time so keep on decreasing till you get any unique time
                    while j >= 0 and possibleArrivalTime == passengers[j]:
                        j -= 1
                        possibleArrivalTime -= 1

                    return possibleArrivalTime 

            i += 1


# Method 2: very very concise way of above same logic only.
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        passengers.sort()
        buses.sort()
        cur = 0
        cap = 0

        for time in buses:
            cap = capacity
            while cur < len(passengers) and passengers[cur] <= time and cap > 0:
                cur += 1
                cap -= 1
        # will try to arrive <= departure time of last bus only if bus is not full else before arrival time of last boarded passenger
        best = buses[-1] if cap > 0 else passengers[cur - 1]
        # Now check if this time 'best' is not matching with any of the passenger arraival time
        passengers = set(passengers)
        while best in passengers:
            best -= 1
        return best


# My mistake:
# if not possible then also we can get more bigger time.
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        
        def isPossibleToReach(time):
            noBuses = bisect.bisect_right(buses, time)
            noPassenger = bisect.bisect_right(passengers, time)
            print(time, noBuses, noPassenger , noBuses * capacity, "time")
            return noPassenger < noBuses * capacity

        buses.sort()
        passengers.sort()
        print(buses , passengers , "buses")
        start = 2
        end = buses[-1]

        while start <= end:
            mid = start + (end - start)//2
            print(mid, isPossibleToReach(mid), "mid")
            if isPossibleToReach(mid):
                start = mid + 1
            else:
                end = mid - 1
        return end


# Do by binary search also.
