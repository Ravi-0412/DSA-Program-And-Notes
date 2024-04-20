# exactly same as Prim's algo
# logic: 1st make adjacency list
# after that it is totally same as prim's algo.

# for adjacency list we will have to take distance between every pair of node,
# and all node will be adjacnet to each other  => O(n^2)

# Time: o(E*logV) + O(n^2)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj= defaultdict(list)
        for i in range(len(points)):
            x1,y1= points[i]
            for j in range(i+1, len(points)):
                x2,y2= points[j]
                distance= abs(x1-x2) + abs(y1-y2)
                adj[i].append((j,distance))
                adj[j].append((i,distance))

        # after this totally prim's algo
        visited= set()
        min_mst= 0
        min_heap= [(0,0)]  # (weight, node)
        while len(visited) < len(points):
            w1,n1= heapq.heappop(min_heap)
            if n1 in visited:
                continue
            visited.add(n1)
            min_mst+= w1
            for n2,w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap,(w2, n2))
        return min_mst


# my mistake: i was creating adjacency list like this
for i in range(len(points)//2 +1):  # if you do like this then you will miss all the edges after mid to the remaining nodes
    x1,y1= points[i]
    for j in range(i+1,len(points)):
        if i==j:
            continue
        x2,y2= points[j]
        distance= abs(x1-x2) + abs(y1-y2)
        adj[i].append((j,distance))
        adj[j].append((i, distance))