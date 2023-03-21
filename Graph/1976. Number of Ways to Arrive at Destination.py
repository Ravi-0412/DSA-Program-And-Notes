# Q: we have to find the number of ways we can reach the destination(n-1 node) from the source.

# main crux: we have to find the no of ways we can reach the detination in shortest path.
# but idea here is: the same thing we have to check for node before it.
# that's why we need to keep one more array than the distance i.e ways.

# why exact simple dijkastra will not work?
# Ans: Since we only update distance in Dijkastra when we find the optimal not even "=".
# And here we need to keep track of equal to also for every node then only we will get ans for 'n-1'th node.

# totally same as Dijkastra Algo. You can say 'Dijkastra with DP'.
# since we have to repeat for every node to reach the destonation.

# logic: 1) we will find optimal one for any node i.e 'distance[n2] > w1 + w2' then we will ways[n2]= ways[n1],
#  since we are getting optimal through 'n1' so then no of ways we can reach 'n2' in this optimal distance 'w1+w2' ,
# will be equal to no of ways we reached 'n1' in optimal ways i.e ways[n1]

# 2) if 'distance[n2] == w1 + w2' then, ways[n2]= ways[n2] + ways[n1] since 'n2' is already reachable in this much distance in ways[n2] before only
# And now 'n2' is reachable through 'n1' in same distance so we will add the ways of both 'n1' and 'n2' to get total ways for 'n2'.

import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj= collections.defaultdict(list)
        for s, d, time in roads:
            adj[s].append((d, time))
            adj[d].append((s, time))
        distance= [float('inf')]*n   # use float('inf') instead of any bigger number
        ways=     [0]*n
        heap= [(0, 0)]    # distance, source
        distance[0]= 0
        ways[0]= 1   # no of way to reach source will be deafult '1'.
        visited= set()
        while heap:
            w1, n1= heapq.heappop(heap)
            if n in visited:
                continue
            visited.add(n1)
            for n2, w2 in adj[n1]:
                if n2 not in visited: 
                    # we have found the better ans than before, so simly update the ways with the poped node.
                    if distance[n2] > w1 + w2:
                        distance[n2]= w1 + w2
                        heapq.heappush(heap, (w1 + w2, n2))
                        ways[n2]= ways[n1]
                    # means we have found the path with same shortest path. so add the no of ways of 'n1' to 'n2'
                    elif distance[n2]== w1 + w2:
                        ways[n2]= (ways[n2] + ways[n1]) % (10**9 + 7)
        return ways[n-1] % (10**9 + 7)


# my mistake:  i was thinking to check the mintime when 'n1' got poped with time when it will get poped again by not marking 'n1' as visited but it won't work.
# since we only update when we find optimal one.