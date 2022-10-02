# using min heap, time: 0(E*logV). Every edge will get relaxed exactly one time 
# logic: same as Bfs only diff is we use here min_heap instead of Q with weight

from collections import defaultdict
import heapq
def ShortestPath(adj,n, src):
    edges= defaultdict(list)  # converting into adjacency list with adjacent edges and their weights
    for u,v,w in adj:
        edges[u].append((v,w))
    distance= [9999999]*n
    distance[src]= 0   # will conatin the distance of source to all other vertices
    minHeap= [(0,src)]  # first ele should be weight as it will create the heap using 1st ele always
    visited= set()  # better use an array since searching in set will take O(n) for each time..visited tells whether that node has been relaxed or not
    while minHeap:
        w1,n1= heapq.heappop(minHeap)
        if n1 in visited:
            continue
        visited.add(n1)
        for n2, w2 in edges[n1]:
            if n2 not in visited:
                if distance[n2] > w1+ w2:
                    distance[n2]= w1+w2
                # when we push more than one ele in heap, 
                # it create the min/max heap acc to the 1st ele(1st pushed ele)
                heapq.heappush(minHeap,(distance[n2], n2))  
    return distance

adj= [[0,1,10],[0,2,5],[1,3,1],[1,2,2],[2,1,3],[2,4,2],[2,3,9],[3,4,4],[4,0,7],[4,3,6]]
print(ShortestPath(adj, 5, 0))


