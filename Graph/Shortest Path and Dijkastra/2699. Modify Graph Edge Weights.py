# time: O(n^2)

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:

        def Dijkastra(distance):
            distance[source]= 0
            minHeap= []
            visited= set()
            heapq.heappush(minHeap, (0, source))   # [weight, node]
            while minHeap:
                w1, n1= heapq.heappop(minHeap)   # [weight, node]
                if n1 in visited:
                    continue
                visited.add(n1)
                distance[n1]= w1
                for n2, w2 in adj[n1]:
                    if n2 not in visited:
                        heapq.heappush(minHeap, (w1 + w2, n2))

        # code starts from here
        adj= collections.defaultdict(list)
        # first make the adjacency list considering only the positive weight.
        for u, v,w in  edges:
            if w== -1:
                continue
            adj[u].append((v, w))  
            adj[v].append((u, w))

        
        dist= [float('inf')]*n     # distance array
        # Apply normal Dijakstra considering only the positive edge
        Dijkastra(dist)
        if dist[destination] < target:
            # After updating the weight of edge = -1 to any +ve value will make distance even more bigger.
            # so not possible
            return []
        if dist[destination]== target:
            # then update those '-'1 with any very large no such that it doesn't consider that path while calculating the distance of destination
            for edge in edges:
                if edge[2]== -1:
                    edge[2]= 10**9
            return edges
        
        # Now try to update the "-ve" weight
        for i in range(len(edges)):
            s, d, w=  edges[i]
            if w== -1:  # if weight= -1
                edges[i][2]= 1  # start updating wuth value= '1'.
                # Add the weight into adjacency list.
                # Before we had not added these.
                adj[s].append((d, edges[i][2]))
                adj[d].append((s, edges[i][2]))

                # Now apply Dijkastra Algo
                distance= [float('inf')] * n
                Dijkastra(distance)
                
                if distance[destination] <= target:
                    # means we have found path from source to destination. 
                    # so just make add remaining distance to cur edge and make other edge weight= very large number
                    # update the value of cur edge with remaining value
                    edges[i][2]+= target - distance[destination]  # remaining value.
                    # Now update the remaining edge (from i+1) to very large value like above
                    for j in range(i+1, len(edges)):
                        if edges[j][2] == -1:
                            edges[j][2]= 10**9
                    return edges
        # if in case we can't reach to deestination in distance= target
        return []






            