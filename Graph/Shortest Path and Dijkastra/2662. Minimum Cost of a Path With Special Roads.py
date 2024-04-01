# just Dijkastra only nut we have to keep tarck of few things.

# At every point, there are 3 cases that we need to consider:
# Case 1. The point is at the starting position of a special road, we use this special road.
# Case 2. We can go from the point to a starting position of a special road.
# Case 3. We can go from the point directly to the target.


class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        edges= collections.defaultdict(list)  # will store the special roads. can be may special road from a single point so Dijkastra
        for x1, y1, x2, y2,cost in specialRoads:
            if abs(x1 - x2) + abs(y1 - y2) > cost:  # then only there is benefit in taking special node
                edges[(x1, y1)].append((x2, y2, cost))  
        q= []
        visited= set() 
        q.append((0, start[0], start[1]))
        while q:
            cost, x1, y1= heapq.heappop(q)
            if x1== target[0] and y1== target[1]:
                return cost
            if (x1, y1) in visited:
                continue
            visited.add((x1, y1))
            # check if this is one start position of special node
            if (x1, y1) in edges:
                for x2, y2, c in edges[(x1, y1)]:
                    if (x2, y2) not in visited:
                        heapq.heappush(q, (cost + c, x2, y2))
            # Try to go to any of the starting position of special node
            for x2, y2 in edges:
                if (x2, y2) not in visited:
                    c= abs(x1 - x2) + abs(y1 - y2)   # cost to go to starting point of special node
                    heapq.heappush(q, (cost + c, x2, y2))
            # also add the target cost from the current node
            c= abs(x1- target[0]) + abs(y1 - target[1])
            heapq.heappush(q, (cost + c, target[0], target[1]))
