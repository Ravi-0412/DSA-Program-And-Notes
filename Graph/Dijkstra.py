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
    visited= set()  
    while minHeap:
        w1,n1= heapq.heappop(minHeap)    # it means for this node, we have got the optimal ans so we will relax all the nodes to this node
        if n1 in visited:    # since we are marking any node visited only we have relaxed all the outgoing edge through that vertex
                            #  so there can be many instances of same node in the minHeap and once we have releaxed all the edges through that node 
                            # then, no need to relax all the edged through that node again anymore so simply skip
            continue
        visited.add(n1)     # only mark visited if we have are going to relax all of the outgoing edge from the curr node. 
        for n2, w2 in edges[n1]:
            if n2 not in visited:
                if distance[n2] > w1+ w2:
                    distance[n2]= w1+w2
                    # visited.add(n2)       # this will give incorrect ans. this is one more diff from Bfs
                                            # you can only add any node to visited if ypu have found the optimal ans for that node i.e when you will pop

                # when we push more than one ele in heap, 
                # it create the min/max heap acc to the 1st ele(1st pushed ele)
                heapq.heappush(minHeap,(distance[n2], n2))  
    return distance


# another way of writing (better one)
def ShortestPath1(adj,n, src):
    edges= defaultdict(list)  # converting into adjacency list with adjacent edges and their weights
    for u,v,w in adj:
        edges[u].append((v,w))
    distance= [9999999]*n
    distance[src]= 0   # will conatin the distance of source to all other vertices
    minHeap= [(0,src)]  # first ele should be weight as it will create the heap using 1st ele always
    visited= set()  
    while minHeap:
        w1,n1= heapq.heappop(minHeap)    # it means for this node, we have got the optimal ans so we will relax all the nodes to this node
        if n1 in visited:    # since we are marking any node visited only we have relaxed all the outgoing edge through that vertex
                            #  so there can be many instances of same node in the minHeap and once we have releaxed all the edges through that node 
                            # then, no need to relax all the edged through that node again anymore so simply skip
            continue
        distance[n1]= w1  # poped one means we have found minimum distance of that
        visited.add(n1)     # only mark visited if we have are going to relax all of the outgoing edge from the curr node. 
        for n2, w2 in edges[n1]:
            if n2 not in visited:  # if not viisted then simply add in minHeap
                heapq.heappush(minHeap,(w1+w2, n2))  
    return distance
adj= [[0,1,10],[0,2,5],[1,3,1],[1,2,2],[2,1,3],[2,4,2],[2,3,9],[3,4,4],[4,0,7],[4,3,6]]
# print(ShortestPath(adj, 5, 0))
print(ShortestPath1(adj, 5, 0))


