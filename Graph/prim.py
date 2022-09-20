# mostly same logic as Dijkastra

from collections import defaultdict
import heapq
def Prim(adj, src, n):
    edges= defaultdict(list)
    parent= [-1]*n
    distance= [9999999]*n
    distance[src]= 0
    for u,v,w in adj:
        edges[u].append((v,w))
    visited= set()
    min_mst= 0
    min_heap= [(0,src)]
    while len(visited)< n:
        w1,n1= heapq.heappop(min_heap)
        if n1 in visited:
            continue
        visited.add(n1)
        min_mst+= w1
        for n2,w2 in edges[n1]:
            if n2 not in visited:
                parent[n2]= n1
                heapq.heappush(min_heap,(w2, n2))
    # for printing the path
    # print("Edge \tweight")
    # for i in range(1,n):
    #     print(parent[i], "-",i, "t", )

    print("cost of minimum spanning tree is:", min_mst)

# adj= [[0,1,28],[0,5,10],[1,0,28],[1,6,14],[1,2,16],[2,1,16],[2,3,12],[3,6,18],[3,2,12],[3,4,22],[4,6,24],[4,5,25],[5,0,10],[4,3,22],[5,4,25],[6,1,14],[6,4,24],[6,3,18]]
adj= [[0,2,3],[1,3,4],[1,2,10],[2,1,10],[2,3,2],[2,4,6],[2,0,3],[3,1,4],[3,2,2],[3,4,1],[4,2,6],[4,3,1]]
# Prim(adj, 0, 7)
Prim(adj, 0, 5)
