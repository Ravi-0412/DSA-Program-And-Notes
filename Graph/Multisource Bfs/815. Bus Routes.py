
"""
Approach 1 (Wrong):
Try to move only on stops connected by the current bus.
- Build edges between all stops on the same bus.
- Track current bus to decide if bus count increases.
- Problem: This approach fails on some test cases because it restricts moves too much.

"""
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
            # from cur_stop, which all stops we can go using cur_bus.
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

"""
Correct Approach (Multi-source BFS):
- From each stop, consider all buses passing through it.
- From these buses, you can reach all their stops.
- Use BFS starting from the source stop:
  - For each stop, take all buses that stop there.
  - For each bus, enqueue all reachable stops.
  - Keep track of visited buses and stops to avoid repeats.
- The answer is the number of buses taken to reach the target.
"""
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0 
        busStop = collections.defaultdict(set)   # [stop : buses_that_we_can_take_from_this_stop]
        for bus, stops in enumerate(routes):
            for stop in stops:
                busStop[stop].add(bus)
        
        q = collections.deque()
        visited_bus = set()   # will store the bus we have taken
        visited_stop = set()  # will store the stops which we have taken. This will avoid in checking same buses again at any stop.
        visited_stop.add(source)
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
                    if bus not in visited_bus:
                        for stop in routes[bus] :
                            if stop == target:
                                return ans
                            if stop not in visited_stop:
                                q.append(stop)
                                visited_stop.add(stop)
                        visited_bus.add(bus)
        return -1
"""    
Note: No need of 'visited' set for stops because all buses at that stop will marked visited
So later for same stop , bus won't get added into queue.
So we can do without this. 
But it may improve time little bit because it will avoid for loop' i.e 'for bus in busStop[curStop].

Note vvi: if we mark 'stop' only as visited instead of 'buses' then we will get TLE.
Reason: At each stop, we are checking the routes of bus which come to that stop.
And len(route) can be 10^5  i.e 'for stop in routes[bus]'.
By marking 'bus' as visited, we avoid this for loop.

And without visited set for 'stop', it is getting accepted because it will suffer for loop
'for bus in busStop[curStop]' which can be maximum '500'. given: '1 <= routes.length <= 500

Note: Better mark both visited and avoid these confusion.
But this may help in other questions i.e if some for loop is causing more repititive thing than other
Then try to avoid that for loop that is causing more repititive thing.
Like we must try to avoid for loop: 'for bus in busStop[curStop]' anyhow then we will think of other one.

Time Complexity:
- O(N * M), where N = number of buses, M = max stops per bus
"""
