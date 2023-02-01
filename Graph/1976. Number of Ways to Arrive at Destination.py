# Q: we have to find the number of ways we can reach the destination(n-1 node) from the source.

# main crux: we have to find the no of ways we can reach the dstination in shortest path.
# but idea here is: the same thing we have to check for node before it.
# that's why we need to keep one more array than the distance i.e ways.

# totally same as Dijkastra Algo. You can say 'Dijkastra with DP'.
# since we have to repeat for every node to reach the destonation.

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
        ways[0]= 1
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
