# Logic: when we are any stop , which all stops we can go.
# for this we can take all buses route that goes through this stop.
# Then can go to all those stops


# i.e multisource bfs
# Time: Have to ask someone

# Note one thing vvi: we are poping the stops but marking bus no as visited

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0 
        busStop = collections.defaultdict(set)   # [stop : buses_that_we_can_take_from_this_stop]
        for bus, stops in enumerate(routes):
            for stop in stops:
                busStop[stop].add(bus)
        
        q = collections.deque()
        visited = set()   # will store the bus we have taken
        q.append(source)
        ans = 0
        while q :
            ans += 1
            for i in range(len(q)):
                curStop = q.popleft()
                # which all stops we can reach from cur stop
                # for this 1st we need to go to all the buses that come at this stop
                for bus in busStop[curStop]:
                    # then include all stops where the cur bus goes
                    if bus not in visited:
                        for stop in routes[bus]:
                            if stop == target:
                                return ans
                            q.append(stop)
                    visited.add(bus)
        return -1


# if we mark 'stop' as visited instead of 'buses' then we will get TLE.
# Reason: At each stop, we are checking the routes of bus which come to that stop.
# And len(route) can be 10^5 .

# So it is better to mark bus as visited to skip checking all those routes every time.

# Note: if any Q gives TLE then it is better to see the constraint and modify like above solution.
# For modification always see the whether you are doing repititive thing and where you are wasting a lot of your time.

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0 
        busStop = collections.defaultdict(set)   # [stop : buses_that_we_can_take_from_this_stop]
        for bus, stops in enumerate(routes):
            for stop in stops:
                busStop[stop].add(bus)
        
        q = collections.deque()
        visited = set()   # will store the bus we have taken
        q.append(source)
        visited.add(source)
        ans = 0
        while q :
            ans += 1
            for i in range(len(q)):
                curStop = q.popleft()
                # which all stops we can reach from cur stop
                # for this 1st we need to go to all the buses that come at this stop
                for bus in busStop[curStop]:
                    # then include all stops where the cur bus goes
                    for stop in routes[bus]:
                        if stop == target:
                            return ans
                        if stop not in visited:
                            q.append(stop)
                            visited.add(stop)
        return -1


# 1st approach come in mind is:
# But giving wrong ans for test case : 18 , don't know why. Have to ask someone.

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        adj = collections.defaultdict(list)
        # first make adjacency list
        # in same bus we can reach to any of the stop from one another where the cur bus stops
        source_bus_number = None
        for i in range(len(routes)):
            stops = routes[i]
            if source in stops:
                source_bus_number = i
            # every stop should be reachable to one another in same bus
            # so there be edge between every pair
            for j in range(len(stops) - 1):
                for k in range(j + 1, len(stops)):
                    u, v = stops[j] , stops[k]
                    adj[u].append((v, i))
                    adj[v].append((u, i))
        q = collections.deque()
        q.append((source, source_bus_number , 1))   # (stop, cur_bus, busTaken)
                # cur_bus will check whether we are changing the bus or not
        visited = set() 
        visited.add(source)
        while q:
            stop, cur_bus, busTaken = q.popleft()
            for stop1, bus in adj[stop]:
                if stop1 not in visited:
                    if stop1 == target:
                        return busTaken if cur_bus == bus else busTaken + 1
                    if cur_bus == bus:
                        q.append((stop1, bus, busTaken))
                    else:
                        q.append((stop1, bus, busTaken + 1))
                    visited.add(stop1)
        return -1

            




