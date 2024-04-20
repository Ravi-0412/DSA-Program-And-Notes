# mostly same logic as Dijkastra
# not able to print the exact path(edges). Have to ask someone
from collections import defaultdict
import heapq
def Prim(adj, src, n):
    edges= defaultdict(list)
    parent= [-1]*n
    for u,v,w in adj:
        edges[u].append((v,w))
        edges[v].append((u,w))
    visited= set()
    min_mst= 0
    min_heap= [(0,src)]   # you can start with any node this, will not affect the ans 
    while len(visited)< n:
        w1,n1= heapq.heappop(min_heap)
        print(n1, end="-")
        if n1 in visited:  # this will automatically check whether all nodes get included or not. so no need to check the condition "if len(visited)==n:"
            continue
        visited.add(n1)
        min_mst+= w1   # different from Dijkastra.. Adding the weight of edges coming under MST
        for n2,w2 in edges[n1]:
            if n2 not in visited:
                parent[n2]= n1
                heapq.heappush(min_heap,(w2, n2))  # here little change from dijkastra as in this we have to add the weight of all edges which will be come under MST
                                                   # Instead of adding 'w1+w2' like Dijkastra here adding only 'w2'.

    print("cost of minimum spanning tree is:", min_mst)

# adj= [[0,1,28],[0,5,10],[1,0,28],[1,6,14],[1,2,16],[2,1,16],[2,3,12],[3,6,18],[3,2,12],[3,4,22],[4,6,24],[4,5,25],[5,0,10],[4,3,22],[5,4,25],[6,1,14],[6,4,24],[6,3,18]] # ans= 99
adj= [[0,2,3],[1,3,4],[1,2,10],[2,1,10],[2,3,2],[2,4,6],[2,0,3],[3,1,4],[3,2,2],[3,4,1],[4,2,6],[4,3,1]]  # ans= 10
# Prim(adj, 0, 7)
Prim(adj, 0, 5)


# Note: Whenever you are asked directly or indirectly to find the :
# 1) minimum cost to connect all points/nodes (or anything) gievn some cost/distance between each point
# 2) 