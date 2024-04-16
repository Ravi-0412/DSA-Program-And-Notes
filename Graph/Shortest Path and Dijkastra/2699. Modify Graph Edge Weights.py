# Logic: 1st find distance to all nodes using only positive weight like normal Dijkastra.
# Now compare distance[destination] with 'target':
# 1) if 'distance[destination] < target' then there won't be any possible way
# Because after making any weight negative -> positive , distance[destination] will decrease only
# because there will be more possible paths to take after adding the any edge and that will result in lesser distance only.
# So simply return []

# 2) If 'distance[destination] == target' in this case it is better to not add any edge otherwise weight of destination
# will decrease only. For this  make all weight having negative weight = maximum large value so that all automatically 
# get skipped because of very large value. 

# 3) else: if 'distance[destination] > target', in this case if we will include other edges then 'distance[destination]'
# will decrease.
# But we don't need to check every possible value for each negative weight and backtrack.
# Just for each negative weight put weight = 1 and again call 'Dijkastra' and then use above
# two case with little modification. We will get any one of possible ans.

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
        # Case 1:
        if dist[destination] < target:
            return []
        # case 2:
        if dist[destination]== target:
            # then update those '-'1 with any very large no such that it doesn't consider that path while calculating the distance of destination
            for edge in edges:
                if edge[2]== -1:
                    edge[2]= 10**9
            return edges
        
        # Case 3: Now try to update the "-ve" weight with weight = 1
        for i in range(len(edges)):
            s, d, w=  edges[i]
            if w== -1:  
                edges[i][2]= 1
                # Add the weight into adjacency list.
                # Before we had not added these.
                adj[s].append((d, edges[i][2]))
                adj[d].append((s, edges[i][2]))

                # Now apply Dijkastra Algo
                distance= [float('inf')] * n
                Dijkastra(distance)
                
                # utilising the two cases i.e when 'distance[destination] <= target'
                if distance[destination] <= target:
                    # means we have found path from source to destination. 
                    # so just add remaining distance to cur edge and make other edge weight= very large number
                    # update the value of cur edge with remaining value
                    edges[i][2]+= target - distance[destination]  # remaining value.
                    # Now update the remaining edge (from i+1) to very large value like above
                    for j in range(i+1, len(edges)):
                        if edges[j][2] == -1:
                            edges[j][2]= 10**9
                    return edges
                # if distance[destination] > target:then assign other edges weight = 1 and check
        # if in case we can't reach to deestination in distance= target
        return []






            